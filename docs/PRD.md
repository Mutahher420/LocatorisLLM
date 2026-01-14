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
analytics, and structured reasoning to produce defensible insights, not scraped
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

1. **Map-First Exploration**  
   Users may freely explore geographic areas on a map to understand existing
   business presence, clustering, and contextual activity.

2. **Chat-First Analysis**  
   Users may directly ask natural-language questions (e.g., “Is this a good area
   for a mid-range café?”). The system interprets intent and triggers the
   relevant analytical pipelines.

3. **Dashboard-on-Demand**  
   When deeper insights are requested, LocatorisLLM generates structured
   analytics (charts, metrics, comparisons) associated with the user’s query.

Users may switch freely between map exploration and conversational analysis at
any point.

---

## 4. Core Design Principles

1. **Compliance-first**  
   - No scraping of closed platforms (e.g., Google Maps, Yelp, TripAdvisor)  
   - Only open or permissively licensed data sources are used

2. **Explainability over certainty**  
   - All insights are reasoned, not asserted  
   - Assumptions and uncertainty are made explicit

3. **Business behavior over raw data**  
   - Industries are defined by economic behavior, not tag families  
   - Signals are interpreted contextually

4. **Global by default**  
   - Core functionality works anywhere OpenStreetMap coverage exists  
   - No country-specific hardcoding required

5. **Unit and language independence**  
   - All internal calculations use metric units  
   - Presentation supports metric and imperial systems  
   - Analytics are language-agnostic by design

6. **Upgradeable architecture**  
   - Licensed or paid datasets can be added later without redesign

---

## 5. Product Scope & Phases

### Phase 0 — Foundations & Governance (Completed)

- Product vision and non-goals
- Compliance-first data policy
- Phase-based architecture and acceptance criteria
- Versioned PRD and documentation discipline

---

### Phase 1 — Data Ingestion & Normalization (Completed)

- Approved open data sources (OSM and similar)
- Ingestion of business, anchor, and contextual entities
- Separation of raw data from normalized analytical representations
- Documented coverage gaps and data limitations

---

### Phase 2 — Business Ontology & Classification (Completed)

- Canonical industry and sub-industry registry
- Deterministic classification from map-based tags
- Explicit separation between raw data namespaces (e.g., `tourism=*`) and
  economic roles (e.g., hospitality vs culture)
- Coverage across healthcare, food, retail, education, tourism, recreation,
  professional services, and informal economy

---

### Phase 3 — Competition & Density Analysis (Completed)

Phase 3 models the **competitive terrain** of a location in an objective and
explainable way. It does not provide business advice, but produces structured
signals that later phases reason over.

Key capabilities include:

- Distance-weighted competition analysis (metric internally)
- Industry-normalized density tolerance
- Anchor-weighted competitor influence  
  (e.g., hospitals, offices, educational institutions, recreation)
- Explicit distinction between:
  - **baseline population density**, and
  - **demand anchors**, which amplify demand beyond population alone
- Effective competition scoring (beyond raw counts)
- Detection of spatial patterns (clustered, dispersed, corridor-based)
- Identification of dominant competitors and competitive imbalance
- Generation of **competitive advantage vectors**, describing where competitors
  derive strength (e.g., anchor proximity, centrality, clustering)

Phase 3 outputs are deterministic, comparable across locations, and explicitly
designed to **enable strategic reasoning** in later phases without embedding
prescriptive judgment.

---

### Phase 4 — Reputation & Price Signal Modeling (Planned)

LocatorisLLM does not collect or store consumer reviews or actual prices.
Instead, it models per-business **inferred signals** that approximate reputation
and price positioning.

These signals are analytical proxies, not observed consumer ratings or prices.

#### Reputation Signal Examples
- Business longevity and survival density
- Brand vs independent presence
- Proximity to demand anchors
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

### Phase 5 — Temporal & Behavioral Analysis (Planned)

- Time-of-day and day-of-week demand proxies
- Recreation, tourism, and event spillover effects
- Adaptive time windows inferred from data, not hardcoded
- Mobility-aware reasoning for mobile businesses

---

### Phase 6 — Reasoning & Explanation Layer (Planned)

This phase introduces structured reasoning over analytical outputs.

Key properties:

- The reasoning layer receives **only internal analytics**, not raw data
- It may use LLMs, rule-based systems, or hybrids (to be researched)
- No external browsing or uncontrolled generation
- Multilingual explanation support
- Focus on:
  - explanation
  - trade-offs
  - uncertainty
  - strategic alternatives

The reasoning layer **does not replace analytical computation** and does not
override deterministic metrics from earlier phases.

---

### Phase 7 — Dashboards & Projects (Planned)

- On-demand analytics dashboards
- Visualization of metrics and comparisons
- Project-based saving of in-depth analyses

---

### Phase 8 — User Accounts & Access (Planned)

- Email-based authentication
- Device trust and session management (future)
- Tiered access to advanced features (future)

---

## 6. Example Insights (Illustrative)

For a user exploring a café concept in a specific urban area, LocatorisLLM may
surface insights such as:

- Food & beverage businesses are within expected density, but cafés are
  underrepresented near office and recreation anchors.
- One dominant competitor captures most anchor-driven demand, while peripheral
  areas show lower effective competition.
- Competitive advantage vectors suggest differentiation through format,
  mobility, or pricing rather than direct substitution.

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
[ Temporal & Behavioral Modeling ]
↓
[ Reasoning & Explanation Layer ]
↓
[ API / UI ]


---

## 8. Data, Compliance & Risk Mitigation

### 8.1 Explicit Non-Goals

LocatorisLLM explicitly does NOT:
- scrape Google Maps, Yelp, TripAdvisor, or similar platforms
- store or redistribute proprietary reviews or prices
- track individuals or personal real-time movement
- provide financial, legal, or investment advice

---

## 9. Success Metrics

- Median analysis response time under defined load
- Coverage completeness for mapped business categories
- Stability of competition signals under small input changes
- User-reported agreement with insights
- Clarity of explanations across languages

---

## 10. Why Now

- Proprietary location data is increasingly restricted and expensive
- AI tools are widespread but often opaque and unexplainable
- Entrepreneurs seek decision support, not raw data
- Open geographic data has reached sufficient maturity for analysis

---

## 11. Roadmap Summary

- Phase 0: Foundations & governance ✅  
- Phase 1: Data ingestion & normalization ✅  
- Phase 2: Ontology & classification ✅  
- Phase 3: Competition & density analysis ✅  
- Phase 4: Reputation & price signals  
- Phase 5: Temporal & behavioral modeling  
- Phase 6: Reasoning & explanation layer  
- Phase 7: Dashboards & projects  
- Phase 8: User accounts & tiered access  

---

### End of PRD
