"""Validate skill structure, metadata, local references and citation registration.

Run: uv run --with pyyaml python scripts/check_skills.py
This checks artifact integrity; it does not establish accessibility correctness.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

import yaml


def check(root: Path) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    rows = []
    skills = root / "plugins/a11y/skills"
    allowed_fields = {"name", "description", "license", "compatibility", "metadata",
                      "allowed-tools", "argument-hint", "context", "agent",
                      "disable-model-invocation", "user-invocable"}
    directories = sorted(p for p in skills.iterdir() if p.is_dir())
    names = {p.name for p in directories}
    for directory in directories:
        prefix = directory.name
        entry = directory / "SKILL.md"
        if not entry.is_file():
            errors.append(f"{prefix}: missing SKILL.md")
            continue
        body = entry.read_text(encoding="utf-8-sig")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", body, re.S)
        if not match:
            errors.append(f"{prefix}: missing YAML frontmatter")
            continue
        try:
            meta = yaml.safe_load(match[1])
            if not isinstance(meta, dict):
                raise ValueError("expected mapping")
        except (yaml.YAMLError, ValueError) as exc:
            errors.append(f"{prefix}: invalid frontmatter: {exc}")
            continue
        if meta.get("name") != prefix or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", prefix) or len(prefix) > 64:
            errors.append(f"{prefix}: invalid or mismatched name")
        desc = meta.get("description")
        if not isinstance(desc, str) or not desc.strip() or len(desc) > 1024:
            errors.append(f"{prefix}: invalid description")
        for key in meta.keys() - allowed_fields:
            errors.append(f"{prefix}: unknown frontmatter key {key}")
        lines = len(body[match.end():].splitlines())
        if lines >= 500:
            errors.append(f"{prefix}: body has {lines} lines (must be below 500)")
        registry = directory / "references/sources.yaml"
        common = directory / "references/common-mistakes.md"
        if not common.is_file():
            errors.append(f"{prefix}: missing references/common-mistakes.md")
        urls: set[str] = set()
        if not registry.is_file():
            errors.append(f"{prefix}: missing references/sources.yaml")
        else:
            try:
                data = yaml.safe_load(registry.read_text(encoding="utf-8-sig"))
                entries = []
                def collect(value):
                    if isinstance(value, dict):
                        if "url" in value or "urls" in value:
                            entries.append(value)
                        else:
                            for child in value.values():
                                collect(child)
                    elif isinstance(value, list):
                        for child in value:
                            collect(child)
                collect(data)
                if not entries:
                    raise ValueError("expected nonempty source records")
                for source in entries:
                    values = [source["url"]] if "url" in source else source["urls"]
                    if not isinstance(values, list) or not all(isinstance(v, str) for v in values):
                        raise ValueError("source needs URL strings")
                    urls.update(v.rstrip("/") for v in values)
            except (yaml.YAMLError, ValueError) as exc:
                errors.append(f"{prefix}: invalid source registry: {exc}")
        for doc in sorted(directory.rglob("*.md")):
            text = doc.read_text(encoding="utf-8-sig")
            # Inline markdown targets, excluding anchors and external URLs.
            for target in re.findall(r"\]\(([^)\s]+)(?:\s+[^)]*)?\)", text):
                target = target.strip("<>")
                if target.startswith(("http://", "https://")):
                    if target.rstrip("/") not in urls:
                        errors.append(f"{prefix}/{doc.relative_to(directory)}: unregistered citation {target}")
                elif not target.startswith("#"):
                    dest = (doc.parent / target.split("#", 1)[0]).resolve()
                    if not dest.is_file():
                        errors.append(f"{prefix}/{doc.relative_to(directory)}: broken link {target}")
            if doc != entry and len(text.splitlines()) > 100 and not re.search(r"^## (?:Contents|Table of [Cc]ontents)\s*$", text, re.M):
                warnings.append(f"{prefix}/{doc.relative_to(directory)}: long reference lacks contents")
            # Companion skill names use code spans. Only audit known-prefix names.
            for sibling in re.findall(r"`(a11y-[a-z-]+)`", text):
                if sibling not in names:
                    warnings.append(f"{prefix}/{doc.relative_to(directory)}: unknown companion {sibling}")
        rows.append({"name": prefix, "body_lines": lines})
    for manifest in ["plugins/a11y/.claude-plugin/plugin.json",
                     "plugins/a11y/.codex-plugin/plugin.json",
                     ".claude-plugin/marketplace.json", ".agents/plugins/marketplace.json"]:
        try:
            json.loads((root / manifest).read_text(encoding="utf-8-sig"))
        except (OSError, ValueError) as exc:
            errors.append(f"{manifest}: {exc}")
    return {"skills": rows, "errors": sorted(set(errors)),
            "warnings": sorted(set(warnings))}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = check(args.root)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{len(result['skills'])} skills; {len(result['errors'])} errors; {len(result['warnings'])} warnings")
        for kind in ("errors", "warnings"):
            for finding in result[kind]:
                print(f"{kind[:-1].upper()}: {finding}")
    return bool(result["errors"])


if __name__ == "__main__":
    sys.exit(main())
