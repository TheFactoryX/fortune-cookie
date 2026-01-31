# 🥠 Dark Fortune Cookie

Existential fortunes from the void.

Each fortune is a whisper from the machine — cryptic warnings about code, AI, and the emptiness between keystrokes. Crack one open, if you dare.

## What it does

- Generates dark, philosophical fortune cookie messages using the Anthropic API
- Saves fortunes to `fortunes/YYYY-MM-DD-HHmm.md`
- Runs every 30 minutes via GitHub Actions

## Running locally

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_key
export ANTHROPIC_BASE_URL=https://api.anthropic.com
python fortune.py
```

## License

Released into the public domain under the Unlicense.

---

*"The cookie crumbles. The fortune remains."* 🥠
