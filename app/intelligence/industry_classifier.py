"""
Industry classification logic for LocatorisLLM.

This module converts raw map tags into canonical
industry and sub-industry labels using the registry.

Design goals:
• Deterministic
• Explainable
• Safe with incomplete data
"""

from app.intelligence.industry_registry import INDUSTRY_REGISTRY


def classify_business(tags: dict) -> dict:
    """
    Classify a place using raw map-style tags.

    Parameters
    ----------
    tags : dict
        Example:
        {
            "amenity": "restaurant",
            "name": "ABC Cafe"
        }

    Returns
    -------
    dict
        {
            "industry": str | None,
            "sub_industry": str | None
        }
    """

    # Defensive: missing or empty tags
    if not tags:
        return {"industry": None, "sub_industry": None}

    # Iterate through ontology
    for industry, tag_groups in INDUSTRY_REGISTRY.items():
        for tag_key, value_map in tag_groups.items():
            raw_value = tags.get(tag_key)

            if raw_value in value_map:
                return {
                    "industry": industry,
                    "sub_industry": value_map[raw_value]
                }

    # Unknown / unsupported business
    return {"industry": None, "sub_industry": None}
