RAASIS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]


def get_house_number(lagna_raasi, planet_raasi):

    lagna_index = RAASIS.index(lagna_raasi)
    planet_index = RAASIS.index(planet_raasi)

    house = (planet_index - lagna_index) % 12 + 1

    return house