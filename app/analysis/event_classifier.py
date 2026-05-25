from app.analysis.planet_nature_engine import (
    PLANET_NATURES
)

EVENT_MAP = {

    1: "self-development",

    2: "finance",

    3: "communication",

    4: "home and property",

    5: "love and creativity",

    6: "health and competition",

    7: "relationships and marriage",

    8: "transformation and instability",

    9: "higher studies and spirituality",

    10: "career and public image",

    11: "income and networking",

    12: "losses and foreign connections"
}


def classify_events(

    mah_house,
    ant_house,

    mahadasha,
    antardasha
):

    events = []

    # ---------------- HOUSE THEMES ----------------

    if mah_house in EVENT_MAP:

        events.append(
            EVENT_MAP[mah_house]
        )

    if ant_house in EVENT_MAP:

        events.append(
            EVENT_MAP[ant_house]
        )

    # ---------------- PLANET NATURES ----------------

    mah_data = PLANET_NATURES[
        mahadasha
    ]

    ant_data = PLANET_NATURES[
        antardasha
    ]

    mah_themes = ", ".join(
        mah_data["themes"]
    )

    ant_themes = ", ".join(
        ant_data["themes"]
    )

    events.append(

        f"{mahadasha} themes: "
        f"{mah_themes}"
    )

    events.append(

        f"{antardasha} themes: "
        f"{ant_themes}"
    )

    return events


def print_events(events):

    print(
        "\n📅 LIKELY LIFE EVENT THEMES\n"
    )

    for e in events:

        print(f"• {e}")