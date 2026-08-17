# HTML Element to Implicit ARIA Role Mapping
## Contents

- [Key Concepts](#key-concepts)
- [Interactive Elements](#interactive-elements)
- [Sectioning and Landmark Elements](#sectioning-and-landmark-elements)
- [Structural Elements](#structural-elements)
- [Table Elements](#table-elements)
- [Text-Level Elements](#text-level-elements)
- [Media and Embedded Elements](#media-and-embedded-elements)
- [Elements That MUST NOT Have Role Overridden](#elements-that-must-not-have-role-overridden)
- [Redundant ARIA — Do Not Add](#redundant-aria-do-not-add)


Source: [ARIA in HTML — W3C Editor's Draft](https://w3c.github.io/html-aria/)
Section: "Rules of ARIA attribute usage by HTML element"

This table defines the implicit ARIA role for each HTML element and whether authors may override it. When an element already has the implicit role you need, adding `role="..."` is redundant and should be omitted.

## Key Concepts

- **Implicit ARIA Role**: The role the browser automatically assigns to the element in the accessibility tree
- **Can Override?**: Whether `role="..."` is allowed on this element
- **No**: Authors MUST NOT set a role on this element
- **Limited**: Only certain specific roles are allowed
- **Yes**: Any role (or a broad set) is allowed

## Interactive Elements

| HTML Element | Conditions | Implicit ARIA Role | Can Override? | Notes |
|---|---|---|---|---|
| `<a>` | with `href` | `link` | Limited | Allowed: button, checkbox, menuitem, menuitemcheckbox, menuitemradio, option, radio, switch, tab, treeitem |
| `<a>` | without `href` | `generic` | Yes | Any role |
| `<button>` | normal context | `button` | Limited | Allowed: checkbox, combobox, link, menuitem, menuitemcheckbox, menuitemradio, option, radio, slider, switch, tab, treeitem |
| `<button>` | first child of `<select>` | `button` | **No** | Inert context |
| `<details>` | — | `group` | **Limited** | group only |
| `<dialog>` | — | `dialog` | Limited | Allowed: alertdialog |
| `<input type="button">` | — | `button` | Limited | Allowed: checkbox, combobox, link, menuitem, menuitemcheckbox, menuitemradio, option, radio, switch, tab, treeitem |
| `<input type="checkbox">` | — | `checkbox` | Limited | Allowed: button (with aria-pressed), menuitemcheckbox, option, switch |
| `<input type="color">` | — | No corresponding role | **No** | — |
| `<input type="date">` | — | No corresponding role | **No** | — |
| `<input type="datetime-local">` | — | No corresponding role | **No** | — |
| `<input type="email">` | no `list` attr | `textbox` | **Limited** | textbox only |
| `<input type="file">` | — | No corresponding role | **No** | — |
| `<input type="hidden">` | — | No corresponding role | **No** | — |
| `<input type="image">` | — | `button` | Limited | Same as button |
| `<input type="month">` | — | No corresponding role | **No** | — |
| `<input type="number">` | — | `spinbutton` | **Limited** | spinbutton only |
| `<input type="password">` | — | No corresponding role | **No** | — |
| `<input type="radio">` | — | `radio` | Limited | Allowed: menuitemradio |
| `<input type="range">` | — | `slider` | **Limited** | slider only |
| `<input type="reset">` | — | `button` | Limited | Same as button |
| `<input type="search">` | no `list` attr | `searchbox` | **Limited** | searchbox only |
| `<input type="submit">` | — | `button` | Limited | Same as button |
| `<input type="tel">` | no `list` attr | `textbox` | **Limited** | textbox only |
| `<input type="text">` | no `list` attr | `textbox` | Limited | Allowed: combobox, searchbox, spinbutton |
| `<input type="text">` | with `list` attr | `combobox` | **Limited** | combobox only |
| `<input type="time">` | — | No corresponding role | **No** | — |
| `<input type="url">` | no `list` attr | `textbox` | **Limited** | textbox only |
| `<input type="week">` | — | No corresponding role | **No** | — |
| `<select>` | no `multiple`, no `size` > 1 | `combobox` | Limited | Allowed: menu |
| `<select>` | `multiple` or `size` > 1 | `listbox` | **Limited** | listbox only |
| `<textarea>` | — | `textbox` | **Limited** | textbox only |

## Sectioning and Landmark Elements

| HTML Element | Conditions | Implicit ARIA Role | Can Override? | Notes |
|---|---|---|---|---|
| `<article>` | — | `article` | Limited | Allowed: application, document, feed, main, none, presentation, region |
| `<aside>` | — | `complementary` | Limited | Allowed: feed, none, note, presentation, region, search |
| `<footer>` | not in sectioning content | `contentinfo` | Limited | Allowed: doc-footnote, group, none, presentation |
| `<footer>` | in sectioning content | `generic` | Limited | Allowed: doc-footnote, group, none, presentation |
| `<header>` | not in sectioning content | `banner` | Limited | Allowed: group, none, presentation |
| `<header>` | in sectioning content | `generic` | Limited | Allowed: group, none, presentation |
| `<main>` | — | `main` | **Limited** | main only |
| `<nav>` | — | `navigation` | Limited | Allowed: menu, menubar, none, presentation, tablist |
| `<search>` | — | `search` | Limited | Allowed: form, group, none, presentation, region |
| `<section>` | with accessible name | `region` | Limited | Allowed: alert, alertdialog, application, banner, complementary, contentinfo, dialog, document, feed, log, main, marquee, navigation, none, note, presentation, search, status, tabpanel |
| `<section>` | without accessible name | `generic` | Limited | Same as above |

## Structural Elements

| HTML Element | Conditions | Implicit ARIA Role | Can Override? | Notes |
|---|---|---|---|---|
| `<blockquote>` | — | `blockquote` | Yes | Any role |
| `<div>` | normal context | `generic` | Yes | Any role |
| `<div>` | child of `<dl>` | `generic` | Limited | presentation, none only |
| `<fieldset>` | — | `group` | Limited | Allowed: none, presentation, radiogroup |
| `<figure>` | with `<figcaption>` | `figure` | **Limited** | figure only |
| `<figure>` | without `<figcaption>` | `figure` | Yes | Any role |
| `<form>` | — | `form` | Limited | Allowed: none, presentation, search |
| `<h1>`–`<h6>` | — | `heading` | Limited | Allowed: none, presentation, tab |
| `<hr>` | — | `separator` | Limited | Allowed: none, presentation, doc-pagebreak |
| `<li>` | child of `<ol>`/`<ul>`/`<menu>` | `listitem` | **Limited** | listitem only |
| `<li>` | not child of list | `generic` | Yes | Any role |
| `<ol>` | — | `list` | Limited | Allowed: directory, group, listbox, menu, menubar, none, presentation, radiogroup, tablist, toolbar, tree |
| `<p>` | — | `paragraph` | Yes | Any role |
| `<span>` | — | `generic` | Yes | Any role |
| `<ul>` | — | `list` | Limited | Same as `<ol>` |

## Table Elements

| HTML Element | Conditions | Implicit ARIA Role | Can Override? | Notes |
|---|---|---|---|---|
| `<table>` | — | `table` | Yes | Any role |
| `<tbody>` | — | `rowgroup` | Yes | Any role |
| `<td>` | in table context | `cell` or `gridcell` | Limited | Depends on parent table role |
| `<tfoot>` | — | `rowgroup` | Yes | Any role |
| `<th>` | in table context | `columnheader`/`rowheader`/`cell` | Limited | Depends on scope and parent |
| `<thead>` | — | `rowgroup` | Yes | Any role |
| `<tr>` | in table context | `row` | **Limited** | row only |

## Text-Level Elements

| HTML Element | Conditions | Implicit ARIA Role | Can Override? | Notes |
|---|---|---|---|---|
| `<b>` | — | `generic` | Yes | Any role |
| `<code>` | — | `code` | Yes | Any role |
| `<del>` | — | `deletion` | Yes | Any role |
| `<dfn>` | — | `term` | Yes | Any role |
| `<em>` | — | `emphasis` | Yes | Any role |
| `<i>` | — | `generic` | Yes | Any role |
| `<ins>` | — | `insertion` | Yes | Any role |
| `<mark>` | — | No corresponding role | Yes | Any role |
| `<s>` | — | `deletion` | Yes | Any role |
| `<small>` | — | `generic` | Yes | Any role |
| `<strong>` | — | `strong` | Yes | Any role |
| `<sub>` | — | `subscript` | Yes | Any role |
| `<sup>` | — | `superscript` | Yes | Any role |
| `<u>` | — | `generic` | Yes | Any role |

## Media and Embedded Elements

| HTML Element | Conditions | Implicit ARIA Role | Can Override? | Notes |
|---|---|---|---|---|
| `<audio>` | — | No corresponding role | Limited | application only |
| `<canvas>` | — | No corresponding role | Yes | Any role |
| `<embed>` | — | No corresponding role | Limited | application, document, img, presentation, none |
| `<iframe>` | — | No corresponding role | Limited | application, document, img, none, presentation |
| `<img>` | with alt text | `img` | Limited | Allowed: button, checkbox, link, menuitem, menuitemcheckbox, menuitemradio, option, progressbar, radio, scrollbar, separator, slider, switch, tab, treeitem |
| `<img>` | empty `alt`, no accessible name | `presentation`/`none` | **Limited** | presentation, none only |
| `<object>` | — | No corresponding role | Limited | application, document, img |
| `<svg>` | — | `graphics-document` | Yes | Any role |
| `<video>` | — | No corresponding role | Limited | application only |

## Elements That MUST NOT Have Role Overridden

These elements have **No** in the override column — authors MUST NOT add `role="..."`:

- `<area>` (with `href`)
- `<base>`, `<col>`, `<colgroup>`, `<head>`, `<link>`, `<map>`, `<meta>`
- `<input type="color">`, `<input type="date">`, `<input type="datetime-local">`, `<input type="file">`, `<input type="hidden">`, `<input type="month">`, `<input type="password">`, `<input type="time">`, `<input type="week">`
- `<label>` (when associated with a form control)
- `<legend>`
- `<noscript>`, `<param>`, `<picture>`, `<script>`, `<slot>`, `<source>`, `<style>`, `<template>`, `<title>`, `<track>`
- `<button>` (when first child of `<select>`)
- `<summary>` (when child of `<details>`)
- `<selectedcontent>` (when child of `<select>`)

## Redundant ARIA — Do Not Add

These combinations are redundant and should be omitted (the element already has the implicit role):

| Do NOT write | Because |
|---|---|
| `<nav role="navigation">` | `<nav>` already maps to `navigation` |
| `<main role="main">` | `<main>` already maps to `main` |
| `<button role="button">` | `<button>` already maps to `button` |
| `<a href="..." role="link">` | `<a href>` already maps to `link` |
| `<input type="checkbox" role="checkbox">` | Already maps to `checkbox` |
| `<input type="radio" role="radio">` | Already maps to `radio` |
| `<input type="range" role="slider">` | Already maps to `slider` |
| `<input type="number" role="spinbutton">` | Already maps to `spinbutton` |
| `<textarea role="textbox">` | Already maps to `textbox` |
| `<select role="combobox">` | Already maps to `combobox` (single) |
| `<select role="listbox">` | Already maps to `listbox` (multiple) |
| `<table role="table">` | Already maps to `table` |
| `<tr role="row">` | Already maps to `row` |
| `<td role="cell">` | Already maps to `cell` |
| `<th role="columnheader">` | Already maps to `columnheader` |
| `<aside role="complementary">` | Already maps to `complementary` |
| `<header role="banner">` | Already maps to `banner` (top-level) |
| `<footer role="contentinfo">` | Already maps to `contentinfo` (top-level) |
| `<ol role="list">` / `<ul role="list">` | Already maps to `list` |
| `<li role="listitem">` | Already maps to `listitem` (in list context) |
| `<form role="form">` | Already maps to `form` |
| `<article role="article">` | Already maps to `article` |
| `<img role="img">` | Already maps to `img` |
| `<output role="status">` | Already maps to `status` |
| `<progress role="progressbar">` | Already maps to `progressbar` |
| `<dialog role="dialog">` | Already maps to `dialog` |
