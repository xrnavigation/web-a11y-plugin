# Semantic expectation catalog

These are expectations to test, not guaranteed utterances or observed transcripts.
Use `at-experience-verification` to record actual behavior.

| Markup | Expected information |
|---|---|
| `<h2>Products</h2>` | Heading named Products, level 2 |
| `<a href="/pricing">Pricing</a>` | Link named Pricing, navigation destination |
| `<button>Send</button>` | Button named Send, native activation |
| Labeled input | Field name, relevant type, value and invalid state when set |
| Checkbox | Name and checked/unchecked state |
| Expanded disclosure | Button name and expanded/collapsed state |
| Named dialog | Dialog role/name and useful initial focus |
| Status update | Intended polite feedback; observe actual timing and speech |

Role/state semantics: [WAI-ARIA](https://www.w3.org/TR/wai-aria-1.2/).
Native field names: [WAI labels](https://www.w3.org/WAI/tutorials/forms/labels/).
Do not copy exact sentences into acceptance criteria; require conveyed meaning
and task completion, then capture observed wording for the tested environment.
