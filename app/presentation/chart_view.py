from app.data.house_meanings import HOUSE_MEANINGS


def build_house_chart(planet_positions, lagna_raasi, get_raasi_from_longitude, get_house_number):

    # Initialize all 12 houses as empty
    house_map = {h: [] for h in range(1, 13)}

    for planet, lon in planet_positions.items():

        planet_raasi = get_raasi_from_longitude(lon)
        house = get_house_number(lagna_raasi, planet_raasi)

        house_map[house].append((planet, planet_raasi))

    return house_map


def print_chart(house_map):

    print("\n🪐 FULL HOUSE CHART\n")

    for house in sorted(house_map.keys()):

        meaning = HOUSE_MEANINGS.get(house, "")

        print(f"\n🏠 House {house} - {meaning}")

        for planet, sign in house_map[house]:
            print(f"   • {planet} ({sign})")