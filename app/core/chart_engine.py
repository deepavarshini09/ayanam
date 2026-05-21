import swisseph as swe

RAASIS = [
    "Aries","Taurus","Gemini","Cancer","Leo","Virgo",
    "Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"
]

def get_moon_longitude(jd):
    import swisseph as swe
    swe.set_sid_mode(swe.SIDM_LAHIRI)

    moon = swe.calc_ut(jd, swe.MOON)[0][0]
    ayanamsa = swe.get_ayanamsa_ut(jd)

    sidereal_moon = moon - ayanamsa
    if sidereal_moon < 0:
        sidereal_moon += 360

    return sidereal_moon


def get_raasi_from_longitude(lon):
    index = int(lon // 30)
    return RAASIS[index]