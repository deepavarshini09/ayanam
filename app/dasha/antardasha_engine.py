from app.dasha.dasha_engine import DASHA_SEQUENCE, DASHA_YEARS


def generate_antardasha(mahadasha_planet, mahadasha_years):
    """
    Generates Antardasha periods within a Mahadasha
    """

    antardashas = []

    total_cycle = 120

    start_index = DASHA_SEQUENCE.index(mahadasha_planet)

    rotated_sequence = (
        DASHA_SEQUENCE[start_index:]
        + DASHA_SEQUENCE[:start_index]
    )

    current = 0

    for planet in rotated_sequence:

        duration = (
            mahadasha_years
            * DASHA_YEARS[planet]
        ) / total_cycle

        antardashas.append({
            "mahadasha": mahadasha_planet,
            "antardasha": planet,
            "start": round(current, 2),
            "end": round(current + duration, 2)
        })

        current += duration

    return antardashas


def print_antardasha(antardashas):

    print("\n🔹 ANTARDASHA PERIODS\n")

    for a in antardashas:

        print(
            f"{a['mahadasha']} / "
            f"{a['antardasha']} : "
            f"{a['start']} - {a['end']} years"
        )