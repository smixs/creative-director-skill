# 🎬 Creative Director Skill

[![Claude Skill](https://img.shields.io/badge/Claude-Skill-blueviolet?style=flat-square)](https://docs.anthropic.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![20+ Methods](https://img.shields.io/badge/Methods-20%2B-orange?style=flat-square)](#methodologies-20)

**🇷🇺 [Читать на русском](README.ru.md)**

An AI creative director that generates advertising concepts using world-class methodologies, scores them against Cannes/D&AD-calibrated criteria, and recursively refines until the quality threshold is reached.

Not a brainstorming toy. A structured creative process that mirrors how top agencies (Droga5, Wieden+Kennedy, Mother) actually work — insight before ideas, methodology over free association, honest evaluation over flattery.

---

## What It Does

Feed it a brief in any format — text, voice transcript, PDF, raw notes — and it runs a full creative cycle:

1. **INTAKE** — extracts the brief's DNA: product, audience, objectives, constraints
2. **INSIGHT** — mines consumer insights using 7 proven techniques (Mark Pollard, JTBD, Tension Spotting, HMW, Abstraction Laddering)
3. **IDEATION** — generates 8-12 ideas using 3 methods from different categories (structural × associative × disruptive), rotating between 20+ methodologies
4. **EVALUATE + REFINE** — scores against 6 weighted criteria + HumanKind + Grey Scale, then recursively improves until 9+ or convergence
5. **ARTICULATE** — outputs in a presentation-ready format (one-pager, top-3, campaign platform, or quick response)

You can also enter at any phase: jump to insight mining, evaluate an existing idea, or generate concepts from a known insight.

## Why This Exists

Most AI "creative" tools generate ideas by free association — producing volume without structure. The result: hundreds of mediocre concepts that nobody can evaluate.

This skill enforces the discipline that separates award-winning work from filler:

- **Insight-first** — no ideation without a validated consumer tension
- **Structural methods** — SIT, TRIZ, SCAMPER, Bisociation, Synectics, not "give me 10 ideas"
- **Honest scoring** — calibrated against real Cannes winners, with anti-inflation rules that prevent the model from rating everything 8+
- **Recursive refinement** — weak criteria get targeted improvement using different methods each pass
- **Kill Your Darlings** — the skill argues against its own favorite ideas to test their strength

## What's Inside

```
creative-director/
├── SKILL.md                              # Core skill — phase router + instructions
├── assets/
│   └── output-templates.md               # 4 presentation formats
└── references/
    ├── methods-catalog.md                # 20 creative methodologies as executable cards
    ├── method-selection-matrix.md        # Task → method routing + rotation rules
    ├── insight-mining.md                 # 7 insight discovery techniques
    ├── scoring-calibration.md            # Detailed rubrics + calibration anchors
    ├── creative-constitution.md          # 3-layer evaluation system + feedback rules
    └── storytelling-frameworks.md        # 6 narrative frameworks for advertising
```

### Methodologies (20+)

| Category | Methods |
|----------|---------|
| **Structural** | SIT/Goldenberg Templates, SCAMPER, TRIZ (10 principles), Morphological Analysis |
| **Association** | Bisociation, Random Entry, Forced Connections, Synectics |
| **Inversion** | Reverse Brainstorming, Worst Possible Idea, Provocation PO |
| **Perturbation** | Oblique Strategies, Six Thinking Hats, Disney Creative Strategy |
| **Volume** | Crazy 8s, Brainwriting 6-3-5, Starbursting |
| **Bonus** | First Principles Thinking, Lateral Thinking Toolkit, Design Sprint Sketch |

### Evaluation System

Three parallel scoring systems calibrated against real campaigns:

- **6 Weighted Criteria** — Originality (0.25), Strategic Fit (0.20), Emotional Response (0.20), Feasibility (0.15), Scalability (0.10), Simplicity (0.10)
- **HumanKind Scale** (Leo Burnett) — 1-10, from "Destructive" to "Changes the World"
- **Grey Scale** (Grey Group) — 1-10, from "Toxic" to "Best in the World"

Anti-inflation rules: batch control, normal distribution enforcement, real analogues test, specificity test, time test.

### Storytelling Frameworks

Story Spine (Pixar) · Sparkline (Nancy Duarte) · Freytag's Pyramid · Monroe's Motivated Sequence · Pixar Rules · Hero's Journey (StoryBrand)

## Installation

### Claude Projects

Add the files to your Claude Project's knowledge base. Upload all files from `creative-director/` — `SKILL.md` is the entry point, it references other files via `[[wikilinks]]`.

### Claude Code / Cursor / Windsurf / Any AI Agent

Copy the `creative-director/` folder to your project or skills directory:

```bash
git clone https://github.com/smixs/creative-director-skill.git
```

The skill works with any AI agent that supports structured instructions — Claude, GPT, Gemini, or local models. The core logic is in markdown files, no platform lock-in.

## Usage Examples

**Full creative cycle:**
> "Come up with a campaign for [brand]. Target audience: [who]. Budget: [range]. Channels: [where]."

**Insight mining:**
> "Find a consumer insight for [category]. The brief says [context]."

**Evaluate an existing idea:**
> "Evaluate this concept: [description]. The brief objective was [goal]."

**Quick ideation:**
> "Need 5 concepts for [brand] social media posts about [topic]."

## Idea Levels

The skill distinguishes between three levels and matches output to the brief:

| Level | Scope | Example |
|-------|-------|---------|
| **Big Idea** | Brand platform for years | Nike "Just Do It", Dove "Real Beauty" |
| **Campaign Idea** | Time-limited, multi-channel | "Share a Coke", Spotify Wrapped |
| **Execution Idea** | Single channel/format | A specific social post, banner, activation |

A Big Idea for shelf talkers = waste. An Execution Idea for a rebrand = falling short.

## How Recursion Works

```
Generate ideas (3 methods, 8-12 ideas)
        ↓
Score top 3 (6 criteria + HumanKind + Grey)
        ↓
    Score ≥ 9? ──→ YES → Output final deliverable
        ↓ NO
Identify weak criteria → Apply different method → Rescore
        ↓
    5 passes or plateau? ──→ YES → Output best + honest assessment
        ↓ NO
    Continue refinement
```

## What It's Not For

- Media planning or budget allocation
- Production management
- Brand identity / logo design
- Final copywriting (it generates concepts, not polished copy)
- Market research data collection

## Credits

Built on methodologies from: Jacob Goldenberg (SIT), Genrich Altshuller (TRIZ), Edward de Bono (Lateral Thinking, Six Hats, PO), Arthur Koestler (Bisociation), William Gordon (Synectics), Brian Eno (Oblique Strategies), Nancy Duarte (Sparkline), Joseph Campbell / Donald Miller (Hero's Journey / StoryBrand), Leo Burnett (HumanKind), Mark Pollard (Strategy), Clayton Christensen (JTBD).

Creative Constitution based on the Voskresensky/IKRA approach.

## License

MIT — use it, fork it, make better ads.
