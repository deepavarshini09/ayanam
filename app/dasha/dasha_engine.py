# Vimshottari Dasha Engine (Core Version)

NAKSHATRA_LORDS = {
    "Ashwini": "Ketu",
    "Bharani": "Venus",
    "Krittika": "Sun",
    "Rohini": "Moon",
    "Mrigashira": "Mars",
    "Ardra": "Rahu",
    "Punarvasu": "Jupiter",
    "Pushya": "Saturn",
    "Ashlesha": "Mercury",
    "Magha": "Ketu",
    "Purva Phalguni": "Venus",
    "Uttara Phalguni": "Sun",
    "Hasta": "Moon",
    "Chitra": "Mars",
    "Swati": "Rahu",
    "Vishakha": "Jupiter",
    "Anuradha": "Saturn",
    "Jyeshtha": "Mercury",
    "Mula": "Ketu",
    "Purva Ashadha": "Venus",
    "Uttara Ashadha": "Sun",
    "Shravana": "Moon",
    "Dhanishta": "Mars",
    "Shatabhisha": "Rahu",
    "Purva Bhadrapada": "Jupiter",
    "Uttara Bhadrapada": "Saturn",
    "Revati": "Mercury"
}

DASHA_YEARS = {
    "Ketu": 7,
    "Venus": 20,
    "Sun": 6,
    "Moon": 10,
    "Mars": 7,
    "Rahu": 18,
    "Jupiter": 16,
    "Saturn": 19,
    "Mercury": 17
}

DASHA_SEQUENCE = [
    "Ketu",
    "Venus",
    "Sun",
    "Moon",
    "Mars",
    "Rahu",
    "Jupiter",
    "Saturn",
    "Mercury"
]


def get_starting_dasha(nakshatra: str):
    """
    Returns starting Mahadasha lord based on Moon's Nakshatra
    """
    return NAKSHATRA_LORDS.get(nakshatra)


def get_dasha_sequence(start_lord: str):
    """
    Rotates sequence from starting planet
    """
    idx = DASHA_SEQUENCE.index(start_lord)
    return DASHA_SEQUENCE[idx:] + DASHA_SEQUENCE[:idx]


def generate_dasha_table(nakshatra: str):
    """
    Simple full 120-year dasha timeline (basic version)
    """
    start_lord = get_starting_dasha(nakshatra)
    sequence = get_dasha_sequence(start_lord)

    timeline = []
    current_year = 0

    for planet in sequence:
        years = DASHA_YEARS[planet]

        timeline.append({
            "planet": planet,
            "start": current_year,
            "end": current_year + years
        })

        current_year += years

    return timeline


def print_dasha(timeline):
    print("\n🪐 VIMSHOTTARI DASHA TIMELINE\n")

    for d in timeline:
        print(f"{d['planet']}: {d['start']} - {d['end']} years")