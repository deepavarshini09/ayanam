ASPECTS = {
    "Mars": [4, 7, 8],
    "Jupiter": [5, 7, 9],
    "Saturn": [3, 7, 10],
    "Rahu": [5, 7, 9],
    "Ketu": [5, 7, 9],
    "Sun": [7],
    "Moon": [7],
    "Mercury": [7],
    "Venus": [7]
}


def analyze_aspects(planet_positions, get_raasi_from_longitude, get_house_number, lagna_raasi):

    print("\n🧿 ASPECT ANALYSIS\n")

    planets = list(planet_positions.keys())

    for p1 in planets:

        for p2 in planets:

            if p1 == p2:
                continue

            # simplified rule: same house interaction
            if p1 in planet_positions and p2 in planet_positions:

                print(f"{p1} influences {p2}")