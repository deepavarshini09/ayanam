import swisseph as swe

PLANETS = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mars": swe.MARS,
    "Mercury": swe.MERCURY,
    "Jupiter": swe.JUPITER,
    "Venus": swe.VENUS,
    "Saturn": swe.SATURN,
    "Rahu": swe.MEAN_NODE
}


def get_sidereal_longitude(jd, planet_id):

    swe.set_sid_mode(swe.SIDM_LAHIRI)

    # Tropical longitude
    longitude = swe.calc_ut(jd, planet_id)[0][0]

    # Ayanamsa correction
    ayanamsa = swe.get_ayanamsa_ut(jd)

    sidereal_longitude = longitude - ayanamsa

    if sidereal_longitude < 0:
        sidereal_longitude += 360

    return sidereal_longitude


def get_all_planets(jd):

    planet_positions = {}

    for planet_name, planet_id in PLANETS.items():

        sidereal_lon = get_sidereal_longitude(jd, planet_id)

        planet_positions[planet_name] = sidereal_lon

    # Ketu always opposite Rahu
    ketu = planet_positions["Rahu"] + 180

    if ketu >= 360:
        ketu -= 360

    planet_positions["Ketu"] = ketu

    return planet_positions

RAASIS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]


def get_raasi_from_longitude(lon):
    index = int(lon // 30)
    return RAASIS[index]