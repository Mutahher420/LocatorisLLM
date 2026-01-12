# LocatorisLLM — Product Requirements Document (PRD)

## 1. Overview

LocatorisLLM is a global, location-based business intelligence platform designed to
help people generate business ideas and evaluate where and how to start a
business.

The product serves users who:
- are exploring potential business ideas, and
- are ready to start a business but need clarity on location choice and price
  positioning.

LocatorisLLM does not make predictions or guarantees. Instead, it provides
structured analysis and explainable reasoning to support informed,
context-aware decision-making.

The system is built entirely on compliant, open, and legally redistributable
data sources, with an architecture that supports future upgrades to licensed
data without redesign.

---

## 2. Problem Statement

People deciding where and how to start a business struggle to answer questions
such as:

- Is this area already saturated for my idea?
- What type of business is missing here?
- Should I target a budget, mid-range, or premium price point?
- Would a mobile business perform better than a fixed location?
- Does surrounding activity support sustained demand?

Existing tools either:
- show raw map data without interpretation, or
- rely on closed, expensive, or legally restrictive datasets.

LocatorisLLM addresses this gap by combining open geographic data, deterministic
analytics, and LLM-based explanation to produce defensible insights, not scraped
opinions or opaque scores.

---

## 3. Target Users

### Primary Users
- Individuals generating business ideas
- Early-stage entrepreneurs evaluating where and how to launch
- Small business owners assessing expansion or relocation

### Secondary Users
- Mobile vendors (food trucks, pop-ups, temporary stalls)
- Consultants and market researchers
- Urban and regional planners (exploratory use)

The system is designed so that:
- casual users can explore freely and intuitively, and
- advanced users can request deeper analytical insight when needed.

---

## 3.1 User Interaction Model

LocatorisLLM supports multiple interaction paths to accommodate different user
intent and experience levels:

1. Map-First Exploration  
   Users may freely explore geographic areas on a map to understand existing
   business presence, clustering, and contextual activity.

2. Chat-First Analysis  
   Users may directly ask natural-language questions (e.g., “Is this a good area
   for a mid-range café?”). The system interprets intent and triggers the
   relevant analytical pipelines.

3. Dashboard-on-Demand  
   When deeper insights are requested, LocatorisLLM generates structured
   analytics (charts, metrics, comparisons) associated with the user’s query.

Users may switch freely between map exploration and conversational analysis at
any point.

---

## 4. Core Design Principles

1. Compliance-first  
   - No scraping of closed platforms (e.g., Google Maps, Yelp, TripAdvisor)  
   - Only open or permissively licensed data sources are used

2. Explainability over certainty  
   - All insights are reasoned, not asserted  
   - Assumptions and uncertainty are made explicit

3. Business behavior over raw data  
   - Industries are defined by economic behavior, not tag families  
   - Signals are interpreted contextually

4. Global by default  
   - Core functionality works anywhere OpenStreetMap coverage exists  
   - No country-specific hardcoding required

5. Upgradeable architecture  
   - Licensed or paid datasets can be added later without redesign

---

## 5. Product Scope & Phases

### Phase 2 — Business Ontology & Classification (Completed)

- Canonical industry and sub-industry registry
- Deterministic classification from map-based tags
- Explicit separation between raw data namespaces (e.g., tourism=*) and
  economic roles (e.g., hospitality vs culture)
- Coverage across healthcare, food, retail, education, tourism, recreation,
  professional services, and informal economy

---

### Phase 3 — Competition & Density Analysis

- Distance-weighted competitor analysis
- Business clustering and saturation metrics
- Identification of underserved industries and sub-industries
- Support for both fixed-location and mobile businesses

---

### Phase 4 — Reputation & Price Signal Modeling

LocatorisLLM does not collect or store consumer reviews or actual prices.
Instead, it models per-business probabilistic signals that approximate reputation
and price positioning.

These signals are inferred analytics, not observed consumer ratings or prices.

#### Reputation Signal Examples
- Business longevity and survival density
- Brand vs independent presence
- Proximity to demand anchors (tourism, offices, transit)
- Opening-hours intensity
- Stability of similar businesses in the surrounding area

#### Price Position Signal Examples
- Surrounding business mix (utility vs premium)
- Land-use and zoning context
- Proximity to premium or budget anchors
- Industry-specific pricing norms

Signals are combined into confidence-weighted assessments rather than absolute
scores.

---

### Phase 5 — Temporal & Behavioral Analysis

- Time-of-day and day-of-week demand proxies
- Recreation, tourism, and event spillover effects
- Adaptive time windows inferred from data, not hardcoded
- Mobility-aware reasoning for mobile businesses

---

### Phase 6 — LLM Reasoning Layer (RAG)

- Retrieval-Augmented Generation (RAG)
- LLM receives only structured internal analytics
- No external browsing or uncontrolled generation
- Output focuses on explanation, trade-offs, uncertainty, and business reasoning

The LLM acts as a business analyst, not a predictor or oracle.

---

## 6. Example Insights (Illustrative)

For a user exploring a café concept in a specific urban area, LocatorisLLM may
surface insights such as:

- Food & beverage businesses are moderately saturated, but cafés are
  underrepresented relative to nearby offices and recreation.
- The surrounding area supports mid-range pricing, with limited premium
  competition.
- Evening demand is stronger than morning demand due to nearby leisure
  activities.
- A mobile or hybrid setup may reduce initial risk due to variable foot traffic.

Insights are presented with context and confidence, not as guarantees.

---

## 6.1 Projects & Saved Analyses

LocatorisLLM treats each in-depth analysis as a discrete project, which may
include:
- the original query
- assumptions and parameters
- generated metrics and charts
- explanatory insights

Projects allow users to revisit, refine, and compare analyses over time.

While saving and managing projects may be gated behind paid tiers in the future,
this functionality is designed and built into the system from the start.

---

## 7. System Architecture

### 7.1 High-Level Architecture

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

### 7.2 Backend Stack

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

## 8. Data, Compliance & Risk Mitigation

### 8.1 Explicit Non-Goals

LocatorisLLM explicitly does NOT:
- scrape Google Maps, Yelp, TripAdvisor, or similar platforms
- store or redistribute proprietary reviews or prices
- track individuals or personal real-time movement
- provide financial, legal, or investment advice

---

### 8.2 Compliance & Risk Mitigation

| Risk | Mitigation |
|---|---|
| Licensing violations | Use OSM-compatible licenses with attribution |
| Platform ToS violations | No scraping of closed platforms |
| Privacy exposure | Aggregate-only analysis |
| Overconfidence | Confidence bands and assumption disclosure |
| LLM hallucination | RAG constrained to internal analytics |

---

## 9. Success Metrics

- Median analysis response time under defined load
- Coverage completeness for mapped business categories
- User-reported agreement with insights
- Stability of recommendations under small input changes
- Clarity of explanations for non-technical users

---

## 10. Why Now

- Proprietary location data is increasingly restricted and expensive
- AI tools are widespread but often opaque and unexplainable
- Entrepreneurs seek decision support, not raw data
- Open geographic data has reached sufficient maturity for analysis

---

## 11. Roadmap Summary

- Phase 2: Ontology & classification ✅
- Phase 3: Competition & gap analysis
- Phase 4: Reputation & price signals
- Phase 5: Temporal & behavioral modeling
- Phase 6: Chat-based interface with RAG
- Phase 7: Dashboard generation & projects
- Phase 8: User accounts, saving, tiered access
