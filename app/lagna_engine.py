import swisseph as swe

def get_lagna(jd, lat, lon):

    # Get tropical ascendant
    houses, ascmc = swe.houses_ex(jd, lat, lon, b'P')
    tropical_lagna = ascmc[0]

    # Get Lahiri ayanamsa
    ayanamsa = swe.get_ayanamsa_ut(jd)

    # Convert to sidereal lagna
    sidereal_lagna = tropical_lagna - ayanamsa

    if sidereal_lagna < 0:
        sidereal_lagna += 360

    return sidereal_lagna