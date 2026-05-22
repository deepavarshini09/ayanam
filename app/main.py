from app.core.geo_engine import get_coordinates
from app.core.time_utils import convert_to_utc, get_julian_day

from app.core.chart_engine import get_raasi_from_longitude
from app.core.nakshathra_engine import get_nakshathra
from app.core.lagna_engine import get_lagna

from app.core.planet_engine import get_all_planets
from app.core.house_engine import get_house_number

from app.data.constants import RAASI_TAMIL, NAKSHATHRA_TAMIL
from app.data.house_meanings import HOUSE_MEANINGS
from app.data.test_cases import TEST_CASE_1

from app.presentation.chart_view import build_house_chart, print_chart

from app.analysis.house_strength import get_house_strength, print_house_strength
from app.analysis.prediction_engine import generate_predictions

from app.dasha.dasha_engine import generate_dasha_table, print_dasha

from app.dasha.antardasha_engine import (
    generate_antardasha,
    print_antardasha
)

import swisseph as swe
swe.set_sid_mode(swe.SIDM_LAHIRI)


# ---------------- TEST INPUT ----------------
date = TEST_CASE_1["date"]
time = TEST_CASE_1["time"]
place = TEST_CASE_1["place"]
timezone = TEST_CASE_1["timezone"]

# ---------------- GEO ----------------
lat, lon = get_coordinates(place)

# ---------------- TIME ----------------
utc_time = convert_to_utc(date, time, timezone)
jd = get_julian_day(utc_time)

# ---------------- PLANETS ----------------
planet_positions = get_all_planets(jd)

# ---------------- MOON ----------------
moon_lon = planet_positions["Moon"]

raasi = get_raasi_from_longitude(moon_lon)
nakshathra, paadha = get_nakshathra(moon_lon)

# ---------------- LAGNA ----------------
lagna_lon = get_lagna(jd, lat, lon)
lagna_raasi = get_raasi_from_longitude(lagna_lon)

# ---------------- TAMIL ----------------
tamil_raasi = RAASI_TAMIL[raasi]
tamil_lagna = RAASI_TAMIL[lagna_raasi]
tamil_nakshathra = NAKSHATHRA_TAMIL[nakshathra]

# ---------------- OUTPUT ----------------
print("\n🌌 Raasi:", raasi)
print("🇮🇳 Tamil Raasi:", tamil_raasi)

print("\n🌙 Nakshathra:", nakshathra)
print("🇮🇳 Tamil Nakshathra:", tamil_nakshathra)
print("🔢 Paadha:", paadha)

print("\n🌅 Lagna:", lagna_raasi)
print("🇮🇳 Tamil Lagna:", tamil_lagna)

# ---------------- DEBUG ----------------
print("\nDEBUG JD:", jd)
print("DEBUG LAT/LON:", lat, lon)
print("DEBUG LAGNA DEG:", lagna_lon)

# ---------------- HOUSE MAP ----------------
house_map = build_house_chart(
    planet_positions,
    lagna_raasi,
    get_raasi_from_longitude,
    get_house_number
)

print_chart(house_map)

# ---------------- HOUSE STRENGTH ----------------
strength = get_house_strength(house_map)
print_house_strength(strength, HOUSE_MEANINGS)

# ---------------- PREDICTIONS ----------------
generate_predictions(house_map, strength)

# ---------------- DASHA ----------------
dasha_timeline = generate_dasha_table(nakshathra)
print_dasha(dasha_timeline) 

# ---------------- ANTARDASHA ----------------

first_dasha = dasha_timeline[0]["planet"]
first_years = dasha_timeline[0]["end"] - dasha_timeline[0]["start"]

antardashas = generate_antardasha(
    first_dasha,
    first_years
)

print_antardasha(antardashas)