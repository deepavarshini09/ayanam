from app.data.constants import DASHA_YEARS


def generate_antardasha(
    mahadasha,
    total_years,
    start_age=0
):

    antardasha_list = []

    planets = list(
        DASHA_YEARS.keys()
    )

    start_index = planets.index(
        mahadasha
    )

    ordered_planets = (
        planets[start_index:]
        +
        planets[:start_index]
    )

    current = start_age

    for planet in ordered_planets:

        duration = (
            total_years
            *
            DASHA_YEARS[planet]
            / 120
        )

        antardasha_list.append({

            "mahadasha": mahadasha,

            "antardasha": planet,

            "start": round(current, 2),

            "end": round(
                current + duration,
                2
            )
        })

        current += duration

    return antardasha_list


def print_antardasha(
    antardashas
):

    print("\n🔹 ANTARDASHA PERIODS\n")

    for d in antardashas:

        print(

            f"{d['mahadasha']} / "

            f"{d['antardasha']} : "

            f"{d['start']} - "

            f"{d['end']} years"
        )