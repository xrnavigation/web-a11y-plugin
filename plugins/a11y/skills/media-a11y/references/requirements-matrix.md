# Media requirements matrix

Use each applicable row. Higher conformance levels include lower-level
requirements; the columns below show **additions**. This table covers Guideline
1.2, not every requirement affecting media or players
([WCAG 2.2](https://www.w3.org/TR/WCAG22/#time-based-media)).

| Media | A | AA additions | AAA additions |
|---|---|---|---|
| Prerecorded audio-only | Equivalent text alternative, 1.2.1 | None in 1.2 | None in 1.2 |
| Prerecorded silent video-only | Equivalent text alternative **or** audio track, 1.2.1 | None in 1.2 | Text alternative, 1.2.8 |
| Prerecorded synchronized audio/video | Captions, 1.2.2; audio description **or** full text alternative, 1.2.3 | Audio description, 1.2.5 | Sign language, 1.2.6; extended description when ordinary pauses are insufficient, 1.2.7; full text alternative, 1.2.8 |
| Live audio-only | None in 1.2 | None in 1.2 | Equivalent text alternative, 1.2.9 |
| Live silent video-only | None in 1.2 | None in 1.2 | None in 1.2 |
| Live synchronized audio/video | None in 1.2 | Live captions, 1.2.4 | None in 1.2 |

The matrix derives from [WCAG 2.2, SC 1.2.1–1.2.9](https://www.w3.org/TR/WCAG22/#time-based-media).

## Apply exceptions to the correct content

SC 1.2.1, 1.2.2 and 1.2.3 explicitly except media that is an alternative for text
and clearly labeled as such. This means the media presents no information beyond
the existing text or its text alternatives. A transcript added to an original
video does not turn the original into an alternative for text. For example,
label a recording “Audio version of the following article” only if its actual
content matches. WCAG's definition of synchronized media also excludes clearly
labeled media alternatives for text; apply that definition when determining
scope, rather than inventing exceptions
([Understanding 1.2.3, criterion and key terms](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-or-media-alternative-prerecorded.html)).

A full text alternative contains visual and auditory information in the correct
sequence and a way to achieve any time-based interaction outcomes. A screenplay
must match the final edited media, not an earlier script
([Understanding 1.2.3](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-or-media-alternative-prerecorded.html)).

## Classify borderline examples

Classify caption content rather than its marketing label. “Subtitles” can mean
accessibility captions in some regions or translated dialogue in others. A
dialogue-only translation omits meaningful non-speech sound; translated captions
can preserve it. Check the actual information provided
([WAI captions](https://www.w3.org/WAI/media/av/captions/)).

- **Podcast with speech only:** audio-only still needs an equivalent transcript
  at A; synchronized captions are a useful addition rather than a 1.2.2
  requirement ([WAI planning](https://www.w3.org/WAI/media/av/planning/)).
- **Talking-head video with speech:** captions remain required at A. If all
  important visual information is already spoken, extra description is
  unnecessary; verify names, titles and displayed text before making that finding
  ([Understanding 1.2.5](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-prerecorded.html)).
- **Silent demonstration:** provide descriptive text or equivalent audio at A.
  If an audio track exists, inspect what it contributes before treating the
  content as video-only; tell users when captions or description are unnecessary
  ([WAI planning](https://www.w3.org/WAI/media/av/planning/)).
- **Live broadcast saved for replay:** assess the saved recording as prerecorded
  media. “Live” describes transmission from a real event with only broadcast
  delay, not an exemption retained by every replay
  ([Understanding 1.2.9, key terms](https://www.w3.org/WAI/WCAG22/Understanding/audio-only-live.html)).
- **Live audio following a script:** at AAA, an accurate script available during
  the event can be an alternative; significant deviations leave it inadequate.
  A live text service can follow deviations and meaningful sounds
  ([Understanding 1.2.9](https://www.w3.org/WAI/WCAG22/Understanding/audio-only-live.html)).

At AAA, primarily spoken prerecorded audio-only also has SC 1.4.7 requirements:
no background audio, an option to turn it off, or background at least 20 dB below
foreground speech (apart from occasional sounds lasting one or two seconds).
Its scope excludes audio CAPTCHAs/logos and primarily musical vocalization
([Understanding 1.4.7](https://www.w3.org/WAI/WCAG22/Understanding/low-or-no-background-audio.html)).

For live video, description and an accessible separate text stream may still be
needed by users although 1.2 does not mandate them at these levels. Offer them
as user-needs recommendations and distinguish them from the table's normative
requirements ([WAI transcripts](https://www.w3.org/WAI/media/av/transcripts/)).
