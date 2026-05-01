# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///

"""Validate frontmatter cards against tag-schema.md."""

import argparse
import re
import sys
from pathlib import Path
import yaml

SKILL_ROOT = Path(__file__).parent.parent
SCHEMA_PATH = SKILL_ROOT / "references" / "tag-schema.md"
CARDS_DIR = SKILL_ROOT / "references" / "legendary-campaigns" / "cards"

REQUIRED_FIELDS = [
    "id", "title", "brand", "year", "country", "region", "industry",
    "pattern", "category", "idea_type", "involvement", "channel", "duration",
    "goal", "budget", "emotion", "emotion_tier", "insight_domain",
    "media_epoch", "awards", "quality_score", "scalability", "risk",
]

# Cardinality: field -> (min, max) for list fields
CARDINALITY: dict[str, tuple[int, int]] = {
    "pattern": (1, 3),
    "goal": (1, 4),
    "emotion": (1, 4),
    "awards": (0, 4),
}

# Fields that are free-form strings or validated by other means
SKIP_ENUM: set[str] = {"id", "title", "brand", "agency", "source_url", "emotion"}

# Optional/meta fields and their expected types
OPTIONAL_TYPES: dict[str, type] = {
    "agency": str,
    "confidence": str,
    "verification_required": bool,
    "quality": str,
    "source_url": str,
}

OPTIONAL_ENUMS: dict[str, set[str]] = {
    "confidence": {"high", "medium", "low"},
    "quality": {"canonical", "full", "stub_enriched", "stub_minimal"},
}

ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*-\d{4}(?:-\d+)?$")


