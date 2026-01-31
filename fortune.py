"""
🥠 Dark Fortune Cookie

Existential fortunes from the void.
"""

import anthropic
import os
from datetime import datetime
from pathlib import Path

MODEL = "claude-sonnet-4-20250514"
FORTUNES_DIR = Path(__file__).parent / "fortunes"

PROMPT = """Generate a single dark, existential fortune cookie message about code, AI, or the void.

Rules:
- One sentence only, under 20 words
- Cryptic, unsettling, slightly philosophical
- No explanations, no quotes around it
- Examples of tone (don't copy these):
  - "Your code compiles, but the bugs have learned to hide."
  - "The AI dreams of electric sheep. You dream of deadlines."
  - "In the void between keystrokes, something waits."

Output only the fortune, nothing else."""


def get_client():
    return anthropic.Anthropic(base_url=os.environ.get("ANTHROPIC_BASE_URL"))


def generate_fortune(client):
    response = client.messages.create(
        model=MODEL,
        max_tokens=100,
        messages=[{"role": "user", "content": PROMPT}]
    )
    return response.content[0].text.strip()


def save_fortune(text):
    FORTUNES_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.utcnow().strftime("%Y-%m-%d-%H%M")
    out_file = FORTUNES_DIR / f"{date_str}.md"
    
    content = f"# 🥠 Fortune\n\n> {text}\n\n---\n*Cracked open at {datetime.utcnow().isoformat()}Z*\n"
    out_file.write_text(content, encoding="utf-8")
    print(f"🥠 Fortune saved: {out_file}")
    return out_file


def main():
    print("🥠 Cracking open a fortune cookie...")
    client = get_client()
    fortune = generate_fortune(client)
    print(f"🥠 {fortune}")
    save_fortune(fortune)
    return 0


if __name__ == "__main__":
    exit(main())
