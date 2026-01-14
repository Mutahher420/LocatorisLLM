"""
competition.py

This module computes RAW COMPETITION PRESSURE.

It answers:
- How many competitors exist?
- How close are they?
- How strongly do they exert pressure?

This is intentionally simple and deterministic.
"""

from math import radians, sin, cos, sqrt, atan2


def haversine(lat1, lon1, lat2, lon2) -> float:
    """
    Computes geographic distance between two points.

    Returns:
    - distance in kilometers
    """
    R = 6371

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1))
        * cos(radians(lat2))
        * sin(dlon / 2) ** 2
    )

    return 2 * R * atan2(sqrt(a), sqrt(1 - a))


def effective_competition(target, competitors, radius_km=2.0) -> float:
    """
    Computes effective competition score.

    Logic:
    - Nearby competitors matter more
    - Pressure decays with distance
    - Uses inverse distance weighting

    Parameters:
    - target: location being evaluated
    - competitors: list of competitor locations
    - radius_km: max distance for relevance

    Returns:
    - numeric competition score
    """

    score = 0.0

    for comp in competitors:
        dist = haversine(
            target["lat"],
            target["lon"],
            comp["lat"],
            comp["lon"],
        )

        if dist <= radius_km:
            # Inverse distance weighting
            score += 1 / (dist + 0.1)

    return round(score, 3)
