from house_meanings import HOUSE_MEANINGS


def build_house_chart(planet_positions, lagna_raasi, get_raasi_from_longitude, get_house_number):

    house_map = {}

    for planet, lon in planet_positions.items():

        planet_raasi = get_raasi_from_longitude(lon)
        house = get_house_number(lagna_raasi, planet_raasi)

        if house not in house_map:
            house_map[house] = []

        house_map[house].append((planet, planet_raasi))

    return house_map


def print_chart(house_map):

    print("\n🪐 FULL HOUSE CHART\n")

    for house in sorted(house_map.keys()):

        meaning = HOUSE_MEANINGS.get(house, "")

        print(f"\n🏠 House {house} - {meaning}")

        for planet, sign in house_map[house]:
            print(f"   • {planet} ({sign})")