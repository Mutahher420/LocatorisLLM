"""
main.py

This is the main entry point for the LocatorisLLM backend.

Responsibilities of this file:
- Initialize the FastAPI application
- Expose API endpoints for each completed phase
- Act as a thin orchestration layer (NO business logic here)

Business logic lives in:
- app/intelligence/  -> classification, reasoning
- app/metrics/       -> competition, density, signals
"""

from fastapi import FastAPI

# -------------------------------
# Phase 2 imports (Business ontology & classification)
# -------------------------------
from app.intelligence.industry_classifier import classify_business

# -------------------------------
# Phase 3 imports (Competition & density analysis)
# -------------------------------
from app.metrics.phase3_engine import phase3_analyze


# -------------------------------
# FastAPI app initialization
# -------------------------------

# Create the FastAPI application instance
# Title appears in Swagger UI
app = FastAPI(title="LocatorisLLM")


# -------------------------------
# Health check endpoint
# -------------------------------

@app.get("/health")
def health():
    """
    Health check endpoint.

    Purpose:
    - Verify that the API is running
    - Used by developers, monitoring tools, or deployment checks

    Returns:
    - Simple status message
    """
    return {"status": "ok"}


# -------------------------------
# Phase 2: Industry classification endpoint
# -------------------------------

@app.post("/classify")
def classify(tags: dict):
    """
    Classify a business based on OpenStreetMap-style tags.

    This endpoint belongs to Phase 2.

    Input:
    - tags: dictionary of key/value pairs
      Example:
      {
        "amenity": "cafe",
        "cuisine": "coffee_shop"
      }

    Output:
    - canonical industry
    - sub-industry
    - confidence / metadata (as defined in classifier)

    Note:
    - This endpoint does NOT perform any competition analysis.
    """
    return classify_business(tags)


# -------------------------------
# Phase 3: Competition & density analysis endpoint
# -------------------------------

@app.post("/phase3/competition")
def phase3_competition(payload: dict):
    """
    Perform Phase 3 competition & density analysis.

    This endpoint evaluates the competitive terrain around a location.

    Input payload structure:
    {
        "target": { "lat": float, "lon": float },
        "industry": "cafe",
        "competitors": [
            { "lat": float, "lon": float },
            ...
        ],
        "anchors": [
            { "type": "hospital", "lat": float, "lon": float },
            { "type": "office", "lat": float, "lon": float }
        ]
    }

    Output:
    - effective competition score
    - density label (low / medium / high)
    - presence of dominant competitors
    - spatial competition pattern
    - competitive advantage vectors

    Important:
    - This endpoint produces SIGNALS, not business advice.
    - Strategy is handled later by the LLM reasoning layer (Phase 6).
    """
    return phase3_analyze(payload)
