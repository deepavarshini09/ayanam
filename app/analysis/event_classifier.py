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


def classify_events(mah_house, ant_house):

    events = set()

    if mah_house in EVENT_MAP:
        events.add(EVENT_MAP[mah_house])

    if ant_house in EVENT_MAP:
        events.add(EVENT_MAP[ant_house])

    return list(events)


def print_events(events):

    print("\n📅 LIKELY LIFE EVENT THEMES\n")

    for e in events:
        print(f"• {e}")