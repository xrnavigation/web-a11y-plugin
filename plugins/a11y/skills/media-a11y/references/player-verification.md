# Verify the delivered player and assets

Use this as a project verification procedure. Record the player, browser,
operating system and screen reader versions, media URL, selected tracks, and
observed results. An asset list alone is not a completed test.

## Content review

1. Watch with sound muted and captions enabled. Compare cues with the audio:
   check words, timing, meaningful sounds and speaker changes. Check captions do
   not cover relevant visual content. A dialogue-only translation can omit
   information that accessibility captions need
   ([WAI captions](https://www.w3.org/WAI/media/av/captions/)).
2. Listen with the picture hidden. Compare with the video: can listeners obtain
   the relevant displayed values, actions and text? Check description timing
   against dialogue; integrated narration or a separate described video are
   possible delivery methods
   ([WAI description](https://www.w3.org/WAI/media/av/description/)).
3. Read the transcript separately. Confirm equivalent sound and visual content,
   speaker identification and sequence. For AAA prerecorded synchronized media,
   audio description alone does not supply the text alternative
   ([Understanding 1.2.8](https://www.w3.org/WAI/WCAG22/Understanding/media-alternative-prerecorded.html)).
4. For a live event, rehearse caption provision, then check the actual event.
   Record omissions and delays rather than counting a scheduled service as
   evidence of usable output ([WAI captions](https://www.w3.org/WAI/media/av/captions/)).

## Player review

Exercise play/pause, seeking, volume/mute, caption selection and description
selection where provided, then leave the player using only the keyboard. Check
visible focus, clear control labels, control states and contrast. Repeat with
page zoom and the project's screen reader combinations; verify the controls
operate, rather than prescribing exact spoken strings
([WAI player](https://www.w3.org/WAI/media/av/player/)).

Check real description delivery. If timed text is used, confirm the player reads
the descriptions at the intended moments. If pauses are insufficient, confirm
the supported extended-description method pauses the video appropriately. For a
separate audio track or described version, verify users can select/access it and
hear the complete presentation. The player/platform must support the chosen
method ([WAI description](https://www.w3.org/WAI/media/av/description/)).

Project recommendation: begin playback on user request. If audio plays
automatically for more than three seconds, WCAG A 1.4.2 requires pause/stop or
volume control independent of system volume
([WCAG 2.2, 1.4.2](https://www.w3.org/TR/WCAG22/)).

## Report template

```text
Media classification and target level:
Required assets / optional additions:
Assets reviewed and specific omissions:
Player / browser / OS / screen reader versions:
Actions tested and observed results:
Description delivery tested:
Untested combinations or unavailable assets:
```

Keep “not tested” distinct from “failed” and “passed.” Do not claim a complete
WCAG evaluation from media-only review.
