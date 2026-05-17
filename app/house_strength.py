def get_house_strength(house_map):
    """
    Returns how 'active' each house is based on number of planets
    """

    strength = {}

    for house, planets in house_map.items():
        strength[house] = len(planets)

    return strength


def print_house_strength(strength, house_meanings):

    print("\n🔥 HOUSE STRENGTH ANALYSIS\n")

    for house in sorted(strength.keys()):

        count = strength[house]

        level = (
            "Very Strong" if count >= 3 else
            "Strong" if count == 2 else
            "Active" if count == 1 else
            "Empty"
        )

        print(f"House {house}: {level} ({count} planets)")
        print(f"   → {house_meanings[house]}\n")