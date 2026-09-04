# Personal daily audio digest — GitHub Pages feed

Private-use repository: papa's agent publishes one mp3 per day here
(`episodes/YYYY-MM-DD.mp3`). A GitHub Action regenerates `feed.json`
(Amazon Flash Briefing format) pointing at the newest episode, which an
Amazon Echo plays on schedule via a Flash Briefing skill.

## Adding an episode (papa's agent)

Commit/push a file named `episodes/YYYY-MM-DD.mp3` (date = Turkish local
day of the episode, e.g. `episodes/2026-09-05.mp3`). Requirements for Alexa:

- MP3, ≥256 kbps, mono or stereo
- 10 seconds to 10 minutes long
- HTTPS URL is automatic (this Pages site)

The workflow builds `feed.json` and pushes it back within a minute.
Site URL: https://denizagent29.github.io — feed at /feed.json
