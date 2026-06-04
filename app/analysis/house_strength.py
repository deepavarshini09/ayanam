from app.core.aspect_engine import get_aspect_strength


def get_house_strength(house_map):

    aspect_strength = get_aspect_strength(house_map)

    strength = {}

    for house, entries in house_map.items():

        # entries are (planet, raasi) tuples
        occupancy = len(entries)

        aspect = aspect_strength.get(house, 0)

        strength[house] = round(
            occupancy + (aspect * 0.5), 1
        )

    return strength


def print_house_strength(strength, house_meanings):

    print("\n🔥 HOUSE STRENGTH ANALYSIS\n")

    for house in sorted(strength.keys()):

        score = strength[house]

        level = (
            "Very Strong" if score >= 3 else
            "Strong"      if score >= 2 else
            "Active"      if score >= 1 else
            "Influenced"  if score > 0  else
            "Empty"
        )

        print(
            f"House {house}: {level} "
            f"(score: {score})"
        )
        print(f"   → {house_meanings[house]}\n")