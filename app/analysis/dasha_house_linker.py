def find_planet_house(house_map, target_planet):

    for house, planets in house_map.items():

        for entry in planets:

            if target_planet in entry:
                return house

    return None


def analyze_dasha_effect(
    house_map,
    mahadasha,
    antardasha,
    house_meanings
):

    maha_house = find_planet_house(
        house_map,
        mahadasha
    )

    antara_house = find_planet_house(
        house_map,
        antardasha
    )

    result = {
        "mahadasha": mahadasha,
        "maha_house": maha_house,
        "maha_meaning": house_meanings.get(
            maha_house,
            "Unknown"
        ),

        "antardasha": antardasha,
        "antara_house": antara_house,
        "antara_meaning": house_meanings.get(
            antara_house,
            "Unknown"
        )
    }

    return result


def print_dasha_analysis(result):

    print("\n🔮 DASHA ANALYSIS\n")

    print(
        f"🪐 Mahadasha: "
        f"{result['mahadasha']}"
    )

    print(
        f"   → House {result['maha_house']}"
    )

    print(
        f"   → {result['maha_meaning']}"
    )

    print()

    print(
        f"🔹 Antardasha: "
        f"{result['antardasha']}"
    )

    print(
        f"   → House {result['antara_house']}"
    )

    print(
        f"   → {result['antara_meaning']}"
    )