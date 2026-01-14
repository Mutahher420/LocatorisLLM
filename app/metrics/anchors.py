"""
anchors.py

This module models DEMAND ANCHORS.

Anchors are NOT competitors.
They are places that amplify demand in an area.

Examples:
- Hospitals
- Offices
- Universities
- Recreation areas

A competitor near anchors is stronger than one in isolation.
"""

from math import radians, sin, cos, sqrt, atan2

# Each anchor type has a weight based on how strongly it drives footfall
ANCHOR_WEIGHTS = {
    "hospital": 1.6,
    "office": 1.4,
    "university": 1.5,
    "school": 1.3,
    "recreation": 1.2,
    "tourism": 1.4,

    # Fallback to prevent breakage
    "default": 1.0,
}


def haversine(lat1, lon1, lat2, lon2) -> float:
    """
    Calculates distance (in kilometers) between two geographic points.

    Uses the Haversine formula.
    Metric units are used internally for global consistency.

    Returns:
    - distance in kilometers
    """
    R = 6371  # Earth radius in kilometers

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1))
        * cos(radians(lat2))
        * sin(dlon / 2) ** 2
    )

    return 2 * R * atan2(sqrt(a), sqrt(1 - a))


def anchor_influence_score(target, anchors, radius_km=1.5) -> float:
    """
    Computes how strongly demand anchors influence a target location.

    Logic:
    - Nearby anchors matter more than distant ones
    - Stronger anchors have higher weights
    - Influence decays smoothly with distance

    This produces a numeric signal, NOT an opinion.

    Parameters:
    - target: dict with lat/lon
    - anchors: list of anchor dicts
    - radius_km: max distance anchors are considered relevant

    Returns:
    - float anchor influence score
    """

    score = 0.0

    # Iterate through all known anchors
    for anchor in anchors:

        # Distance between target and anchor
        dist = haversine(
            target["lat"],
            target["lon"],
            anchor["lat"],
            anchor["lon"],
        )

        # Ignore anchors beyond relevance radius
        if dist <= radius_km:

            # Get anchor type weight
            weight = ANCHOR_WEIGHTS.get(
                anchor["type"],
                ANCHOR_WEIGHTS["default"]
            )

            # Add weighted, distance-decayed influence
            score += weight / (dist + 0.1)

    return round(score, 3)
