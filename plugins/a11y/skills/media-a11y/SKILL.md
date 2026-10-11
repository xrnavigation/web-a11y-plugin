---
name: media-a11y
description: Guides accessible audio, video, livestreams, and media players, including captions, transcripts, audio description, and player verification. Use when adding media, reviewing caption quality, choosing description delivery, or building player controls.
---

# Accessible audio and video

Classify the media before choosing alternatives. Record whether it is live or
prerecorded, audio-only, silent video-only, or synchronized audio/video; identify
information supplied only by sound or sight. Apply the [requirements matrix](references/requirements-matrix.md),
then verify content and player behavior separately. These distinctions determine
WCAG media requirements ([WAI planning](https://www.w3.org/WAI/media/av/planning/)).

## Core principles

- Plan description in the script: say the useful chart values or demonstrated
  action, rather than only “as you can see” ([WAI overview](https://www.w3.org/WAI/media/av/)).
- Preserve equivalent information. Captions include meaningful sounds and speaker
  identification, not only translated dialogue; transcripts are separate text,
  not a replacement for required synchronized captions
  ([WAI captions](https://www.w3.org/WAI/media/av/captions/),
  [WAI transcripts](https://www.w3.org/WAI/media/av/transcripts/)).
- At AA, provide required visual information in audio; a descriptive transcript
  alone does not satisfy 1.2.5. Additional description is unnecessary when the
  main soundtrack already conveys all important visual information
  ([Understanding 1.2.5](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-prerecorded.html)).
- Choose description delivery together with the player. Timed text descriptions
  require playback support; shipping a file is not evidence that users can hear
  it ([WAI description](https://www.w3.org/WAI/media/av/description/)).

## When adding media

1. Use the [matrix](references/requirements-matrix.md) to list required assets and
   any optional additions. Do not claim a text-alternative exception simply
   because the video also has a transcript.
2. Review caption text against the complete audio, correcting recognition errors,
   missing speakers and meaningful sounds, and timing. Automatic captions need
   confirmation of accuracy ([WAI captions](https://www.w3.org/WAI/media/av/captions/)).
3. Listen without viewing the video. Add descriptions for missing visual meaning,
   such as a silent demonstration or an on-screen warning. Choose integrated
   narration, a described version, or player-supported description
   ([WAI description](https://www.w3.org/WAI/media/av/description/)).
4. Put a descriptive transcript near the player and include relevant visual
   information in sequence, not merely exported dialogue
   ([WAI transcripts](https://www.w3.org/WAI/media/av/transcripts/)).
5. Run the [player verification procedure](references/player-verification.md).
   Keyboard access, visible focus, labels and contrast are player concerns as
   well as content concerns ([WAI player](https://www.w3.org/WAI/media/av/player/)).

## HTML example

Example assets below are placeholders for reviewed media and captions. Serve
the media and WebVTT from the same origin for this example. `kind`, `srclang`,
`label` and `default` identify the text track; `default` remains subject to user
preferences ([HTML track element](https://html.spec.whatwg.org/multipage/media.html#the-track-element)).

```html
<figure>
  <figcaption id="demo-title">Replacing a filter (2 minutes)</figcaption>
  <video controls preload="metadata" aria-labelledby="demo-title">
    <source src="/media/filter.mp4" type="video/mp4">
    <track kind="captions" src="/media/filter.en.vtt"
           srclang="en" label="English captions" default>
    <p><a href="/media/filter.mp4">Download the video</a></p>
  </video>
  <p><a href="/media/filter-transcript.html">Descriptive transcript</a></p>
  <p><a href="/media/filter-described.html">Video with audio description</a></p>
</figure>
```

The described-version link illustrates a delivery choice; create and test that
version, including its captions. Do not replace it with an untested
`<track kind="descriptions">` and assume narration: description playback depends
on the player/platform ([WAI description](https://www.w3.org/WAI/media/av/description/)).

## Common mistakes and evidence

Read [wrong/right examples](references/common-mistakes.md) for transcript-only
video, uncorrected captions, and unsupported description tracks. Report which
assets and player/browser/screen reader combinations were inspected, the actual
observed behavior, and what remains untested. Do not invent spoken output or
claim WCAG conformance from this markup example.

Source provenance: [sources.yaml](references/sources.yaml).
