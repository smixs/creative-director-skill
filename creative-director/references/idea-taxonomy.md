# Idea Taxonomy — Pollard 7-Level Framework

Source: Mark Pollard, "How to Explain an Idea" (Sweathead / 7 Types of Ideas in Advertising)

Most failures in creative work are not caused by bad ideas — they are caused by ideas operating at the wrong level. A client briefs a campaign idea; the agency returns an execution. Or a month is spent on a brand idea when the actual ask was a campaign. Knowing which level you are on determines what you are searching for, how to evaluate it, and how to sell it. Mixing levels is the single most common source of misaligned creative work.

The `idea_type` field in card frontmatter maps directly to this taxonomy. Authoritative enum values: `business` / `brand` / `tagline` / `advertising` / `campaign` / `non_advertising` / `execution`.

---

## Level 1 — Business Idea

**What it is:** What the company does — that is novel.

**Question:** "What new thing does this business do in the world?"

**Examples:**
- Uber — private rides on demand, no dispatcher
- Airbnb — rent a stranger's home as accommodation
- Dollar Shave Club — razor subscription, cutting out retail markup

**Lifespan:** Foundational; changes only with pivots or acquisitions.

**Agency works on this?** Rarely. This is the domain of founders and strategy consultants.

**When critical:** New product launch, full business repositioning, startup brief.

---

## Level 2 — Brand Idea

**What it is:** What the company stands for — beyond selling the product.

**Question:** "What does this brand believe in, that is not just a product claim?"

**Examples:**
- Nike — every human being is an athlete
- Dove — real beauty, unretouched
- Patagonia — don't buy this jacket (anti-consumerism as brand stance)

**Lifespan:** Years, often decades. The brand platform.

**Agency works on this?** Yes — this is the core strategic assignment.

**When critical:** Brand platform development, rebrand, positioning work.

---

## Level 3 — Brand Tagline

**What it is:** A short phrase that crystallizes the brand idea.

**Question:** "How do you say this brand idea in five words or fewer?"

**Examples:**
- "Just Do It" — Nike brand idea compressed to three words
- "Real Beauty" — Dove brand idea as two-word anchor
- "Think Different" — Apple's brand stance made portable

**Lifespan:** Long; should not be rotated with campaigns.

**Agency works on this?** Yes, always in tandem with the brand idea. A tagline without a brand idea is an empty slogan. A brand idea without a tagline has substance but no formula.

**When critical:** Rebrand, platform consolidation, market entry.

---

## Level 4 — Advertising Idea

**What it is:** The central creative thought that governs all brand communications over time.

**Question:** "If you removed the logo, would the idea still be recognizable as this brand?"

**Examples:**
- Old Spice — "the man you could smell like" territory: the man your man could smell like, works in any format, any year
- Snickers — "you're not you when you're hungry": any human lapse becomes a Snickers moment
- Apple Mac — "I'm a Mac / I'm a PC": the contrast between old and new thinking, infinitely extensible

**Lifespan:** Several years. Does not rotate with each campaign.

**Agency works on this?** Yes — this is the primary creative assignment.

**When critical:** Establishing long-term creative platform; briefing a new creative team.

---

## Level 5 — Campaign Idea

**What it is:** A subset of the advertising idea applied to a specific period, product, or moment.

**Question:** "How do we express the advertising idea right now, for this brief?"

**Examples:**
- Old Spice advertising idea: "the man your man could smell like" territory → Campaign 2010: "The Man Your Man Could Smell Like" — specific character, format, viral video
- Dove advertising idea: real beauty → Campaign: "Real Beauty Sketches" — specific execution of the underlying belief for one window
- Nike advertising idea: every human is an athlete → Campaign: "Find Your Greatness" (London 2012) — ordinary people, ordinary places

**Lifespan:** 3–12 months.

**Agency works on this?** Yes — the most frequent client deliverable.

**When critical:** Q1/Q2/Q3 campaign briefs, product launches tied to a seasonal window.

---

## Level 6 — Non-advertising Idea

**What it is:** A concept that solves a problem or creates value — but is not an advertisement, even if it can be advertised.

**Question:** "Instead of talking about the product, can we create something useful or meaningful?"

**Examples:**
- Earth Hour (WWF) — a global switch-off, not a commercial
- Dove Real Beauty Sketches — a social experiment, not a soap ad
- Nike+ app — a product for runners, not advertising for shoes

**Lifespan:** Variable; depends on the initiative's scope and infrastructure.

**Agency works on this?** Yes, and increasingly so. Pitched differently — as a cultural object, not a media spend.

**When critical:** Brand wants to become part of life rather than interrupt it. Activation briefs where the concept must stand independently.

---

## Level 7 — Execution

**What it is:** The specific decisions that deliver the idea — style, channel, format, technology, director, tone.

**Question:** "How exactly does this look, sound, and feel?"

**Examples:**
- 3D typography treatment
- A specific TikTok-native format
- Casting an unknown instead of a celebrity
- Augmented reality layer in-store

**Lifespan:** Tied to the campaign window.

**Agency works on this?** Yes, but only after the idea is locked. Execution before idea is the most common creative process failure.