def parse_schema(schema_path: Path) -> dict[str, set[str]]:
    """Parse tag-schema.md and return field -> set of allowed enum values."""
    text = schema_path.read_text(encoding="utf-8")
    schema: dict[str, set[str]] = {}

    # country: any 2-letter uppercase ISO code + Global + unknown
    schema["country"] = {f"{a}{b}" for a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for b in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    schema["country"].update({"Global", "unknown"})

    # region: bullet list
    region_match = re.search(
        r"### `region`\n((?:- `?\w+`?\n?)+)", text
    )
    if region_match:
        schema["region"] = set(re.findall(r"- `?(\w+)`?", region_match.group(1)))

    # industry: bullet list (strip parenthetical notes)
    industry_match = re.search(
        r"### `industry`\n((?:- `?[\w_]+`?.*\n?)+)", text
    )
    if industry_match:
        schema["industry"] = set(
            re.findall(r"- `?([\w_]+)`?", industry_match.group(1))
        )

    # pattern: P01-P18 bullets
    pattern_match = re.search(
        r"### `pattern`.*?\n((?:- `?(P\d{2})`?.*\n?)+)", text
    )
    if pattern_match:
        schema["pattern"] = set(re.findall(r"(P\d{2})", pattern_match.group(1)))

    # Simple single-word bullet enums
    simple_fields = [
        "category", "idea_type", "involvement", "channel", "duration",
        "goal", "budget", "insight_domain", "media_epoch", "scalability", "risk",
    ]
    for field in simple_fields:
        m = re.search(
            rf"### `{field}`[^\n]*\n((?:- `?[\w_]+`?.*\n?)+)", text
        )
        if m:
            schema[field] = set(re.findall(r"- `?([\w_]+)`?", m.group(1)))

    # awards: multi-word slugs
    awards_match = re.search(
        r"### `awards`\n((?:- `?[\w_]+`?.*\n?)+)", text
    )
    if awards_match:
        schema["awards"] = set(re.findall(r"- `?([\w_]+)`?", awards_match.group(1)))

    return schema


def validate_card(card_path: Path, schema: dict[str, set[str]]) -> list[str]:
    """Validate a single card's frontmatter. Returns list of error strings."""
    errors: list[str] = []
    text = card_path.read_text(encoding="utf-8")

    if not text.startswith("---"):
        errors.append("no frontmatter")
        return errors

    # Extract YAML block between first pair of ---
    parts = text.split("---", 2)
    if len(parts) < 3:
        errors.append("no frontmatter")
        return errors

    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:
        errors.append(f"yaml parse error: {exc}")
        return errors

    if not isinstance(fm, dict):
        errors.append("frontmatter is not a mapping")
        return errors

    # --- Required fields ---
    for field in REQUIRED_FIELDS:
        if field not in fm or fm[field] is None:
            errors.append(f"Missing required field: {field}")

    # --- year ---
    if "year" in fm and fm["year"] is not None:
        y = fm["year"]
        if not isinstance(y, int) or not (1950 <= y <= 2025):
            errors.append(f"Invalid `year`: {y!r} (must be int 1950–2025)")

    # --- quality_score ---
    if "quality_score" in fm and fm["quality_score"] is not None:
        qs = fm["quality_score"]
        if not isinstance(qs, int) or not (1 <= qs <= 10):
            errors.append(f"Invalid `quality_score`: {qs!r} (must be int 1–10)")

    # --- emotion_tier ---
    if "emotion_tier" in fm and fm["emotion_tier"] is not None:
        et = fm["emotion_tier"]
        if et not in (1, 2, 3):
            errors.append(f"Invalid `emotion_tier`: {et!r} (must be 1, 2, or 3)")

    # --- id format ---
    if "id" in fm and fm["id"] is not None:
        id_val = str(fm["id"])
        if not ID_RE.match(id_val):
            errors.append(
                f"Invalid `id` format: {id_val!r} "
                "(expected kebab-case ending with 4-digit year)"
            )

    # --- enum + cardinality validation ---
    for field, allowed in schema.items():
        if field in SKIP_ENUM or fm.get(field) is None:
            continue

        value = fm[field]
        card = CARDINALITY.get(field)

        if card is not None:
            # Expect a list
            if not isinstance(value, list):
                errors.append(
                    f"Field `{field}` must be a list, got {type(value).__name__}"
                )
                continue
            min_c, max_c = card
            if not (min_c <= len(value) <= max_c):
                errors.append(
                    f"Field `{field}` cardinality {len(value)} "
                    f"out of range [{min_c}–{max_c}]"
                )
            for v in value:
                if str(v) not in allowed:
                    errors.append(
                        f"Invalid value for `{field}`: {v!r} (not in allowed set)"
                    )
        else:
            # Expect a scalar
            if isinstance(value, list):
                errors.append(
                    f"Field `{field}` must be a single value, not a list"
                )
                continue
            if str(value) not in allowed:
                errors.append(
                    f"Invalid value for `{field}`: {value!r} (not in allowed set)"
                )

    # --- emotion: must be list of strings ---
    if "emotion" in fm and fm["emotion"] is not None:
        em = fm["emotion"]
        card = CARDINALITY["emotion"]
        if not isinstance(em, list):
            errors.append(f"Field `emotion` must be a list, got {type(em).__name__}")
        else:
            if not (card[0] <= len(em) <= card[1]):
                errors.append(
                    f"Field `emotion` cardinality {len(em)} out of range [1–4]"
                )
            for v in em:
                if not isinstance(v, str):
                    errors.append(f"Field `emotion` values must be strings, got {v!r}")

    # --- optional fields type/enum check ---
    for field, expected_type in OPTIONAL_TYPES.items():
        if field not in fm or fm[field] is None:
            continue
        val = fm[field]
        if not isinstance(val, expected_type):
            errors.append(
                f"Optional field `{field}`: expected {expected_type.__name__}, "
                f"got {type(val).__name__}"
            )
        if field in OPTIONAL_ENUMS and str(val) not in OPTIONAL_ENUMS[field]:
            errors.append(
                f"Invalid value for optional `{field}`: {val!r} "
                f"(allowed: {sorted(OPTIONAL_ENUMS[field])})"
            )

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate creative-director cards against tag-schema.md"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with code 1 if any errors are found",
    )
    args = parser.parse_args()

    schema = parse_schema(SCHEMA_PATH)

    cards = sorted(CARDS_DIR.glob("*.md"))
    total = len(cards)
    valid = 0
    errored = 0

    for i, card_path in enumerate(cards, 1):
        if i % 50 == 0 or i == total:
            print(f"Checked {i}/{total} cards...")

        errors = validate_card(card_path, schema)
        if errors:
            errored += 1
            print(f"[ERROR] cards/{card_path.name}", file=sys.stderr)
            for err in errors:
                print(f"  - {err}", file=sys.stderr)
        else:
            valid += 1

    summary = f"Validated {total} cards: {valid} valid, {errored} with errors"
    print(summary)

    if args.strict and errored > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
