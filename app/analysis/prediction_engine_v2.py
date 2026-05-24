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

    # ---------------- MAIN PERIOD ----------------

    predictions.append(
        f"{mahadasha} Mahadasha strongly activates "
        f"House {mah_house} themes: "
        f"{house_meanings.get(mah_house)}."
    )

    # ---------------- ANTARDASHA EFFECT ----------------

    if mahadasha != antardasha:

        predictions.append(
            f"{antardasha} Antardasha brings additional focus on "
            f"House {ant_house}: "
            f"{house_meanings.get(ant_house)}."
        )

    else:

        predictions.append(
            f"This is a pure {mahadasha}/{antardasha} phase, "
            f"making its effects highly intensified."
        )

    # ---------------- PLANET NATURE ----------------

    predictions.append(
        f"{mahadasha} influence indicates "
        f"{PLANET_MEANINGS.get(mahadasha)}."
    )

    if mahadasha != antardasha:

        predictions.append(
            f"{antardasha} modifies the period through "
            f"{PLANET_MEANINGS.get(antardasha)}."
        )

    # ---------------- HOUSE STRENGTH ----------------

    if mah_house in strength:

        level = strength[mah_house]

        if level >= 2:

            predictions.append(
                f"House {mah_house} is strongly activated in the chart."
            )

        else:

            predictions.append(
                f"House {mah_house} has moderate activation."
            )

    return predictions


def print_deep_predictions(predictions):

    print("\n🔮 DEEP PREDICTION INSIGHTS\n")

    for p in predictions:
        print("•", p)