# app/core/aspect_engine.py

"""
Graha Drishti (Planetary Aspects) — Jyotish / Vedic system

Every planet aspects the 7th house from itself (opposition, 180°).
Special additional aspects:
  Mars    → 4th and 8th houses from itself
  Jupiter → 5th and 9th houses from itself
  Saturn  → 3rd and 10th houses from itself
  Rahu    → 5th and 9th houses from itself (like Jupiter)
  Ketu    → 5th and 9th houses from itself (like Jupiter)

Rahu and Ketu special aspects are included per classical Tamil/
South Indian Jyotish tradition.
"""

# Houses each planet aspects IN ADDITION to the universal 7th
SPECIAL_ASPECTS = {
    "Mars":    [4, 8],
    "Jupiter": [5, 9],
    "Saturn":  [3, 10],
    "Rahu":    [5, 9],
    "Ketu":    [5, 9],
}


def get_house_of_planet(planet, house_map):
    """
    Returns the house number (1–12) a planet occupies.
    house_map: { house_number: [list of planet names] }
    """

    for house, planets in house_map.items():

        if planet in planets:
            return house

    return None


def get_aspected_houses(planet, house_map):
    """
    Returns a list of house numbers aspected by the given planet.
    Includes the universal 7th aspect + any special aspects.
    """

    own_house = get_house_of_planet(
        planet, house_map
    )

    if own_house is None:
        return []

    aspected = []

    # Universal 7th aspect (every planet)
    seventh = ((own_house - 1 + 6) % 12) + 1
    aspected.append(seventh)

    # Special aspects for certain planets
    extras = SPECIAL_ASPECTS.get(planet, [])

    for offset in extras:
        target = ((own_house - 1 + offset - 1) % 12) + 1
        aspected.append(target)

    return aspected


def get_all_aspects(house_map):
    """
    Returns a dict mapping each house to the list of planets
    that aspect it.

    Example output:
    {
        1: ["Jupiter", "Saturn"],
        4: ["Mars"],
        ...
    }
    """

    # Collect all planets from house_map
    all_planets = []

    for planets in house_map.values():
        all_planets.extend(planets)

    # Build aspect map
    aspect_map = {h: [] for h in range(1, 13)}

    for planet in all_planets:

        aspected_houses = get_aspected_houses(
            planet, house_map
        )

        for house in aspected_houses:
            aspect_map[house].append(planet)

    return aspect_map


def get_aspect_strength(house_map):
    """
    Returns aspect count per house — same shape as
    get_house_strength() so both can be combined easily.

    { 1: 2, 2: 0, 3: 1, ... }
    """

    aspect_map = get_all_aspects(house_map)

    return {
        house: len(planets)
        for house, planets in aspect_map.items()
    }


def print_aspects(house_map, house_meanings):
    """
    Prints which planets aspect which houses.
    """

    aspect_map = get_all_aspects(house_map)

    print("\n🔭 PLANETARY ASPECTS (Graha Drishti)\n")

    for house in range(1, 13):

        planets = aspect_map[house]

        if planets:
            aspectors = ", ".join(planets)
            print(
                f"House {house} aspected by: "
                f"{aspectors}"
            )
            print(
                f"   → {house_meanings[house]}\n"
            )