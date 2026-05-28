def synthesize_prediction(

    mahadasha,
    antardasha,

    mah_house,
    ant_house
):

    predictions = []

    # ---------------- HOUSE COMBINATIONS ----------------

    if mah_house == 8 and ant_house == 7:

        predictions.append(

            "Relationships may undergo "
            "deep transformation during "
            "this period."
        )

    if mah_house == 10:

        predictions.append(

            "Career responsibilities "
            "and public image become "
            "important themes."
        )

    # ---------------- PLANET EFFECTS ----------------

    if mahadasha == "Saturn":

        predictions.append(

            "Saturn may create delay, "
            "pressure and maturity-driven "
            "growth."
        )

    if antardasha == "Mercury":

        predictions.append(

            "Communication, analysis and "
            "decision-making become more active."
        )

    return predictions


def print_synthesized_predictions(
    predictions
):

    print(
        "\n🧠 SYNTHESIZED PREDICTIONS\n"
    )

    for p in predictions:

        print(f"• {p}")