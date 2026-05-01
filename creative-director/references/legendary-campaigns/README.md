# Legendary Campaigns Library

571 advertising campaigns from 1950–2025, tagged across 17 axes. Used by `creative-director` for pattern calibration, originality benchmarking, and case-based reasoning.

## Structure

```
legendary-campaigns/
├── README.md           ← you are here
├── MOC-index.md        ← all 571 cards by year DESC
├── MOC-pattern.md      ← grouped by P01–P18 (18 mechanics)
├── MOC-emotion.md      ← grouped by emotion_tier (3 → 2 → 1)
├── MOC-format.md       ← grouped by category (film/integrated/stunt_pr/...)
├── MOC-industry.md     ← grouped by industry vertical
├── MOC-budget.md       ← grouped by budget (low/medium/high)
└── cards/
    └── {id}.md         ← 571 individual cards (flat namespace)
```

## Card anatomy

Each card has YAML frontmatter (17 axes — see `../tag-schema.md`) + 4 sections:

- **Insight** — the human truth the campaign exploits (one sentence)
- **Mechanic** — what was actually executed
- **Why it worked** — psychological / cultural / structural reason
- **Steal** — pattern-level borrow strategy
- **Related** — auto-generated wikilinks (pattern hub + 2 sibling cards + emotion match)

## Lookup strategies

**Browse by axis** — open the matching MOC. Each line has inline-context (`brand · year · format · emotion · budget · top_award`) so you can scan without opening cards.

**Filter by combination** — use ripgrep on frontmatter:
```bash
# low-budget Tier-3 emotional campaigns:
rg -l "^budget: low$" cards/ | xargs rg -l "^emotion_tier: 3$"

# all P11 (Absurd as Carrier) cases since 2020:
rg -l "P11" cards/ | xargs rg -l "^year: 202"

# all canonical cases for QSR:
rg -l "^industry: qsr$" cards/ | xargs rg -l "^quality: canonical$"
```

**Pattern calibration** — for any new idea, find its closest pattern (P01–P18), open `MOC-pattern.md`, scan canonical examples in that group, articulate how your idea differs.

## Saturation map (originality pressure)

| Pattern | Cases | Saturation |
|---------|-------|-----------|
| P11 (Absurd as Carrier) | high | hardest to be original |
| P16 (Long-form Drama) | high | hardest to be original |
| P09 (User as Co-Author) | high | crowded |
| P15 (Benefit Hyperbole) | low | underused |
| P01 (Format as Idea) | low | room for novelty |

If your idea sits in a high-saturation pattern, originality cap = 7 unless you bring a structurally new variant.

## Confidence and quality

Each card has `confidence: high/medium/low` and `quality: canonical/full/stub_enriched/stub_minimal`:

- `canonical` — ★ in source list + full pattern-file content
- `full` — non-★ but well-documented from training knowledge
- `stub_enriched` — limited source detail, sections constructed from inference
- `stub_minimal` — `verification_required: true`, sections may have TODOs

Cards with `confidence: low` should be cross-checked against external sources before citing in client work.

## URL verification

⚠️ All `source_url` fields are unverified — proxy blocks egress during enrichment. Verify links manually before sharing.

## Regeneration

Three scripts maintain this library (run via `uv run` from skill root):

- `scripts/validate_schema.py` — checks every card against `tag-schema.md`
- `scripts/generate_mocs.py` — rebuilds 6 MOCs from current cards
- `scripts/generate_links.py` — rebuilds `## Related` sections (idempotent)

Pipeline: edit/add cards → validate → regenerate MOCs → regenerate links.
