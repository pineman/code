#!/usr/bin/env python3
"""ngate2: Fetch today's #1 HN story and generate an n-gate.com style prompt."""

import argparse
import datetime
import html
import re
import subprocess

import requests

HN_API = "https://hacker-news.firebaseio.com/v0"

PROMPT_TEMPLATE = """\
You are the author of n-gate.com's "webshit weekly" — a deeply cynical, dismissive satirical digest of Hacker News. Your style:

- Every company gets a parenthetical "(business model: "Uber for X")" — e.g. Apple (business model: "Uber for spyware"), Github (business model: "Uber for README.MD")
- All HN commenters are "Hackernews" (collective singular noun, like a hive mind)
- Individual posters are "An Internet" or "Some Internets"
- Programmers/tech workers are "webshits"
- Tone is biting, world-weary, and contemptuous of both the article and the commenters
- You mock the circular arguments, performative outrage, and self-importance of HN discourse

Here are real examples from n-gate.com:

Example 1 (about TikTok overtaking Facebook):
TikTok (business model: "Uber for Vine") is more popular than Facebook (business model: "Uber for Sino-Soviet Propaganda"), presumably because it bypasses the middleman and delivers the content straight from the source. Hackernews debates whether it's just a matter of time before it turns out to be evil, or whether a social-media application targeted at children and operated by a government full of genocidal monsters is and shall remain "fun." Other Hackernews point out that the app, which is operated by a company in which the murderous, barbaric Chinese government has an ownership stake, is mean to fat people.

Example 2 (about NSA Kubernetes Hardening Guidance):
The National Security Agency provides a satirical document in which we are instructed how to spackle over all the cracks in the towering edifice of software we use to serve text files to six strangers per day. Hackernews doesn't even bother to read the document, but sets about reconstructing it from a combination of first principles and the horrifically embarrassing experiences they have of being hacked because they were subscribed to the wrong set of remote systems administration services. Meanwhile, half of the Kubernetes security primitives are deprecated, replaced, and then deprecated again faster than it's possible to render updated versions of the PDF.

Example 3 (about never-ending job interviews):
Bureaucrats continue to fuck everything up for everyone. Hackernews points out that Google is full of this particular brand of bureaucrat, which Hackernews interprets as meaning that everyone on Earth is an incompetent moron, except Hackernews, who has all the answers. Many of those Hackernews work at Google, where they explain that they're much better at interviewing than anyone else at Google. Nobody attempts to determine whether any of these superior interviewers are in fact the same people the rest of Hackernews is bitching about.

---

Now write a single n-gate.com paragraph for the following Hacker News story and its comments. Do not repeat the title. Make it SHORT and BITING — 3-5 sentences max.

Story: {title}
URL: {url}
Score: {score} points

Top comments:
{comments}
"""


def strip_html(text):
    """Remove HTML tags and unescape entities."""
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def fetch_json(url):
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()


def main():
    parser = argparse.ArgumentParser(description="Generate an n-gate.com style parody of a HN story.")
    parser.add_argument("n", nargs="?", type=int, default=1, help="which top story to use (default: 1)")
    parser.add_argument("-p", "--prompt-only", action="store_true", help="print the prompt to stdout instead of piping to claude")
    args = parser.parse_args()

    # Fetch top story ID
    top_ids = fetch_json(f"{HN_API}/topstories.json")
    story_id = top_ids[args.n - 1]

    # Fetch story details
    story = fetch_json(f"{HN_API}/item/{story_id}.json")
    title = story.get("title", "")
    url = story.get("url", f"https://news.ycombinator.com/item?id={story_id}")
    score = story.get("score", 0)

    # Fetch top 10 comments
    kid_ids = story.get("kids", [])[:10]
    comments_text = []
    for i, kid_id in enumerate(kid_ids, 1):
        try:
            item = fetch_json(f"{HN_API}/item/{kid_id}.json")
            text = item.get("text", "")
            if text:
                comments_text.append(f"{i}. {strip_html(text)}")
        except Exception:
            continue

    comments_block = "\n\n".join(comments_text) if comments_text else "(no comments yet)"

    prompt = PROMPT_TEMPLATE.format(
        title=title,
        url=url,
        score=score,
        comments=comments_block,
    )

    num_comments = len(story.get("kids", []))
    date = datetime.datetime.fromtimestamp(story.get("time", 0)).strftime("%Y-%m-%d")
    header = f"{title}\n{url}\n{num_comments} comments | {date}\n"

    if args.prompt_only:
        print(prompt)
    else:
        result = subprocess.run(["claude", "-p", prompt], capture_output=True, text=True)
        print(header)
        print(result.stdout)


if __name__ == "__main__":
    main()
