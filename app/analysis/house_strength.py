# app/analysis/house_strength.py

from app.core.aspect_engine import get_aspect_strength


def get_house_strength(house_map):
    """
    Returns combined strength per house:
    occupancy (planets present) + aspect influence.

    Occupancy counts full (weight 1 per planet).
    Aspects count half (weight 0.5 per aspecting planet)
    since presence is stronger than aspect in Jyotish.
    """

    aspect_strength = get_aspect_strength(house_map)

    strength = {}

    for house, planets in house_map.items():

        occupancy = len(planets)

        aspect = aspect_strength.get(house, 0)

        # Combined score: occupancy + half aspect weight
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