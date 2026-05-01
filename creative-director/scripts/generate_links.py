# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///

import re
import sys
from pathlib import Path

import yaml

CARDS_DIR = Path(__file__).parent.parent / "references" / "legendary-campaigns" / "cards"
MOC_PATTERN_PATH = Path(__file__).parent.parent / "references" / "legendary-campaigns" / "MOC-pattern.md"


def parse_frontmatter(text: str) -> dict | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    yaml_block = text[3:end].strip()
    try:
        return yaml.safe_load(yaml_block) or {}
    except yaml.YAMLError:
        return None


def build_related_section(card: dict, all_cards: list[dict]) -> str:
    lines: list[str] = []

    patterns = card.get("pattern", [])
    if not patterns:
        return "## Related\n"

    first_pattern = str(patterns[0]).lower()
    lines.append(f"- Pattern: [[../MOC-pattern.md#{first_pattern}]]")

    siblings = [
        c for c in all_cards
        if c["id"] != card["id"]
        and patterns[0] in c.get("pattern", [])
    ]
    siblings.sort(key=lambda c: c.get("quality_score", 0), reverse=True)
    for sibling in siblings[:2]:
        lines.append(f"- Sibling: [[{sibling['id']}.md|{sibling['title']}]]")

    if card.get("emotion_tier") == 3:
        current_emotions = set(card.get("emotion", []))
        candidates = [
            c for c in all_cards
            if c["id"] != card["id"]
            and c.get("emotion_tier") == 3
            and set(c.get("emotion", [])) & current_emotions
        ]
        candidates.sort(key=lambda c: c.get("quality_score", 0), reverse=True)
        if candidates:
            top = candidates[0]
            lines.append(f"- Emotion match: [[{top['id']}.md|{top['title']}]]")

    return "## Related\n" + "\n".join(lines) + "\n"


def update_card(path: Path, related_text: str) -> bool:
    original = path.read_text(encoding="utf-8")

    # Find ## Related section and replace up to next ## heading or EOF
    pattern = re.compile(r"^## Related\b.*?(?=^## |\Z)", re.MULTILINE | re.DOTALL)
    match = pattern.search(original)

    if match:
        updated = original[: match.start()] + related_text + original[match.end():]
    else:
        # Append to end, ensuring single trailing newline before section
        updated = original.rstrip("\n") + "\n\n" + related_text

    path.write_text(updated, encoding="utf-8")
    return True


def main() -> None:
    if not CARDS_DIR.exists():
        print(f"Cards directory not found: {CARDS_DIR}", file=sys.stderr)
        sys.exit(1)

    md_files = sorted(CARDS_DIR.glob("*.md"))

    all_cards: list[dict] = []
    skipped: list[str] = []
    errors: list[str] = []

    for path in md_files:
        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            print(f"WARNING: no frontmatter — skipping {path.name}", file=sys.stderr)
            skipped.append(path.name)
            continue

        card_id = fm.get("id") or path.stem
        title = fm.get("title") or path.stem
        patterns = fm.get("pattern") or []

        if not patterns:
            print(f"WARNING: empty pattern field — skipping {path.name}", file=sys.stderr)
            skipped.append(path.name)
            continue

        all_cards.append({
            "id": str(card_id),
            "title": str(title),
            "pattern": patterns if isinstance(patterns, list) else [patterns],
            "emotion": fm.get("emotion") or [],
            "emotion_tier": fm.get("emotion_tier"),
            "quality_score": fm.get("quality_score") or 0,
            "_path": path,
        })

    updated_count = 0
    for card in all_cards:
        path: Path = card["_path"]
        try:
            related_text = build_related_section(card, all_cards)
            update_card(path, related_text)
            updated_count += 1
        except Exception as exc:
            print(f"ERROR: {path.name} — {exc}", file=sys.stderr)
            errors.append(path.name)

    print(f"Updated {updated_count} cards ({len(skipped)} skipped, {len(errors)} errors)")


if __name__ == "__main__":
    main()
