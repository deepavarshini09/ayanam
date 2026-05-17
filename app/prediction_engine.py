def generate_predictions(house_map, strength):

    print("\n🔮 BASIC PREDICTIONS\n")

    for house, planets in house_map.items():

        if len(planets) == 0:
            continue

        if house == 8 and len(planets) >= 2:
            print("⚠️ Strong transformation phases possible")

        if house == 11 and len(planets) >= 2:
            print("📈 Gains, networking, opportunities increase")

        if house == 4 and len(planets) >= 2:
            print("🏡 Focus on home, emotional grounding")

        if house == 10 and len(planets) >= 2:
            print("💼 Career focus and visibility increases")