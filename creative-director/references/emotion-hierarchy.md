# Emotion Hierarchy

Generic emotions make advertising forgettable because they are shared by every campaign in every category. When a brief says "make people feel happy," the audience has no reason to store the memory — the emotion is undifferentiated from a hundred competing messages. Tier 3 emotions (complex, contradictory) are memorable because they match how humans actually feel: not one thing at a time, but two opposing things simultaneously. Holding that tension without resolving it is what separates great creative from adequate creative.

---

## Tier 1 — Generic / Forgettable

These emotions are universal, low-resolution, and cliché in advertising context.

- `happy`
- `sad`
- `angry`
- `afraid`
- `surprised`
- `disgusted`

**Why they underperform:** Everyone feels them, so nothing differentiates. "Happy" describes a Coke ad, a dog food ad, and a bank ad equally. The emotion carries no information about the brand, the insight, or the audience. Targeting Tier 1 guarantees forgettability: no specificity → no distinctiveness → no recall. Score ceiling: 6/10.

---

## Tier 2 — Specific / Memorable

Single emotions, but precise enough to belong to a specific truth about a specific audience.

| Value | Definition |
|-------|------------|
| `nostalgic` | Longing for a past that felt simpler or more whole |
| `defiant` | Resistance to a norm, expectation, or authority |
| `melancholic` | Quiet, reflective sadness without acute pain |
| `proud` | Satisfaction derived from achievement or identity |
| `wistful` | Gentle regret for something that cannot be recovered |
| `triumphant` | Exhilaration at overcoming specific obstacles |
| `protective` | Fierce care for someone or something vulnerable |
| `reverent` | Deep respect bordering on awe, without irony |
| `hopeful` | Forward-looking belief that things can improve |
| `ironic` | Awareness of the gap between expectation and reality |
| `ashamed` | Recognition of falling short of one's own standard |
| `belonging` | Relief at being part of a group that accepts you |
| `vulnerable` | Exposure of an unguarded, authentic self |
| `recognized` | The feeling of being seen accurately by others |
| `witnessed` | Being seen in a moment of difficulty or significance |

---

## Tier 3 — Complex / Greatness

Two emotions in unresolved tension. Cannot be explained in one word. Memorable because they match real emotional experience rather than a simplified version of it.

| Value | Definition | Canonical campaigns |
|-------|------------|---------------------|
| `bittersweet_pride` | Pride in achievement shadowed by awareness of cost or loss | Procter & Gamble "Thank You Mom" (2012); Always "Like a Girl" (2014) |
| `defensive_hope` | Hope held carefully, guarded against disappointment | Volkswagen "Think Small" (1959); Dove "Real Beauty" (2004) |
| `ironic_sincerity` | Genuine message delivered through playful or self-aware tone | Old Spice "The Man Your Man Could Smell Like" (2010); Cards Against Humanity Black Friday (2015) |
| `wry_affection` | Love expressed through gentle mockery rather than sentimentality | John Lewis "Man on the Moon" (2015); Guinness "Surfer" (1999) |
| `vulnerable_defiance` | Strength claimed from a position of acknowledged weakness | Nike "Dream Crazy" (2018); Eminem "Lose Yourself" (not ad, but referenced in Chrysler "Born of Fire" 2011) |
| `melancholic_joy` | Happiness that is intensified by the knowledge it will end | Thai Life Insurance long-form films (2014–2018); Sony Bravia "Balls" (2005) |
| `reluctant_optimism` | Cautious forward movement despite evidence against it | Apple "1984" (1984); Heineken "Worlds Apart" (2017) |
| `dignified_grief` | Loss processed without collapse — sorrow held with composure | Google "Parisian Love" (2010); MetLife Hong Kong "My Dad is a Liar" (2015) |
| `cathartic_release` | Relief that arrives only after sustained tension — earned, not given | Nike "Just Do It" original (1988); Gillette "We Believe" (2019) |
| `sublime_terror` | Awe mixed with fear — scale or power that dwarfs the viewer | Sony PlayStation "Double Life" (1999); Volvo Trucks "The Epic Split" (2013) |

---

## Tier Test — Which Tier Is This Idea?

Ask these questions in sequence. Stop when you have an answer.

**Step 1.** Write the emotion in one word. Can you replace it with happy / sad / angry / afraid? If yes → Tier 1.

**Step 2.** Is the emotion specific enough that it excludes most other brands in the category? If no → still Tier 1. If yes → candidate for Tier 2.

**Step 3.** Does the emotion contain a contradiction — two feelings that should not coexist but do? If no → Tier 2. If yes → candidate for Tier 3.

**Step 4.** Would a reasonable person say "that's exactly how I feel about this, but I never had a word for it"? If yes → confirmed Tier 3.

**Step 5.** Can the emotion sustain a full campaign, not just a single execution? If no, reconsider whether it is an insight or a tactic.

---

## Scoring Rule

| Tier | `emotional_response` score range |
|------|----------------------------------|
| Tier 1 | ≤ 6 |
| Tier 2 | 6 – 8 |
| Tier 3 | 8 – 10 |

Score 9+ requires Tier 3. If the nominated emotion cannot be expressed as a compound (two tensions in coexistence), the score cannot exceed 8 regardless of execution quality.

---

## Vocabulary Expansion

Extended list of specific emotions for use when describing or evaluating ideas. Organized by facet. All values are snake_case for frontmatter use.

### Loss
`grief` / `mourning` / `nostalgia` / `wistful` / `melancholic` / `elegiac` / `bereft`

### Recognition
`recognized` / `witnessed` / `validated` / `seen` / `understood` / `known`

### Belonging
`belonging` / `included` / `welcomed` / `claimed` / `rooted` / `bonded`

### Status
`proud` / `ashamed` / `humiliated` / `dignified` / `triumphant` / `envious` / `admired`

### Fear
`afraid` / `dread` / `anxious` / `wary` / `vigilant` / `vulnerable`

### Hope
`hopeful` / `optimistic` / `longing` / `expectant` / `trusting`

### Defiance
`defiant` / `rebellious` / `indignant` / `resolute` / `fierce`

### Complexity (Tier 3 building blocks)
`bittersweet_pride` / `defensive_hope` / `ironic_sincerity` / `wry_affection` / `vulnerable_defiance` / `melancholic_joy` / `reluctant_optimism` / `dignified_grief` / `cathartic_release` / `sublime_terror`

---

## Use in creative-director Skill

- **Phase 4, Axis 2 — Emotional Response:** When scoring this criterion (weight 0.20), identify the emotion first using the Tier Test above, then apply the Scoring Rule. Justify the tier in the axis rationale field. Never accept "positive emotion" as a description.
- **Pre-Mortem:** If the nominated emotion is Tier 1, flag as a risk: "emotional underdifferentiation — audience will not recall this." Require the team to articulate a Tier 2 or Tier 3 replacement before proceeding.

---

## Authoritative `emotion` Values for tag-schema.md

This block is the single source of truth for the `emotion` frontmatter field (multi, 1–4 values).

```
# Tier 1 (use only for legacy/archival cards)
happy
sad
angry
afraid
surprised
disgusted

# Tier 2
nostalgic
defiant
melancholic
proud
wistful
triumphant
protective
reverent
hopeful
ironic
ashamed
belonging
vulnerable
recognized
witnessed
validated
longing
indignant
resolute
dignified
anxious
envious
bonded

# Tier 3
bittersweet_pride
defensive_hope
ironic_sincerity
wry_affection
vulnerable_defiance
melancholic_joy
reluctant_optimism
dignified_grief
cathartic_release
sublime_terror
```
