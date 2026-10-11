# Autocomplete Attribute Values
## Contents

- [Personal Information](#personal-information)
- [Authentication](#authentication)
- [Address](#address)
- [Payment / Credit Card](#payment-credit-card)
- [Contact](#contact)
- [Other](#other)
- [Modifiers](#modifiers)
  - [Scope: section-{name}](#scope-section-name)
  - [Purpose: shipping / billing](#purpose-shipping-billing)
  - [Contact Type: home / work / mobile / fax / pager](#contact-type-home-work-mobile-fax-pager)
  - [Control Keywords: on / off](#control-keywords-on-off)
  - [WebAuthn: webauthn](#webauthn-webauthn)
- [Token Order](#token-order)


Use supported `autocomplete` tokens to expose applicable input purposes. SC 1.3.5 covers fields collecting information about the user, with purposes in its taxonomy and supported technology; it does not require this attribute on every field. Whether a browser actually autofills is separate from exposing purpose ([Identify Input Purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html)).

Source: [HTML Spec: Autofill](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill)

---

## Personal Information

| Value | Purpose |
|---|---|
| `name` | Full name |
| `honorific-prefix` | Prefix/title (Mr., Ms., Dr.) |
| `given-name` | First name |
| `additional-name` | Middle name |
| `family-name` | Last name |
| `honorific-suffix` | Suffix (Jr., III) |
| `nickname` | Nickname / handle |
| `organization-title` | Job title |
| `organization` | Company / organization name |
| `username` | Username or account identifier |

---

## Authentication

| Value | Purpose |
|---|---|
| `new-password` | New password (registration, password change) |
| `current-password` | Existing password (login) |
| `one-time-code` | SMS/email verification code, TOTP |

---

## Address

| Value | Purpose |
|---|---|
| `street-address` | Full street address (may be multiline) |
| `address-line1` | Street address line 1 |
| `address-line2` | Street address line 2 (apt, suite) |
| `address-line3` | Street address line 3 |
| `address-level4` | Finest administrative level |
| `address-level3` | Third administrative level |
| `address-level2` | City / town |
| `address-level1` | State / province / region |
| `country` | Country code (ISO 3166-1 alpha-2) |
| `country-name` | Country name (localized) |
| `postal-code` | ZIP / postal code |

---

## Payment / Credit Card

| Value | Purpose |
|---|---|
| `cc-name` | Full name on card |
| `cc-given-name` | First name on card |
| `cc-additional-name` | Middle name on card |
| `cc-family-name` | Last name on card |
| `cc-number` | Card number |
| `cc-exp` | Expiration date (MM/YY or MM/YYYY) |
| `cc-exp-month` | Expiration month |
| `cc-exp-year` | Expiration year |
| `cc-csc` | Security code (CVV/CVC) |
| `cc-type` | Card type (Visa, Mastercard, etc.) |
| `transaction-currency` | Currency for transaction |
| `transaction-amount` | Amount for transaction |

---

## Contact

| Value | Purpose |
|---|---|
| `tel` | Full phone number |
| `tel-country-code` | Country code (+1, +44) |
| `tel-national` | National phone number (without country code) |
| `tel-area-code` | Area code |
| `tel-local` | Local phone number (without area/country code) |
| `tel-extension` | Extension |
| `email` | Email address |
| `impp` | Instant messaging protocol URL |

---

## Other

| Value | Purpose |
|---|---|
| `language` | Preferred language (BCP 47 tag) |
| `bday` | Birthday (full date) |
| `bday-day` | Birthday day |
| `bday-month` | Birthday month |
| `bday-year` | Birthday year |
| `sex` | Sex / gender |
| `url` | Home page or profile URL |
| `photo` | Photo / avatar URL |

---

## Modifiers

Modifiers are prepended to the base values above.

### Scope: `section-{name}`

Groups related fields so the browser knows they belong together. Useful when a form has multiple instances of the same field type (e.g., two phone numbers).

```html
<input autocomplete="section-primary tel" name="main-phone">
<input autocomplete="section-emergency-contact tel" name="emergency-phone">
```

### Purpose: `shipping` / `billing`

Distinguishes address and contact fields by purpose.

```html
<input autocomplete="shipping street-address" name="ship-street">
<input autocomplete="billing street-address" name="bill-street">
```

### Contact Type: `home` / `work` / `mobile` / `fax` / `pager`

Qualifies telephone and email fields.

```html
<input autocomplete="work email" name="work-email">
<input autocomplete="mobile tel" name="cell">
```

### Control Keywords: `on` / `off`

- `on` — enable autofill (default)
- `off` — disable autofill (use sparingly; browsers may ignore this)

### WebAuthn: `webauthn`

For passkey/credential fields in WebAuthn authentication flows.

```html
<input autocomplete="webauthn" name="credential">
```

---

## Token Order

When combining modifiers, use this order:

```
[section-*] [shipping|billing] [home|work|mobile|fax|pager] <base-value>
```

Example:
```html
<input autocomplete="section-ship billing work tel" name="work-billing-phone">
```
