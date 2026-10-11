# Media mistakes: wrong and right

These abbreviated examples show decisions, not full implementations or tested
browser behavior.

## Transcript replaces captions

Wrong for prerecorded synchronized video with meaningful audio:

```html
<video controls src="interview.mp4"></video>
<a href="interview-transcript.html">Transcript</a>
```

Right: retain the transcript and add reviewed synchronized captions:

```html
<video controls src="interview.mp4">
  <track kind="captions" src="interview.en.vtt"
         srclang="en" label="English captions">
</video>
<a href="interview-transcript.html">Descriptive transcript</a>
```

Separate text does not satisfy the required synchronized captions. Captions
preserve speech and meaningful non-speech sound alongside the video
([WCAG 2.2, 1.2.2](https://www.w3.org/TR/WCAG22/#time-based-media),
[WAI captions](https://www.w3.org/WAI/media/av/captions/)).

## Speech text is treated as a descriptive transcript

Wrong when a result appears only on screen:

```html
<p>Presenter: Here is the result.</p>
```

Right: include the missing visual information in sequence:

```html
<p>Presenter: Here is the result.</p>
<p>[The display reads: Test passed. Pressure: 40 kPa.]</p>
```

Descriptive transcripts include relevant visual information as well as audio.
For AA synchronized prerecorded video, also convey that visual meaning through
audio; the transcript alone does not meet 1.2.5
([WAI transcripts](https://www.w3.org/WAI/media/av/transcripts/),
[Understanding 1.2.5](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-prerecorded.html)).

## Description track is assumed to be spoken everywhere

Wrong: treat this element alone as completed description delivery:

```html
<track kind="descriptions" src="demo-description.en.vtt"
       srclang="en" label="English descriptions">
```

Right: connect and test it with a player that supports spoken text descriptions,
or supply a tested described version:

```html
<a href="demo-described.html">Demo with audio description</a>
```

Text description requires player support and suitable timing or pause behavior.
Verify the chosen platform instead of promising screen reader narration
([WAI description](https://www.w3.org/WAI/media/av/description/)).

## Generated captions accepted without review

Wrong process:

```text
Generate captions -> publish
```

Right process:

```text
Generate captions -> compare with actual audio -> correct text and timing
-> check meaningful sounds and speakers -> verify delivered captions
```

Recognition output is a starting point; unconfirmed accuracy does not establish
usable captions ([WAI captions](https://www.w3.org/WAI/media/av/captions/)).
