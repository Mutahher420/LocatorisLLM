"""
LocatorisLLM – Canonical Industry & Sub-Industry Registry (Phase 2)

This file defines WHAT kinds of businesses and activity locations exist.

IMPORTANT CONCEPTS
------------------
• Raw map tags (amenity=*, tourism=*, shop=*) are DATA SOURCES
• Industries represent ECONOMIC BEHAVIOR
• A single tag family (e.g. tourism=*) may map to different industries
• This file contains DATA ONLY — no logic

This registry is the single source of truth for classification.
"""

INDUSTRY_REGISTRY = {

    # ==================================================
    # HEALTHCARE & LIFE SCIENCES
    # ==================================================
    "Healthcare": {
        "healthcare": {
            "hospital": "Hospital",
            "clinic": "Clinic",
            "doctors": "Clinic",
            "dentist": "Dental Clinic",
            "laboratory": "Diagnostics Lab",
            "imaging": "Imaging Center",
            "pharmacy": "Pharmacy",
            "physiotherapy": "Physiotherapy Center",
            "mental_health": "Mental Health Clinic",
            "veterinary": "Veterinary Clinic",
            "nursing_home": "Nursing Home",
        }
    },

    # ==================================================
    # FOOD, BEVERAGE & NIGHT ECONOMY
    # ==================================================
    "Food & Beverage": {
        "amenity": {
            "restaurant": "Restaurant",
            "cafe": "Cafe",
            "fast_food": "Fast Food",
            "food_court": "Food Court",
            "bar": "Bar",
            "nightclub": "Nightclub",
            "ice_cream": "Ice Cream Shop",
            "juice_bar": "Juice Bar",
        },
        "vendor": {
            "mobile_food": "Mobile Food Vendor"
        }
    },

    # ==================================================
    # RETAIL & COMMERCIAL
    # ==================================================
    "Retail": {
        "shop": {
            "supermarket": "Supermarket",
            "convenience": "Convenience Store",
            "grocery": "Grocery Store",
            "clothes": "Clothing Store",
            "shoes": "Footwear Store",
            "electronics": "Electronics Store",
            "mobile_phone": "Mobile Phone Store",
            "furniture": "Furniture Store",
            "hardware": "Hardware Store",
            "cosmetics": "Cosmetics Store",
            "jewelry": "Jewelry Store",
            "books": "Bookstore",
            "florist": "Florist",
            "pet": "Pet Shop",
            "optician": "Optical Store",
        }
    },

    # ==================================================
    # EDUCATION & KNOWLEDGE (FULL SPECTRUM)
    # ==================================================
    "Education": {
        "amenity": {
            "kindergarten": "Preschool / Kindergarten",
            "school": "School",
            "college": "College",
            "university": "University",
            "library": "Library",
            "training": "Training Institute",
            "language_school": "Language Institute",
            "driving_school": "Driving School",
            "research_institute": "Research Institute",
        }
    },

    # ==================================================
    # FINANCE, LEGAL & PROFESSIONAL SERVICES
    # ==================================================
    "Professional Services": {
        "amenity": {
            "bank": "Bank",
            "atm": "ATM",
        },
        "office": {
            "insurance": "Insurance Office",
            "lawyer": "Law Firm",
            "accountant": "Accounting Firm",
            "consulting": "Consulting Firm",
            "real_estate": "Real Estate Agency",
        }
    },

    # ==================================================
    # HOSPITALITY & ACCOMMODATION
    # ==================================================
    "Hospitality": {
        "tourism": {
            "hotel": "Hotel",
            "hostel": "Hostel",
            "guest_house": "Guest House",
            "resort": "Resort",
            "motel": "Motel",
        }
    },

    # ==================================================
    # CULTURE, HERITAGE & TOURISM ANCHORS
    # ==================================================
    "Culture & Tourism": {
        "tourism": {
            "museum": "Museum",
            "attraction": "Tourist Attraction",
            "gallery": "Art Gallery",
            "exhibition": "Exhibition Hall",
        },
        "historic": {
            "monument": "Monument",
            "memorial": "Memorial",
            "heritage": "Heritage Site",
        },
        "amenity": {
            "arts_centre": "Cultural Center",
            "theatre": "Theatre",
        }
    },

    # ==================================================
    # ENTERTAINMENT, RECREATION & SPORTS
    # ==================================================
    "Entertainment & Recreation": {
        "leisure": {
            "park": "Park",
            "playground": "Playground",
            "cinema": "Cinema",
            "gym": "Gym",
            "sports_centre": "Sports Facility",
            "pitch": "Sports Pitch",
            "swimming_pool": "Swimming Pool",
        },
        "sport": {
            "football": "Football Ground",
            "futsal": "Futsal Court",
            "basketball": "Basketball Court",
            "tennis": "Tennis Court",
            "padel": "Padel Court",
            "cricket": "Cricket Ground",
        }
    },

    # ==================================================
    # PERSONAL & LIFESTYLE SERVICES
    # ==================================================
    "Personal Services": {
        "shop": {
            "hairdresser": "Salon / Barber",
            "beauty": "Beauty Services",
            "laundry": "Laundry / Dry Cleaning",
            "tailor": "Tailor",
            "tattoo": "Tattoo Studio",
        }
    },

    # ==================================================
    # AUTOMOTIVE & MOBILITY SERVICES
    # ==================================================
    "Automotive": {
        "amenity": {
            "fuel": "Fuel Station",
            "charging_station": "EV Charging Station",
            "parking": "Parking Facility",
        },
        "shop": {
            "car_repair": "Auto Repair",
            "tyres": "Tire Shop",
            "car_wash": "Car Wash",
        }
    },

    # ==================================================
    # PUBLIC & GOVERNMENT SERVICES
    # ==================================================
    "Public Services": {
        "amenity": {
            "police": "Police Station",
            "fire_station": "Fire Station",
            "post_office": "Post Office",
            "court": "Court",
            "townhall": "Government Office",
        }
    },

    # ==================================================
    # MARKETS & INFORMAL ECONOMY
    # ==================================================
    "Markets & Informal Economy": {
        "amenity": {
            "marketplace": "Market",
        },
        "shop": {
            "kiosk": "Kiosk",
            "street_vendor": "Street Vendor",
        }
    },

    # ==================================================
    # MIXED-USE & COMMERCIAL ANCHORS
    # ==================================================
    "Mixed-Use & Anchors": {
        "building": {
            "mall": "Shopping Mall",
            "commercial": "Commercial Complex",
            "office": "Office Complex",
        }
    },
}
