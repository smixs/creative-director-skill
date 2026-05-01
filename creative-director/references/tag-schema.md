# Tag Schema — single source of truth

Frontmatter contract for `legendary-campaigns/cards/{id}.md`. All enums below are authoritative — `validate_schema.py` checks every card against this file. When extending: edit this file first, then re-validate.

---

## Required fields

| Field | Type | Cardinality | Notes |
|-------|------|-------------|-------|
| `id` | string | single | kebab-case `{brand}-{title}-{year}`, lowercase |
| `title` | string | single | campaign name as published |
| `brand` | string | single | brand name |
| `year` | int | single | 1950–2025 (most are 2010+; vintage classics included for calibration) |
| `country` | enum | single | see `country` below |
| `region` | enum | single | see `region` below |
| `industry` | enum | single | see `industry` below |
| `pattern` | enum[] | multi (1–3) | from P01–P18 |
| `category` | enum | single | format/medium |
| `idea_type` | enum | single | Pollard 7-level |
| `involvement` | enum | single | how audience engages |
| `channel` | enum | single | physical / digital / hybrid |
| `duration` | enum | single | timespan of execution |
| `goal` | enum[] | multi (1–4) | brief intent |
| `budget` | enum | single | low / medium / high |
| `emotion` | string[] | multi (1–4) | values from `emotion-hierarchy.md` |
| `emotion_tier` | int | single | 1 / 2 / 3 |
| `insight_domain` | enum | single | psychographic root |
| `media_epoch` | enum | single | distribution era |
| `awards` | enum[] | multi (0–4) | recognition |
| `quality_score` | int | single | HumanKind 1–10 |
| `scalability` | enum | single | universal / regional / unique |
| `risk` | enum | single | safe / edgy / provocative / dangerous |

## Optional/meta fields

| Field | Type | Notes |
|-------|------|-------|
| `agency` | string | creative agency, free-form (e.g. "Wieden+Kennedy", "Mother London") |
| `confidence` | enum | `high` / `medium` / `low` — for enriched stubs |
| `verification_required` | bool | `true` for low-confidence cards |
| `quality` | enum | `canonical` / `full` / `stub_enriched` / `stub_minimal` |
| `source_url` | string | primary reference link |

---

## Enums

### `country`
Two-letter ISO code (uppercase) or `Global` or `unknown`. Examples: `US`, `UK`, `BR`, `JP`, `DE`, `FR`, `AU`, `CA`, `IN`, `CN`, `MX`, `ES`, `IT`, `NL`, `SE`, `KR`, `TH`, `AE`, `ZA`, `Global`, `unknown`.

### `region`
- `north_america`
- `europe`
- `apac`
- `latam`
- `mena`
- `africa`
- `global`

### `industry`
- `alcohol`
- `automotive`
- `b2b`
- `beauty`
- `beverage` (non-alcoholic)
- `cpg`
- `education`
- `entertainment`
- `fashion_luxury`
- `finance`
- `food` (excl. QSR)
- `gaming`
- `government`
- `healthcare`
- `kids`
- `media`
- `ngo`
- `qsr`
- `real_estate`
- `retail`
- `social_causes`
- `sports`
- `tech_telco`
- `travel`
- `utilities` (energy/water/etc.)

### `pattern` (P01–P18)
- `P01` — Format as Idea
- `P02` — Enemy or Conflict
- `P03` — Behavior Inversion
- `P04` — Brand as Activist
- `P05` — Cultural Hijack
- `P06` — Limitation as Power
- `P07` — Invisible Brand
- `P08` — Craft as Message
- `P09` — User as Co-Author
- `P10` — Serialization & Ritual
- `P11` — Absurd as Carrier
- `P12` — Social Experiment
- `P13` — Truth Telling
- `P14` — Product as Proof
- `P15` — Benefit Hyperbole
- `P16` — Long-form Drama
- `P17` — Design as Idea
- `P18` — Tech as Canvas

### `category` (format/medium)
- `film`
- `integrated`
- `stunt_pr`
- `social`
- `ooh_print`
- `experiential`
- `digital_product`
- `long_form`

### `idea_type` (Pollard 7-level)
- `business`
- `brand`
- `tagline`
- `advertising`
- `campaign`
- `non_advertising`
- `execution`

### `involvement`
- `user_co_author` — audience generates content
- `participation` — active step required (challenge, vote, scan)
- `passive_view` — watch/listen only

### `channel`
- `physical`
- `digital`
- `hybrid`

### `duration`
- `moment` — one-shot stunt (≤24h)
- `campaign` — 3–6 months
- `seasonal` — recurring annually
- `ongoing` — permanent ritual / always-on

### `goal`
- `awareness`
- `trial`
- `engagement`
- `behaviour_change`
- `advocacy`
- `sales`
- `purpose`
- `brand_equity`

### `budget`
- `low` — UGC, social-first, single stunt
- `medium` — produced film + PR machinery, regional
- `high` — global production, multi-channel, talent

### `emotion_tier`
- `1` — generic (happy/sad/angry/afraid)
- `2` — specific (nostalgic, defiant, proud, etc.)
- `3` — complex (bittersweet pride, ironic sincerity, etc.)

### `emotion` values
See `references/emotion-hierarchy.md` for the authoritative 30+ values and tier mapping.

### `insight_domain`
- `identity` — how I see myself
- `community` — how I belong
- `fear` — what I avoid
- `joy` — what I seek
- `status` — how others see me
- `belonging` — being accepted
- `autonomy` — control over my life
- `survival` — basic safety/needs

### `media_epoch`
- `tv_first` — primary distribution = broadcast
- `viral_first` — designed to be shared
- `social` — native to social platforms
- `ooh` — out-of-home led
- `owned` — brand channel (app, store, site)
- `hybrid` — multi-vector

### `awards`
- `cannes_grand_prix`
- `cannes_gold`
- `cannes_silver`
- `cannes_bronze`
- `dnad_black_pencil`
- `dnad_yellow_pencil`
- `dnad_white_pencil`
- `one_show`
- `clio`
- `effie`
- `webby`
- `multiple` — meta-tag for 5+ awards across shows
- `none`
- `unknown`

### `quality_score` (HumanKind 1–10)
See `SKILL.md` "HumanKind Scale" section. Integers only.

### `scalability`
- `universal` — works in any market without adaptation
- `regional` — needs cultural adaptation
- `unique` — irreproducible (one-off cultural moment)

### `risk`
- `safe` — no controversy potential
- `edgy` — challenges convention but unlikely to backlash
- `provocative` — designed to provoke; backlash possible
- `dangerous` — high backlash risk; backlash occurred

---

## Unknown handling

When a value cannot be determined from public sources:
- Omit the field if optional
- Use `unknown` if the enum supports it (`awards: [unknown]`)
- For required fields without `unknown` support, set `confidence: low` and `verification_required: true`

Never invent values. `unknown` is always preferred over a guess.

---

## ID generation rules

Format: `{brand-slug}-{title-slug}-{year}`

- Lowercase, kebab-case
- Strip articles ("the", "a", "an") from title
- Strip punctuation
- Collapse whitespace to single hyphen
- Year always 4-digit
- Collisions: append `-2`, `-3`, etc.

Examples:
- `dove-real-beauty-sketches-2013`
- `burger-king-moldy-whopper-2020`
- `ikea-pee-ad-2018`
- `nike-dream-crazy-2018`
