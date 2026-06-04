SPECIAL_ASPECTS = {
    "Mars":    [4, 8],
    "Jupiter": [5, 9],
    "Saturn":  [3, 10],
    "Rahu":    [5, 9],
    "Ketu":    [5, 9],
}


def get_planet_names(house_map):
    """
    Extracts plain planet name strings from house_map
    which stores (planet, raasi) tuples.
    """

    names = []

    for entries in house_map.values():
        for entry in entries:
            # entry is (planet_name, raasi)
            names.append(entry[0])

    return names


def get_house_of_planet(planet, house_map):

    for house, entries in house_map.items():

        for entry in entries:

            if entry[0] == planet:
                return house

    return None


def get_aspected_houses(planet, house_map):

    own_house = get_house_of_planet(
        planet, house_map
    )

    if own_house is None:
        return []

    aspected = []

    seventh = ((own_house - 1 + 6) % 12) + 1
    aspected.append(seventh)

    extras = SPECIAL_ASPECTS.get(planet, [])

    for offset in extras:
        target = ((own_house - 1 + offset - 1) % 12) + 1
        aspected.append(target)

    return aspected


def get_all_aspects(house_map):

    all_planets = get_planet_names(house_map)

    aspect_map = {h: [] for h in range(1, 13)}

    for planet in all_planets:

        aspected_houses = get_aspected_houses(
            planet, house_map
        )

        for house in aspected_houses:
            aspect_map[house].append(planet)

    return aspect_map


def get_aspect_strength(house_map):

    aspect_map = get_all_aspects(house_map)

    return {
        house: len(planets)
        for house, planets in aspect_map.items()
    }


def print_aspects(house_map, house_meanings):

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