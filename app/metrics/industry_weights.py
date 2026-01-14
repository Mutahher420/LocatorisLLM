"""
industry_weights.py

This file defines how tolerant different industries are to competition density.

Why this exists:
- Not all businesses behave the same under competition.
- Cafés can exist densely.
- Clinics, hospitals, and specialized services cannot.

These weights are NOT opinions.
They are normalization factors that allow fair comparison across industries.

Lower tolerance value  => industry tolerates more competitors
Higher tolerance value => industry saturates faster
"""

# Dictionary mapping industry → density tolerance factor
# These values are intentionally simple and explainable.
INDUSTRY_DENSITY_TOLERANCE = {
    "cafe": 0.7,
    "restaurant": 0.8,
    "clinic": 1.5,
    "hospital": 2.0,
    "pharmacy": 1.2,
    "retail": 1.0,
    "grocery": 0.9,

    # Default ensures unknown industries still work
    "default": 1.0,
}


def get_density_tolerance(industry: str) -> float:
    """
    Returns the density tolerance factor for a given industry.

    Why this function exists:
    - Centralizes industry behavior logic
    - Prevents hardcoding values throughout the codebase
    - Makes future tuning easy and safe

    Parameters:
    - industry: canonical industry name (string)

    Returns:
    - float representing tolerance multiplier
    """
    return INDUSTRY_DENSITY_TOLERANCE.get(
        industry,
        INDUSTRY_DENSITY_TOLERANCE["default"]
    )
