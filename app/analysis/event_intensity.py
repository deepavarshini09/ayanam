def calculate_event_intensity(
    mah_house,
    ant_house,
    strength
):

    score = 0

    # Mahadasha weight
    if mah_house in strength:
        score += strength[mah_house]

    # Antardasha weight
    if ant_house in strength:
        score += strength[ant_house]

    # Same house amplification
    if mah_house == ant_house:
        score += 2

    return score


def classify_intensity(score):

    if score >= 6:
        return "VERY STRONG"

    elif score >= 4:
        return "STRONG"

    elif score >= 2:
        return "MODERATE"

    return "LOW"


def print_intensity(score, level):

    print("\n⚡ EVENT INTENSITY\n")

    print(f"Score : {score}")
    print(f"Level : {level}")