**When critical:** After the idea is agreed. Not before.

---

## Where Does Activation Live?

Activation is a format or engagement mechanic — not a fixed level in the hierarchy. It can exist at two levels:

**Activation as Non-advertising Idea (standalone)**

The activation itself is the idea. It has its own concept and meaning and does not require a campaign above it.

Test: "Is there a higher-order idea this activation expresses?" If no — it is a non-advertising idea.

Examples: Earth Hour, Whopper Sacrifice ("delete 10 friends, get a free burger"), Ice Bucket Challenge.

Pitch as: "We are creating something new in culture."

**Activation as Execution (inside a Campaign Idea)**

The brand has a campaign idea; the activation is one way to express it.

Test: "Does this mechanic only exist because there is a campaign idea above it?" If yes — it is execution.

Example: Nike "Just Do It" campaign idea → a running challenge inside the app (activation = execution of the campaign).

Pitch as: "Here is how we activate our campaign idea."

**Grey zone — Content Idea**

Pollard mentioned an eighth type: content idea, defined as "jargon for stuff that isn't an ad." Brand podcast, YouTube series, recurring social posts. Not a campaign idea (no unifying thought), not a non-advertising idea (does not solve a problem independently), not execution (too autonomous). Pollard ultimately removed it from the canonical seven. Treat it as either a weak campaign idea or execution — do not use it as a standalone category.

**Diagnostic rule for activation:**

Ask: "If the campaign disappeared tomorrow, would this activation still make sense?"
- Yes → non-advertising idea
- No → execution inside a campaign idea

The answer changes the budget conversation, the scope, and the pitch logic.

---

## Diagnostic Table: Client Says X → Likely Needs Y

| Client says | Likely needs |
|---|---|
| "We need to rethink the brand" | `brand` + `tagline` |
| "We need a big idea for the brand" | `advertising` |
| "We need a campaign for Q3" | `campaign` |
| "We need an activation / event / promo" | Clarify first: self-contained concept (→ `non_advertising`) or mechanic inside a campaign (→ `execution`)? |
| "We need a tagline" | `tagline` — but brand idea must exist first |
| "We need an idea for a TV spot" | `campaign` → `execution` |

---

## Common Level-Mixing Mistakes

**Execution presented as an idea.**
"Our idea: we partner with a famous blogger." That is execution. Where is the idea?

**Campaign idea locked in as advertising idea.**
Client approves a campaign idea as "the brand foundation for five years." In twelve months it is dated and the brand has no platform underneath it.

**Brand idea without advertising idea.**
A beautiful brand platform exists. No one can answer: what does this look like in a commercial?

**Non-advertising idea disconnected from brand idea.**
The brand launches a brilliant initiative that any competitor could have launched. No brand equity is built.

---

## How to Explain an Idea — Pollard Principles (compressed)

**Logline (25 words or fewer)**
State the idea without describing the execution. Format: "We [do / create / say] [to whom] [what exactly] [why it is new]."
Earth Hour: "We ask the entire world to turn off its lights for one hour."
Test: if the logline requires clarification, the idea is not ready.

**Label (name the idea)**
Name the idea before the presentation. Otherwise the client names it ("that idea with the cat"). Good labels: Earth Hour, Real Beauty, The Man Your Man Could Smell Like. Bad labels: Concept A, Option B, Social Mechanic.

**Blink Test**
Ideas are bought in seconds or not at all. If you need three minutes to explain it, it is not a single idea — it is a collection of elements. One sentence, one image, one moment of "got it."

**Separate idea from execution**
Present in order: what is it → how does it work → how does it look. Never open with "we're going to use an AR filter that..."

**Pause and repeat**
Say less than you think you need to. Repeat the key phrase. The best signal: the client starts adding to the idea themselves.

---

## 5 Presentation Structures

**A. Logline (15 seconds)**
1. Problem: "You know how..."
2. Idea: "We came up with..."
3. Hook: "Want to hear more?"

**B. Aristotle 3-Act**
1. Act 1 — Problem: stakes, tension, context
2. Act 2 — Idea: reveal it, show how it works
3. Act 3 — Ask: next steps, what you need from the client

**C. Hollywood Logline**
Precedent + Character + Conflict + Resolution.
"This is [known reference] meets [other reference], but for [our audience]."

**D. Visionary (emotional impact)**
1. Image or film clip that opens a gap in the room
2. "What if we could change this?"
3. Idea as the answer

**E. Pecha Kucha (discipline)**
Hard time limit. "I'll show this in five minutes." Tension through constraint. Forces ruthless editing.

---

## Use in creative-director Skill

- **Phase 1 INTAKE:** Before generating or evaluating ideas, identify which level is actually being requested. Misread level = wrong deliverable. Ask if unclear.
- **Phase 4 PASS 0 (selection):** Classify every candidate idea by level before scoring. An execution cannot compete against a campaign idea in the same pass.
- **Activation briefs:** Apply the non-advertising vs. execution diagnostic before scoping any activation work. See `activation-toolkit.md` for mechanics. The answer changes pitch framing, budget logic, and what "done" looks like.
