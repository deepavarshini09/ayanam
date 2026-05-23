from app.data.planet_meanings import PLANET_MEANINGS


def generate_deep_predictions(
    mahadasha,
    antardasha,
    house_map,
    house_meanings,
    get_house_strength
):

    mah_house = None
    ant_house = None

    for h, planets in house_map.items():
        for p in planets:
            if mahadasha in p:
                mah_house = h
            if antardasha in p:
                ant_house = h

    strength = get_house_strength(house_map)

    predictions = []

    # MAIN INTERPRETATION
    predictions.append(
        f"{mahadasha} Mahadasha activates {house_meanings.get(mah_house)}"
    )

    predictions.append(
        f"{antardasha} Antardasha modifies with {house_meanings.get(ant_house)} energy"
    )

    # PLANET NATURE
    predictions.append(
        f"{mahadasha} nature: {PLANET_MEANINGS.get(mahadasha)}"
    )

    predictions.append(
        f"{antardasha} nature: {PLANET_MEANINGS.get(antardasha)}"
    )

    # HOUSE STRENGTH EFFECT
    if mah_house in strength:
        predictions.append(
            f"House {mah_house} strength: {strength[mah_house]}"
        )

    if ant_house in strength:
        predictions.append(
            f"House {ant_house} strength: {strength[ant_house]}"
        )

    return predictions


def print_deep_predictions(predictions):

    print("\n🔮 DEEP PREDICTION INSIGHTS\n")

    for p in predictions:
        print("•", p)