# LocatorisLLM — Product Requirements Document (PRD)

## 1. Overview

LocatorisLLM is a location-based business intelligence platform designed to help
entrepreneurs, business owners, and analysts evaluate whether a business is
likely to perform well in a specific geographic area.

Rather than relying on proprietary or scraped data, LocatorisLLM combines:
- open geographic datasets
- deterministic analytics
- probabilistic business signals
- and LLM-based explanation

to produce defensible, explainable insights that support decision-making without
claiming certainty or prediction.

---

## 2. Problem Statement

Business owners struggle to answer questions such as:
- Is this area saturated for my type of business?
- What kind of business is missing here?
- Does demand justify premium or affordable pricing?
- Would a mobile business outperform a fixed location?

Existing solutions either:
- provide raw maps without interpretation, or
- rely on closed, expensive, or legally restrictive data sources

LocatorisLLM is designed to provide **analysis, not raw data**, and **reasoned
insights, not scraped metrics**.

---

## 3. Target Users

- Small and medium business owners
- Mobile vendors (food trucks, pop-ups, temporary stalls)
- Entrepreneurs and startup founders
- Market researchers and consultants
- Urban planners (secondary use case)

---

## 4. Core Design Principles

1. **Compliance-first**  
   Only open, permissive, and redistributable data sources are used.

2. **Explainability over certainty**  
   Insights must be traceable to underlying assumptions and signals.

3. **Global by default**  
   The system must work reasonably well across countries without
   country-specific hardcoding.

4. **Upgradeable architecture**  
   Paid or licensed data sources may be added later without redesigning
   the system.

---

## 5. Product Scope & Phases

### Phase 2 — Business Ontology & Classification (Completed)

- Canonical industry and sub-industry registry
- Deterministic classification from map-based tags
- Clear separation between:
  - raw data tags (e.g. `tourism=*`)
  - economic behavior (e.g. hospitality vs culture)
- Support for healthcare, food, retail, education, tourism, recreation,
  professional services, and informal economy

---

### Phase 3 — Competition & Density Analysis

- Distance-weighted competitor analysis
- Business clustering and saturation metrics
- Identification of underserved industries and sub-industries
- Support for both fixed-location and mobile businesses

---

### Phase 4 — Reputation & Price Signal Modeling

Rather than scraping reviews or prices, LocatorisLLM models **per-business
signals** that approximate reputation and price positioning.

#### Reputation Signals (examples):
- business longevity and survival density
- brand vs independent presence
- proximity to demand anchors (tourism, offices, transit)
- opening-hours intensity
- category stability in the surrounding area

#### Price Position Signals (examples):
- surrounding business mix (luxury vs utility)
- land-use intensity
- proximity to premium anchors
- industry-specific pricing norms

Signals are combined probabilistically and expressed with confidence levels,
not absolute values.

---

### Phase 5 — Temporal & Behavioral Analysis

- Time-of-day and day-of-week demand proxies
- Recreation, tourism, and event spillover logic
- Mobility-aware reasoning for mobile businesses
- Adaptive time windows inferred from data, not hardcoded

---

### Phase 6 — LLM Reasoning Layer (RAG)

- Retrieval-Augmented Generation (RAG)
- LLMs receive **structured analytics only**
- No external browsing or free-form guessing
- Output focuses on:
  - explanation
  - trade-offs
  - uncertainty
  - business reasoning

The LLM acts as a **business analyst**, not a predictor.

---

## 6. System Architecture

### 6.1 High-Level Architecture

[ Open Data Sources ]
↓
[ Ingestion & Normalization ]
↓
[ Industry Classification ]
↓
[ Competition & Density Metrics ]
↓
[ Reputation & Price Signals ]
↓
[ Insight Assembly ]
↓
[ RAG + LLM Explanation ]
↓
[ API / UI ]


---

### 6.2 Backend Stack

- Language: Python 3.11
- API Framework: FastAPI
- Core Data Sources:
  - OpenStreetMap (POIs, roads, land use)
  - Overpass API
  - Public population and urban datasets
- Enrichment Sources (optional, compliant):
  - Wikidata
  - Open city and tourism datasets
- Database (planned):
  - SQLite (development)
  - PostgreSQL + PostGIS (scaling)
- LLM Usage:
  - Explanation and synthesis only
  - Never treated as a factual source

---

## 7. Data, Compliance & Risk Mitigation

### 7.1 Explicit Non-Goals (Important)

LocatorisLLM explicitly does NOT:
- scrape Google Maps, Yelp, TripAdvisor, or similar platforms
- store or redistribute proprietary reviews or prices
- track individuals or real-time personal movement
- provide financial, legal, or investment advice

---

### 7.2 Compliance & Risk Mitigation

| Risk | Mitigation |
|----|-----------|
| Licensing violations | Use OSM-compatible licenses with attribution |
| Platform ToS violations | No scraping of closed platforms |
| Privacy exposure | Aggregate-only analysis |
| Overconfidence | Confidence bands and assumption disclosure |
| LLM hallucination | RAG constrained to internal analytics |

---

## 8. Success Criteria

- Insights feel intuitive to domain experts
- Reasoning is transparent and explainable
- System remains usable without paid data
- Architecture supports future licensed upgrades
- Clear differentiation from map-only tools

---

## 9. Roadmap Summary

- Phase 2: Ontology & classification ✅
- Phase 3: Competition & gap analysis
- Phase 4: Reputation & price signals
- Phase 5: Temporal & behavioral modeling
- Phase 6: RAG-based explanation
- Phase 7: UI, user accounts, tiered access
