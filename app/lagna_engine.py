import swisseph as swe

def get_lagna(jd, lat, lon):
    houses, ascmc = swe.houses_ex(jd, lat, lon, b'P')
    asc = ascmc[0]

    # ensure 0–360 normalization
    if asc < 0:
        asc += 360

    return asc