"""
phase3_engine.py

Phase 3 orchestration layer.

This module:
- Combines raw competition pressure
- Adds anchor-driven demand amplification
- Normalizes results for human interpretation

IMPORTANT CONCEPT:
- Raw scores are unbounded and precise (machine-facing)
- Normalized scores are bounded and interpretable (human-facing)
"""

import math

from app.metrics.competition import effective_competition
from app.metrics.anchors import anchor_influence_score
from app.metrics.industry_weights import get_density_tolerance


def normalize_score(raw_score: float) -> float:
    """
    Normalize an unbounded competition score using log scaling.

    Why log scaling:
    - Preserves ordering (higher stays higher)
    - Compresses extreme values
    - Matches human perception of saturation
    - Prevents dense urban areas from dominating everything

    Formula:
        log(1 + raw_score)

    Returns:
    - normalized score (human-scale)
    """
    return round(math.log1p(raw_score), 3)


def classify_density(normalized_score: float) -> str:
    """
    Convert normalized score into qualitative density labels.

    These thresholds are deliberately coarse to avoid false precision.
    """
    if normalized_score < 1.2:
        return "low"
    if normalized_score < 3.0:
        return "medium"
    return "high"


def phase3_analyze(payload: dict) -> dict:
    """
    Main Phase 3 analysis function.

    Produces:
    - raw analytical signals (machine-facing)
    - normalized signals (human & LLM-facing)

    This function does NOT provide advice.
    It produces structured inputs for later reasoning layers.
    """

    # -------------------------------
    # Extract inputs
    # -------------------------------
    target = payload["target"]
    competitors = payload.get("competitors", [])
    anchors = payload.get("anchors", [])
    industry = payload.get("industry", "default")

    # -------------------------------
    # Step 1: Raw competition pressure
    # -------------------------------
    raw_competition = effective_competition(
        target,
        competitors
    )

    # -------------------------------
    # Step 2: Anchor-driven amplification
    # -------------------------------
    anchor_score = anchor_influence_score(
        target,
        anchors
    )

    # -------------------------------
    # Step 3: Industry normalization
    # -------------------------------
    tolerance = get_density_tolerance(industry)

    raw_effective_score = round(
        (raw_competition + anchor_score) / tolerance,
        3
    )

    # -------------------------------
    # Step 4: Human-scale normalization
    # -------------------------------
    normalized_score = normalize_score(raw_effective_score)

    # -------------------------------
    # Step 5: Density classification
    # -------------------------------
    density_label = classify_density(normalized_score)

    # -------------------------------
    # Step 6: Competitive advantage vectors
    # -------------------------------
    advantage_vectors = {
        # Indicates whether competitors derive strength mainly from anchors
        "anchor_dependence": "high"
        if anchor_score > raw_competition
        else "medium",

        # Indicates whether competition is spatially concentrated
        "centralization": "high"
        if raw_competition > 2.5
        else "low",

        # Dense environments favor mobile or flexible formats
        "mobility_opportunity": "high"
        if density_label == "high"
        else "medium",
    }

    # -------------------------------
    # Final Phase 3 output
    # -------------------------------
    return {
        # Raw metrics (machine-facing, precise)
        "raw_competition_score": raw_effective_score,

        # Normalized metrics (human & LLM-facing)
        "normalized_competition_score": normalized_score,
        "density_label": density_label,

        # Structural signals
        "competitor_count": len(competitors),
        "dominant_competitor_present": raw_effective_score > 4.5,
        "competition_pattern": (
            "anchor_clustered"
            if anchor_score > raw_competition
            else "distributed"
        ),

        # Strategic input vectors (NOT advice)
        "advantage_vectors": advantage_vectors,
    }
