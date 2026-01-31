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

LocatorisLLM is designed as a deterministic-first system. All analytical metrics,
scores, classifications, and signals are computed using explicit algorithms
before any reasoning or explanation occurs. Interpretive components operate only
on finalized analytical outputs.

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

All questions addressed by LocatorisLLM are treated as structural analysis
problems. The system evaluates spatial distribution, density, proximity, and
contextual relationships rather than attempting to forecast outcomes, revenue,
or success.

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

LocatorisLLM supports a spectrum of user sophistication. All users access the
same analytical foundation; differences in experience are limited to the depth
and framing of explanations.

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

Conversational interaction may be presented through an assistant-style interface
to improve approachability. This assistant acts solely as a presentation and
explanation layer and does not introduce new analytical capabilities.

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

Compliance is enforced structurally through architectural constraints. The system
is incapable of ingesting proprietary data sources or emitting legal, financial,
or investment advice.

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

Distance-based influence is modeled using continuous decay functions rather than
binary radii. Anchor influence varies by industry and reflects demand
amplification rather than guaranteed patronage. Density tolerance normalizes
competitive pressure based on industry-specific operating characteristics.

---

### Phase 4 — Reputation & Price Signal Modeling (Planned)

LocatorisLLM does not collect or store consumer reviews or actual prices.
Instead, it models per-business **inferred signals** that approximate reputation
and price positioning.

These signals are analytical proxies, not observed consumer ratings or prices.

Reputation and price are inferred structurally using contextual stability,
business mix, longevity patterns, and anchor proximity. Signals are combined into
confidence-weighted assessments rather than absolute scores.

---

### Phase 5 — Temporal & Behavioral Analysis (Planned)

- Time-of-day and day-of-week demand proxies
- Recreation, tourism, and event spillover effects
- Adaptive time windows inferred from data, not hardcoded
- Mobility-aware reasoning for mobile businesses

Temporal demand is inferred from contextual activity distributions and land-use
patterns rather than explicit footfall or real-time tracking.

---

### Phase 6 — Reasoning & Explanation Layer (Planned)

This phase introduces structured reasoning over analytical outputs.

The reasoning layer is explicitly designed as an interpretive system. It does not
compute metrics, retrieve data, rank options, optimize outcomes, or make
predictions.

Key properties:

- The reasoning layer receives only finalized internal analytics
- Reasoning operates on a frozen analytical snapshot
- No external browsing, scraping, or uncontrolled generation
- Multilingual explanation support
- Focus on explanation, trade-offs, uncertainty, and structural comparison

The reasoning layer may compare strategic formats (e.g., mobile vs fixed),
positioning bands, or temporal focus only in terms of relative structural
alignment with observed signals.

The reasoning layer must refuse to answer when analytical coverage is
insufficient, signals are irreconcilably conflicting, or a question exceeds
system scope.

Reasoning may support controlled counterfactuals involving a single hypothetical
change (e.g., time window or business category). Counterfactuals must be clearly
labeled, non-stacked, and grounded in existing analytics.

---

### Phase 7 — Dashboards & Projects (Planned)

- On-demand analytics dashboards
- Visualization of metrics and comparisons
- Project-based saving of in-depth analyses

Dashboards display metrics and indicators but do not contain interpretation.
Interpretation is exclusively provided through the reasoning layer.

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

Insights are presented with context, uncertainty, and structural framing, not as
guarantees.

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

The system architecture enforces strict separation of concerns. Analytical layers
compute structure, the reasoning layer interprets structure, and presentation
layers render results.

---

## 8. Data, Compliance & Risk Mitigation

### 8.1 Explicit Non-Goals

LocatorisLLM explicitly does NOT:
- scrape Google Maps, Yelp, TripAdvisor, or similar platforms
- store or redistribute proprietary reviews or prices
- track individuals or personal real-time movement
- provide financial, legal, or investment advice

Legal and regulatory knowledge is treated as contextual constraints rather than
advice. Jurisdiction-specific rules may be referenced to explain feasibility
boundaries but never to prescribe compliance actions.

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
