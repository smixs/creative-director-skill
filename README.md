# 🎬 Creative Director Skill

[![Claude Skill](https://img.shields.io/badge/Claude-Skill-blueviolet?style=flat-square)](https://docs.anthropic.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Methods 20+](https://img.shields.io/badge/Methods-20%2B-orange?style=flat-square)](#methodologies-20)
[![Case Library](https://img.shields.io/badge/Cases-571-blue?style=flat-square)](#case-library)
[![Version](https://img.shields.io/badge/Version-2.0-red?style=flat-square)](#whats-new-in-v20)

**🇷🇺 [Читать на русском](README.ru.md)**

> Created in collaboration with **Paul Deadcough**.

An AI creative director that generates advertising concepts using world-class methodologies, scores them against Cannes/D&AD-calibrated criteria, recursively refines until the quality threshold is reached, and **calibrates every idea against a library of 571 legendary campaigns** to detect saturation and ensure originality.

Not a brainstorming toy. A structured creative process that mirrors how top agencies (Droga5, Wieden+Kennedy, Mother) actually work — insight before ideas, methodology over free association, honest evaluation over flattery, **calibration against the canon** over invention from zero.

---

## What's New in v2.0

- **571-case library** with full Insight / Mechanic / Why-it-worked / Steal structure on every card
- **17-axis frontmatter schema** — every card tagged across pattern (P01-P18), industry, format, emotion (Tier 1/2/3), budget, idea_type (Pollard 7-level), awards, and more
- **6 MOCs** (Maps of Content) for fast lookup by pattern, emotion, format, industry, budget, and chronological index
- **4-point case library integration** in workflow — priming before generation, originality empirical cap, RESTART case-soaking, pattern calibration before exit
- **3 maintenance scripts** (Python via `uv`) — schema validation, MOC generation, graph wikilinks
- **Pollard 7-level idea taxonomy** replacing the previous 3-level system
- **3-tier emotion hierarchy** with 30+ specific emotion values
- **Activation toolkit** with 9 formats and the Non-advertising vs Execution test
- **Pre-Mortem template** before final delivery

Quality reviewed via [`skill-conductor`](https://github.com/smixs/skill-conductor): **41/50 production-grade** (Discovery 7/10, Clarity 9/10, Efficiency 7/10, Robustness 8/10, Completeness 10/10).

---

## What It Does

Feed it a brief in any format — text, voice transcript, PDF, raw notes — and it runs a full creative cycle:

1. **INTAKE** — extracts the brief's DNA: product, audience, objectives, constraints + classifies the required idea level using Pollard 7-level taxonomy (business / brand / tagline / advertising / campaign / non_advertising / execution)
2. **INSIGHT** — mines consumer insights using 7 proven techniques (Mark Pollard, JTBD, Tension Spotting, HMW, Abstraction Laddering)
3. **IDEATION** — primes against the canon (scans 5-7 cases from the relevant MOC), then generates 8-12 ideas using 3 methods from different categories (structural × associative × disruptive), rotating between 20+ methodologies, with a Tension test on each
4. **EVALUATE + REFINE** — scores against 6 weighted criteria + HumanKind + Grey Scale, then recursively improves; **Originality is capped empirically** by case-library saturation (3+ canonical cases of the same mechanic → cap at 7); when stuck, RESTARTs through case-soaking (read 8-12 canonical cards, remix allowed); Pattern Calibration + Pre-Mortem before exit
5. **ARTICULATE** — outputs in a presentation-ready format (one-pager, top-3, campaign platform, or quick response)

You can also enter at any phase: jump to insight mining, evaluate an existing idea, or generate concepts from a known insight.

## Why This Exists

Most AI "creative" tools generate ideas by free association — producing volume without structure. The result: hundreds of mediocre concepts that nobody can evaluate, often unknowingly recycling work that already exists.

This skill enforces the discipline that separates award-winning work from filler:

- **Insight-first** — no ideation without a validated consumer tension
- **Structural methods** — SIT, TRIZ, SCAMPER, Bisociation, Synectics, not "give me 10 ideas"
- **Empirical originality** — every idea is checked against 571 real campaigns; if 3+ canonical cases use the same mechanic, originality is capped, not subjectively claimed
- **Honest scoring** — calibrated against real Cannes winners, with anti-inflation rules
- **Recursive refinement** — weak criteria get targeted improvement using different methods each pass
- **Case-soaking on plateau** — when ideas plateau, the skill reads 8-12 canonical cards to re-train its sense for what a strong insight feels like; combining/remixing existing patterns is explicitly allowed (this is how Cannes-grade work is built)
- **Kill Your Darlings** — the skill argues against its own favorite ideas to test their strength
- **Pre-Mortem** — before delivery, simulates failure and surfaces the most likely failure modes

## What's Inside

```
creative-director/
├── SKILL.md                                  # Core skill — phase router + 5-phase workflow
├── assets/
│   └── output-templates.md                   # 4 presentation formats
├── scripts/                                  # Python via uv (PEP 723 inline deps)
│   ├── validate_schema.py                    # Frontmatter validation against tag-schema
│   ├── generate_mocs.py                      # Builds 6 MOCs from cards
│   └── generate_links.py                     # Adds Related sections (idempotent)
└── references/
    ├── tag-schema.md                         # Single source of truth — 17-axis frontmatter contract
    ├── idea-taxonomy.md                      # Pollard 7-level taxonomy
    ├── emotion-hierarchy.md                  # Tier 1/2/3 + 30+ specific emotion values
    ├── activation-toolkit.md                 # 9 activation formats + Non-ad vs Execution test
    ├── legendary-patterns.md                 # P01-P18 mechanics + Pre-Mortem template
    ├── methods-catalog.md                    # 20 creative methodologies as executable cards
    ├── method-selection-matrix.md            # Task → method routing + rotation rules
    ├── insight-mining.md                     # 7 insight discovery techniques
    ├── scoring-calibration.md                # Detailed rubrics + calibration anchors
    ├── creative-constitution.md              # 3-layer evaluation system + feedback rules
    ├── storytelling-frameworks.md            # 6 narrative frameworks for advertising
    └── legendary-campaigns/                  # 571-case library
        ├── README.md                         # Library guide
        ├── MOC-index.md                      # All 571 cards by year DESC
        ├── MOC-pattern.md                    # Grouped by P01–P18 (18 mechanics)
        ├── MOC-emotion.md                    # Grouped by emotion_tier (3 → 2 → 1)
        ├── MOC-format.md                     # Grouped by category (film/integrated/stunt_pr/...)
        ├── MOC-industry.md                   # Grouped by industry vertical
        ├── MOC-budget.md                     # Grouped by budget (low/medium/high)
        └── cards/                            # 571 individual cards (flat namespace)
            └── {id}.md
```

## Case Library

571 advertising campaigns from 1950–2025, tagged across **17 axes**, with full structural analysis on every card.

### Card structure

Each card has YAML frontmatter (17 axes — see `references/tag-schema.md`) + 4 sections:

- **Insight** — the human truth the campaign exploits (one sentence)
- **Mechanic** — what was actually executed
- **Why it worked** — psychological / cultural / structural reason
- **Steal** — pattern-level borrow strategy
- **Related** — auto-generated wikilinks (pattern hub + 2 sibling cards + emotion match)

### Tag schema (17 axes)

`id`, `title`, `brand`, `agency`, `year`, `country`, `region`, `industry`, `pattern[]` (P01–P18), `category`, `idea_type` (Pollard 7-level), `involvement`, `channel`, `duration`, `goal[]`, `budget`, `emotion[]`, `emotion_tier` (1/2/3), `insight_domain`, `media_epoch`, `awards[]`, `quality_score` (HumanKind 1–10), `scalability`, `risk`.

### 18 patterns (P01–P18)

Format as Idea · Enemy or Conflict · Behavior Inversion · Brand as Activist · Cultural Hijack · Limitation as Power · Invisible Brand · Craft as Message · User as Co-Author · Serialization & Ritual · Absurd as Carrier · Social Experiment · Truth Telling · Product as Proof · Benefit Hyperbole · Long-form Drama · Design as Idea · Tech as Canvas

### Lookup strategies

```bash
# Browse by axis — open the matching MOC
# Each line has inline-context (brand · year · format · emotion · budget · top_award)

# Filter by combination — ripgrep on frontmatter
rg -l "^budget: low$" cards/ | xargs rg -l "^emotion_tier: 3$"

# All P11 cases since 2020
rg -l "P11" cards/ | xargs rg -l "^year: 202"

# All canonical cases for QSR
rg -l "^industry: qsr$" cards/ | xargs rg -l "^quality: canonical$"
```

### Saturation map (originality pressure)

| Pattern | Saturation | Originality cap |
|---------|-----------|----------------|
| P11 (Absurd as Carrier), P16 (Long-form Drama), P09 (User as Co-Author) | high (>50 cases) | ≤6 unless structurally new variant |
| P02, P10, P12, P14, P18 | medium | ≤7 if 3+ canonical use same mechanic |
| P01, P15 | low | room for novelty |

This is empirical saturation, not subjective novelty.

## Methodologies (20+)

| Category | Methods |
|----------|---------|
| **Structural** | SIT/Goldenberg Templates, SCAMPER, TRIZ (10 principles), Morphological Analysis |
| **Association** | Bisociation, Random Entry, Forced Connections, Synectics |
| **Inversion** | Reverse Brainstorming, Worst Possible Idea, Provocation PO |
| **Perturbation** | Oblique Strategies, Six Thinking Hats, Disney Creative Strategy |
| **Volume** | Crazy 8s, Brainwriting 6-3-5, Starbursting |
| **Bonus** | First Principles Thinking, Lateral Thinking Toolkit, Design Sprint Sketch |

## Evaluation System

Three parallel scoring systems calibrated against real campaigns:

- **6 Weighted Criteria** — Originality (0.25, empirically capped by case library), Strategic Fit (0.20), Emotional Response (0.20, Tier 1/2/3 hierarchy), Feasibility (0.15), Scalability (0.10), Simplicity (0.10)
- **HumanKind Scale** (Leo Burnett) — 1-10, from "Destructive" to "Changes the World"
- **Grey Scale** (Grey Group) — 1-10, from "Toxic" to "Best in the World"

Anti-inflation rules: batch control, normal distribution enforcement, real analogues test, specificity test, time test, **empirical saturation cap from case library**.

## Idea Taxonomy (Pollard 7-level)

| Level | When required | Lifespan |
|-------|---------------|----------|
| `business` | new venture, repositioning the entire company | years |
| `brand` | rebranding, brand platform — "what does the brand stand for?" | 5–10+ years |
| `tagline` | short phrase that crystallizes brand idea | 5–10+ years |
| `advertising` | central thought across all comms — recognizable without logo | 3–5 years |
| `campaign` | seasonal campaign, product launch, promo | 3–12 months |
| `non_advertising` | activation/utility/cultural object that lives without ads | varies |
| `execution` | one-off channel/format/mechanic | days–weeks |

**Activation diagnostic:** if brief mentions activation/stunt/utility — apply the test "remove the campaign, does it still have meaning?" → Yes = `non_advertising` / No = `execution`.

## Emotion Hierarchy (Tier 1/2/3)

- **Tier 1 (forgettable):** happy, sad, angry, afraid → score ≤ 6
- **Tier 2 (memorable):** nostalgic, defiant, proud, ironic, etc. → score 6–8
- **Tier 3 (greatness):** bittersweet pride, ironic sincerity, vulnerable defiance, etc. → score 8–10
- **Score 9+ requires Tier 3.**

## How Recursion Works

```
Generate ideas (3 methods, 8-12 ideas, primed against canon)
        ↓
Tension test on each idea
        ↓
Score top 3 (6 criteria + HumanKind + Grey, originality capped by saturation)
        ↓
    Score ≥ 9? ──→ YES → Pattern Calibration + Pre-Mortem → Output
        ↓ NO
Identify weak criteria → Apply different method → Rescore
        ↓
    Plateau? ──→ YES → RESTART via case-soaking
        ↓             (read 8-12 canonical cards, remix allowed)
        ↓ NO
    Continue refinement
        ↓
    5 passes? ──→ YES → Output best + honest assessment
```

## Storytelling Frameworks

Story Spine (Pixar) · Sparkline (Nancy Duarte) · Freytag's Pyramid · Monroe's Motivated Sequence · Pixar Rules · Hero's Journey (StoryBrand)

## Installation

### Claude Code (recommended)

```bash
git clone https://github.com/smixs/creative-director-skill.git
cp -r creative-director-skill/creative-director ~/.claude/skills/
```

After installation, restart Claude Code session (`/clear` or new session) to pick up the skill.

### Claude Projects

Add the files to your Claude Project's knowledge base. Upload all files from `creative-director/` — `SKILL.md` is the entry point, it references other files via `[[wikilinks]]`.

### Other AI Agents (Cursor, Windsurf, GPT, Gemini)

The skill works with any AI agent that supports structured instructions — the core logic is in markdown files, no platform lock-in. Copy the `creative-director/` folder to your project or skills directory.

## Maintenance Scripts

Three Python scripts (run via `uv run`, PEP 723 inline deps — no manual setup):

```bash
cd creative-director
uv run scripts/validate_schema.py        # Validate all card frontmatter
uv run scripts/generate_mocs.py          # Rebuild 6 MOCs from cards
uv run scripts/generate_links.py         # Rebuild Related sections (idempotent)
```

Run pipeline: edit/add cards → validate → regenerate MOCs → regenerate links.

## Usage Examples

**Full creative cycle:**
> "Come up with a campaign for [brand]. Target audience: [who]. Budget: [range]. Channels: [where]."

**Insight mining:**
> "Find a consumer insight for [category]. The brief says [context]."

**Evaluate an existing idea:**
> "Evaluate this concept: [description]. The brief objective was [goal]."

**Activation / non-advertising:**
> "Need a PR-stunt for [brand]. Low budget, must drive earned media in a week. Not a campaign — a one-shot activation."

**Quick ideation:**
> "Need 5 concepts for [brand] social media posts about [topic]."

## What It's Not For

- Media planning or budget allocation
- Production management
- Brand identity / logo design
- Final copywriting (it generates concepts, not polished copy)
- Market research data collection
- Brand positioning warmaps (use a dedicated positioning skill)

## Limitations & Honest Notes

- **Auto-trigger in `claude -p` mode is unreliable.** This is an advisory skill — when invoked through one-shot CLI, the model often answers creative briefs directly without consulting it. For consistent behavior in interactive sessions, invoke explicitly or share a detailed brief (>500 chars with structure).
- **571 source URLs are unverified.** Library was built from public award-show indexes; verify links manually before citing in client work.
- **12 cards have `confidence: low`** with `verification_required: true` — these should be cross-checked against external sources. The skill prefers `quality: canonical` cards for calibration.
- **Library is static.** New campaigns from 2026+ are not auto-added; periodic manual extension required.

## Credits

Created in collaboration with **Paul Deadcough**.

Built on methodologies from: Jacob Goldenberg (SIT), Genrich Altshuller (TRIZ), Edward de Bono (Lateral Thinking, Six Hats, PO), Arthur Koestler (Bisociation), William Gordon (Synectics), Brian Eno (Oblique Strategies), Nancy Duarte (Sparkline), Joseph Campbell / Donald Miller (Hero's Journey / StoryBrand), Leo Burnett (HumanKind), Mark Pollard (Strategy + 7-level Taxonomy), Clayton Christensen (JTBD).

Creative Constitution based on the Voskresensky/IKRA approach.

Case library curated from D&AD, Cannes Lions, One Show, Webby, and Effie shortlists 1950–2025.

## License

MIT — use it, fork it, make better ads.
