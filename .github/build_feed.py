#!/usr/bin/env python3
"""Regenerate feed.json from episodes/*.mp3 (latest episode wins).

Runs inside the GitHub Action after papa's agent pushes a new mp3 named
YYYY-MM-DD.mp3. Writes a single-item Amazon Flash Briefing JSON feed
pointing to the newest episode on GitHub Pages.
"""
import datetime, glob, json, os, uuid

BASE = "https://denizagent29.github.io"
FILES = [f for f in glob.glob("episodes/*.mp3") if os.path.basename(f)[:10].replace("-", "").isdigit()]

if not FILES:
    if os.path.exists("feed.json"):
        os.remove("feed.json")
        print("no episodes — removed stale feed.json")
    else:
        print("no episodes yet — no feed.json")
    raise SystemExit(0)

latest = max(FILES, key=lambda f: os.path.basename(f)[:10])
name = os.path.basename(latest)          # e.g. 2026-09-05.mp3
date = name[:10]                         # e.g. 2026-09-05
stream_url = f"{BASE}/episodes/{name}"

feed = {
    "uid": "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, stream_url)),
    "updateDate": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "titleText": f"Günlük haber bülteni — {date}",
    "mainText": "",
    "streamUrl": stream_url,
    "redirectionUrl": f"{BASE}/",
}

with open("feed.json", "w", encoding="utf-8") as f:
    json.dump(feed, f, ensure_ascii=False, indent=2)
print("feed.json ->", stream_url)
