# 🎬 Creative Director Skill

[![Claude Skill](https://img.shields.io/badge/Claude-Skill-blueviolet?style=flat-square)](https://docs.anthropic.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Methods 20+](https://img.shields.io/badge/Methods-20%2B-orange?style=flat-square)](#методологии-20)
[![Case Library](https://img.shields.io/badge/Cases-571-blue?style=flat-square)](#библиотека-кейсов)
[![Version](https://img.shields.io/badge/Version-2.0-red?style=flat-square)](#что-нового-в-v20)

**🇬🇧 [Read in English](README.md)**

> Создан в соавторстве с **Paul Deadcough**.

AI-креативный директор, который генерирует рекламные концепции по методологиям мирового уровня, оценивает их по критериям, калиброванным на Cannes/D&AD, рекурсивно дорабатывает до порога качества и **калибрует каждую идею по библиотеке из 571 легендарной кампании** для детекции насыщения и контроля оригинальности.

Не игрушка для брейншторма. Структурированный креативный процесс, который повторяет реальную работу топ-агентств (Droga5, Wieden+Kennedy, Mother) — инсайт перед идеями, методология вместо свободных ассоциаций, честная оценка вместо лести, **калибровка по канону** вместо изобретения с нуля.

---

## Что нового в v2.0

- **Библиотека из 571 кейса** с полной структурой Insight / Mechanic / Why-it-worked / Steal на каждой карточке
- **17-осевая schema frontmatter** — каждая карточка размечена по pattern (P01–P18), индустрии, формату, эмоции (Tier 1/2/3), бюджету, idea_type (7-уровневая таксономия Pollard), наградам и т.д.
- **6 MOC** (Maps of Content) для быстрого поиска по паттерну, эмоции, формату, индустрии, бюджету и хронологии
- **4-точечная интеграция case library** в workflow — прайминг перед генерацией, эмпирический cap оригинальности, RESTART через case-soaking, pattern calibration перед exit
- **3 maintenance-скрипта** (Python через `uv`) — schema validation, MOC generation, граф wikilinks
- **7-уровневая таксономия идей Pollard** заменяет прежнюю 3-уровневую систему
- **3-уровневая иерархия эмоций** с 30+ конкретными значениями
- **Activation toolkit** с 9 форматами и тестом Non-advertising vs Execution
- **Pre-Mortem template** перед финальной выдачей

Качество проверено через [`skill-conductor`](https://github.com/smixs/skill-conductor): **41/50 production-grade** (Discovery 7/10, Clarity 9/10, Efficiency 7/10, Robustness 8/10, Completeness 10/10).

---

## Что делает

Скармливаешь бриф в любом формате — текст, voice transcript, PDF, заметки — и получаешь полный креативный цикл:

1. **INTAKE** — извлекает ДНК брифа: продукт, аудитория, цели, ограничения + классифицирует требуемый уровень идеи через 7-уровневую таксономию Pollard (business / brand / tagline / advertising / campaign / non_advertising / execution)
2. **INSIGHT** — добывает потребительские инсайты по 7 техникам (Mark Pollard, JTBD, Tension Spotting, HMW, Abstraction Laddering)
3. **IDEATION** — праймится по канону (сканирует 5–7 кейсов из релевантного MOC), затем генерирует 8–12 идей по 3 методам из разных категорий (структурный × ассоциативный × подрывной), ротируя 20+ методологий, с Tension test на каждой
4. **EVALUATE + REFINE** — оценивает по 6 взвешенным критериям + HumanKind + Grey Scale, рекурсивно улучшает; **Originality эмпирически ограничен** насыщением библиотеки (3+ канонических кейса с той же механикой → cap 7); при плато RESTART через case-soaking (читает 8–12 канонических карточек, ремикс разрешён); Pattern Calibration + Pre-Mortem перед exit
5. **ARTICULATE** — выдаёт результат в presentation-ready формате (one-pager, top-3, campaign platform или quick response)

Можно входить с любой фазы: jump к insight mining, оценить готовую идею, сгенерировать концепты по известному инсайту.

## Зачем это

Большинство AI-«креативных» инструментов генерируют идеи свободной ассоциацией — производят объём без структуры. Результат: сотни посредственных концептов, которые никто не может оценить, часто неосознанно повторяя уже сделанную работу.

Этот скилл навязывает дисциплину, которая отделяет award-winning работу от наполнителя:

- **Insight-first** — никакой ideation без валидированного потребительского tension
- **Структурные методы** — SIT, TRIZ, SCAMPER, Bisociation, Synectics, а не «дай 10 идей»
- **Эмпирическая оригинальность** — каждая идея проверяется по 571 реальной кампании; если 3+ канонических кейса используют ту же механику, originality ограничен, не объявлен субъективно
- **Честная оценка** — калибровка по реальным Cannes-победителям, anti-inflation rules
- **Рекурсивное улучшение** — слабые критерии получают targeted improvement разными методами на каждом проходе
- **Case-soaking при плато** — когда идеи плато, скилл читает 8–12 канонических карточек, чтобы re-train ощущение что такое сильный инсайт; комбинирование/ремикс существующих паттернов разрешён явно (так строится Cannes-grade work)
- **Kill Your Darlings** — скилл аргументирует против собственных любимых идей, чтобы проверить их силу
- **Pre-Mortem** — перед финалом симулирует провал и поднимает наиболее вероятные failure modes

## Что внутри

```
creative-director/
├── SKILL.md                                  # Ядро скилла — phase router + 5-фазный workflow
├── assets/
│   └── output-templates.md                   # 4 формата презентации
├── scripts/                                  # Python через uv (PEP 723 inline deps)
│   ├── validate_schema.py                    # Валидация frontmatter по tag-schema
│   ├── generate_mocs.py                      # Билдит 6 MOC из cards
│   └── generate_links.py                     # Добавляет Related-секции (идемпотентно)
└── references/
    ├── tag-schema.md                         # Single source of truth — 17-осевой контракт frontmatter
    ├── idea-taxonomy.md                      # 7-уровневая таксономия Pollard
    ├── emotion-hierarchy.md                  # Tier 1/2/3 + 30+ конкретных значений эмоций
    ├── activation-toolkit.md                 # 9 форматов активаций + Non-ad vs Execution test
    ├── legendary-patterns.md                 # P01-P18 механики + Pre-Mortem template
    ├── methods-catalog.md                    # 20 креативных методологий как actionable cards
    ├── method-selection-matrix.md            # Тип задачи → метод + правила ротации
    ├── insight-mining.md                     # 7 техник поиска инсайта
    ├── scoring-calibration.md                # Детальные rubrics + калибровочные якоря
    ├── creative-constitution.md              # 3-слойная система оценки + правила обратной связи
    ├── storytelling-frameworks.md            # 6 нарративных фреймворков для рекламы
    └── legendary-campaigns/                  # Библиотека 571 кейса
        ├── README.md                         # Гид по библиотеке
        ├── MOC-index.md                      # Все 571 карточек по году DESC
        ├── MOC-pattern.md                    # Группировка по P01–P18 (18 механик)
        ├── MOC-emotion.md                    # Группировка по emotion_tier (3 → 2 → 1)
        ├── MOC-format.md                     # Группировка по category (film/integrated/stunt_pr/...)
        ├── MOC-industry.md                   # Группировка по индустриальной вертикали
        ├── MOC-budget.md                     # Группировка по бюджету (low/medium/high)
        └── cards/                            # 571 индивидуальная карточка (плоский namespace)
            └── {id}.md
```

## Библиотека кейсов

571 рекламная кампания с 1950 по 2025, размечена по **17 осям**, с полным структурным анализом на каждой карточке.

### Структура карточки

YAML frontmatter (17 осей — см. `references/tag-schema.md`) + 4 секции:

- **Insight** — человеческая правда, которую кампания эксплуатирует (одно предложение)
- **Mechanic** — что именно было сделано
- **Why it worked** — психологическая / культурная / структурная причина
- **Steal** — pattern-уровневая стратегия заимствования
- **Related** — auto-generated wikilinks (pattern hub + 2 sibling cards + emotion match)

### Tag schema (17 осей)

`id`, `title`, `brand`, `agency`, `year`, `country`, `region`, `industry`, `pattern[]` (P01–P18), `category`, `idea_type` (7-уровневая Pollard), `involvement`, `channel`, `duration`, `goal[]`, `budget`, `emotion[]`, `emotion_tier` (1/2/3), `insight_domain`, `media_epoch`, `awards[]`, `quality_score` (HumanKind 1–10), `scalability`, `risk`.

### 18 паттернов (P01–P18)

Format as Idea · Enemy or Conflict · Behavior Inversion · Brand as Activist · Cultural Hijack · Limitation as Power · Invisible Brand · Craft as Message · User as Co-Author · Serialization & Ritual · Absurd as Carrier · Social Experiment · Truth Telling · Product as Proof · Benefit Hyperbole · Long-form Drama · Design as Idea · Tech as Canvas

### Стратегии поиска

```bash
# Browse по оси — открой соответствующий MOC
# Каждая строка содержит inline-context (бренд · год · формат · эмоция · бюджет · top award)

# Фильтр по комбинации — ripgrep по frontmatter
rg -l "^budget: low$" cards/ | xargs rg -l "^emotion_tier: 3$"

# Все P11 кейсы с 2020
rg -l "P11" cards/ | xargs rg -l "^year: 202"

# Все canonical кейсы для QSR
rg -l "^industry: qsr$" cards/ | xargs rg -l "^quality: canonical$"
```

### Карта насыщения (давление на оригинальность)

| Паттерн | Насыщение | Cap оригинальности |
|---------|-----------|-------------------|
| P11 (Absurd as Carrier), P16 (Long-form Drama), P09 (User as Co-Author) | высокое (>50 кейсов) | ≤6 без структурно нового варианта |
| P02, P10, P12, P14, P18 | среднее | ≤7 если 3+ канонических с той же механикой |
| P01, P15 | низкое | пространство для новизны |

Это эмпирическое насыщение, не субъективная новизна.

## Методологии (20+)

| Категория | Методы |
|-----------|--------|
| **Структурные** | SIT/Goldenberg Templates, SCAMPER, TRIZ (10 принципов), Morphological Analysis |
| **Ассоциация** | Bisociation, Random Entry, Forced Connections, Synectics |
| **Инверсия** | Reverse Brainstorming, Worst Possible Idea, Provocation PO |
| **Возмущение** | Oblique Strategies, Six Thinking Hats, Disney Creative Strategy |
| **Объём** | Crazy 8s, Brainwriting 6-3-5, Starbursting |
| **Бонус** | First Principles Thinking, Lateral Thinking Toolkit, Design Sprint Sketch |

## Система оценки

Три параллельные системы, калиброванные по реальным кампаниям:

- **6 взвешенных критериев** — Originality (0.25, эмпирически ограничен библиотекой), Strategic Fit (0.20), Emotional Response (0.20, иерархия Tier 1/2/3), Feasibility (0.15), Scalability (0.10), Simplicity (0.10)
- **HumanKind Scale** (Leo Burnett) — 1–10, от «Destructive» до «Changes the World»
- **Grey Scale** (Grey Group) — 1–10, от «Toxic» до «Best in the World»

Anti-inflation rules: batch control, normal distribution, тест реальных аналогов, specificity test, time test, **эмпирический cap по case library**.

## Таксономия идей (Pollard 7-level)

| Уровень | Когда нужен | Жизнь |
|---------|-------------|-------|
| `business` | новый бизнес, repositioning всей компании | годы |
| `brand` | ребрендинг, brand platform — «за что бренд стоит?» | 5–10+ лет |
| `tagline` | короткая фраза, кристаллизующая brand idea | 5–10+ лет |
| `advertising` | центральная мысль во всех коммах — узнаваемая без логотипа | 3–5 лет |
| `campaign` | сезонная кампания, запуск продукта, промо | 3–12 месяцев |
| `non_advertising` | активация/utility/культурный объект, живущий без рекламы | varies |
| `execution` | one-off канал/формат/механика | дни–недели |

**Activation diagnostic:** если бриф упоминает activation/stunt/utility — применить тест «убери кампанию, идея сохраняет смысл?» → Да = `non_advertising` / Нет = `execution`.

## Иерархия эмоций (Tier 1/2/3)

- **Tier 1 (забываемые):** happy, sad, angry, afraid → score ≤ 6
- **Tier 2 (запоминаемые):** nostalgic, defiant, proud, ironic и др. → score 6–8
- **Tier 3 (величие):** bittersweet pride, ironic sincerity, vulnerable defiance и др. → score 8–10
- **Score 9+ требует Tier 3.**

## Как работает рекурсия

```
Генерация идей (3 метода, 8-12 идей, праймнутых по канону)
        ↓
Tension test на каждую идею
        ↓
Оценка top 3 (6 критериев + HumanKind + Grey, originality capped по насыщению)
        ↓
    Score ≥ 9? ──→ ДА → Pattern Calibration + Pre-Mortem → Output
        ↓ НЕТ
Идентификация слабых критериев → Применить другой метод → Rescore
        ↓
    Плато? ──→ ДА → RESTART через case-soaking
        ↓             (читать 8-12 канонических карточек, ремикс разрешён)
        ↓ НЕТ
    Continue refinement
        ↓
    5 проходов? ──→ ДА → Output best + честная оценка
```

## Storytelling-фреймворки

Story Spine (Pixar) · Sparkline (Nancy Duarte) · Freytag's Pyramid · Monroe's Motivated Sequence · Pixar Rules · Hero's Journey (StoryBrand)

## Установка

### Claude Code (рекомендуется)

```bash
git clone https://github.com/smixs/creative-director-skill.git
cp -r creative-director-skill/creative-director ~/.claude/skills/
```

После установки перезапусти сессию Claude Code (`/clear` или новая сессия), чтобы скилл подхватился.

### Claude Projects

Добавь файлы в knowledge base своего Claude Project. Загрузи все файлы из `creative-director/` — `SKILL.md` это entry point, ссылается на остальные через `[[wikilinks]]`.

### Другие AI-агенты (Cursor, Windsurf, GPT, Gemini)

Скилл работает с любым AI-агентом, поддерживающим структурированные инструкции — core logic в markdown-файлах, без platform lock-in. Скопируй папку `creative-director/` в свой проект или skills-директорию.

## Maintenance-скрипты

Три Python-скрипта (запуск через `uv run`, PEP 723 inline deps — без manual setup):

```bash
cd creative-director
uv run scripts/validate_schema.py        # Валидация frontmatter всех карточек
uv run scripts/generate_mocs.py          # Перегенерация 6 MOC из карточек
uv run scripts/generate_links.py         # Перегенерация Related-секций (идемпотентно)
```

Pipeline: edit/add cards → validate → regenerate MOCs → regenerate links.

## Примеры использования

**Полный креативный цикл:**
> «Придумай кампанию для [бренда]. ЦА: [кто]. Бюджет: [диапазон]. Каналы: [где].»

**Insight mining:**
> «Найди потребительский инсайт для [категории]. Бриф говорит [контекст].»

**Оценить готовую идею:**
> «Оцени эту концепцию: [описание]. Цель брифа: [goal].»

**Активация / non-advertising:**
> «Нужен PR-стант для [бренда]. Бюджет low, должен дать earned media за неделю. Не кампания — one-shot активация.»

**Быстрая ideation:**
> «Нужно 5 концептов для соцсетей [бренда] на тему [topic].»

## Для чего НЕ подходит

- Медиапланирование или распределение бюджета
- Управление продакшном
- Brand identity / дизайн логотипа
- Финальный копирайтинг (генерирует концепты, не отполированный текст)
- Сбор данных market research
- Brand positioning warmaps (используй отдельный позиционный скилл)

## Ограничения и честные заметки

- **Auto-trigger в `claude -p` mode ненадёжен.** Это advisory-скилл — при one-shot CLI модель часто отвечает на креативные брифы напрямую, не консультируясь со скиллом. Для consistent поведения в интерактивных сессиях вызывай явно или давай развёрнутый бриф (>500 chars со структурой).
- **571 source URL не верифицированы.** Библиотека собрана из публичных индексов award-show; верифицируй ссылки вручную перед цитированием в client work.
- **12 карточек имеют `confidence: low`** с `verification_required: true` — их стоит cross-check по внешним источникам. Скилл предпочитает `quality: canonical` для калибровки.
- **Библиотека статична.** Кампании с 2026+ не добавляются автоматически; периодическое расширение вручную.

## Авторство

Создан в соавторстве с **Paul Deadcough**.

Построено на методологиях: Jacob Goldenberg (SIT), Genrich Altshuller (TRIZ), Edward de Bono (Lateral Thinking, Six Hats, PO), Arthur Koestler (Bisociation), William Gordon (Synectics), Brian Eno (Oblique Strategies), Nancy Duarte (Sparkline), Joseph Campbell / Donald Miller (Hero's Journey / StoryBrand), Leo Burnett (HumanKind), Mark Pollard (Strategy + 7-level Taxonomy), Clayton Christensen (JTBD).

Creative Constitution — на основе подхода Воскресенский / IKRA.

Библиотека кейсов курирована из shortlist'ов D&AD, Cannes Lions, One Show, Webby и Effie 1950–2025.

## Лицензия

MIT — используй, форкай, делай рекламу лучше.
