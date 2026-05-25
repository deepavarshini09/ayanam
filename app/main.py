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

from app.presentation.chart_view import (
    build_house_chart,
    print_chart
)

from app.analysis.house_strength import (
    get_house_strength,
    print_house_strength
)

from app.analysis.prediction_engine import (
    generate_predictions
)

from app.analysis.prediction_engine_v2 import (
    generate_deep_predictions,
    print_deep_predictions
)

from app.analysis.event_classifier import (
    classify_events,
    print_events
)

from app.analysis.dasha_house_linker import (
    analyze_dasha_effect,
    print_dasha_analysis
)

from app.analysis.event_intensity import (
    calculate_event_intensity,
    classify_intensity,
    print_intensity
)

from app.dasha.dasha_engine import (
    generate_dasha_table,
    print_dasha
)

from app.dasha.antardasha_engine import (
    generate_antardasha,
    print_antardasha
)

from app.dasha.current_dasha import (
    get_current_age,
    find_current_dasha,
    find_current_antardasha
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

utc_time = convert_to_utc(
    date,
    time,
    timezone
)

jd = get_julian_day(utc_time)

# ---------------- PLANETS ----------------

planet_positions = get_all_planets(jd)

# ---------------- MOON ----------------

moon_lon = planet_positions["Moon"]

raasi = get_raasi_from_longitude(
    moon_lon
)

nakshathra, paadha = get_nakshathra(
    moon_lon
)

# ---------------- LAGNA ----------------

lagna_lon = get_lagna(
    jd,
    lat,
    lon
)

lagna_raasi = get_raasi_from_longitude(
    lagna_lon
)

# ---------------- TAMIL ----------------

tamil_raasi = RAASI_TAMIL[raasi]

tamil_lagna = RAASI_TAMIL[lagna_raasi]

tamil_nakshathra = (
    NAKSHATHRA_TAMIL[nakshathra]
)

# ---------------- OUTPUT ----------------

print("\n🌌 Raasi:", raasi)
print("🇮🇳 Tamil Raasi:", tamil_raasi)

print("\n🌙 Nakshathra:", nakshathra)
print(
    "🇮🇳 Tamil Nakshathra:",
    tamil_nakshathra
)

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

strength = get_house_strength(
    house_map
)

print_house_strength(
    strength,
    HOUSE_MEANINGS
)

# ---------------- BASIC PREDICTIONS ----------------

generate_predictions(
    house_map,
    strength
)

# ---------------- DASHA TIMELINE ----------------

dasha_timeline = generate_dasha_table(
    nakshathra
)

print_dasha(dasha_timeline)

# ---------------- CURRENT AGE ----------------

birth_year = int(
    date.split("-")[0]
)

current_age = get_current_age(
    birth_year
)

# ---------------- CURRENT MAHADASHA ----------------

current_dasha = find_current_dasha(
    dasha_timeline,
    current_age
)

current_mahadasha = (
    current_dasha["planet"]
)

current_dasha_start = (
    current_dasha["start"]
)

current_dasha_years = (
    current_dasha["end"]
    -
    current_dasha["start"]
)

# ---------------- ANTARDASHA ----------------

antardashas = generate_antardasha(
    current_mahadasha,
    current_dasha_years,
    current_dasha_start
)

print_antardasha(antardashas)

# ---------------- CURRENT ANTARDASHA ----------------

current_antardasha = (
    find_current_antardasha(
        antardashas,
        current_age
    )
)

current_antardasha_name = (
    current_antardasha["antardasha"]
)

# ---------------- CURRENT ACTIVE PERIOD ----------------

print("\n🕒 CURRENT ACTIVE PERIOD\n")

print(
    f"Current Age : {current_age}"
)

print(
    f"Mahadasha   : "
    f"{current_mahadasha}"
)

print(
    f"Antardasha  : "
    f"{current_antardasha_name}"
)

# ---------------- DEEP PREDICTIONS ----------------

preds = generate_deep_predictions(
    current_mahadasha,
    current_antardasha_name,
    house_map,
    HOUSE_MEANINGS,
    get_house_strength
)

print_deep_predictions(preds)

# ---------------- DASHA ANALYSIS ----------------

dasha_result = analyze_dasha_effect(
    house_map,
    current_mahadasha,
    current_antardasha_name,
    HOUSE_MEANINGS
)

print_dasha_analysis(
    dasha_result
)

# ---------------- EVENT CLASSIFICATION ----------------

mah_house = dasha_result["maha_house"]

ant_house = dasha_result["antara_house"]

events = classify_events(
    mah_house,
    ant_house,
    current_mahadasha,
    current_antardasha_name
)

# ---------------- EVENT INTENSITY ----------------

score = calculate_event_intensity(
    mah_house,
    ant_house,
    strength
)

level = classify_intensity(score)

print_intensity(
    score,
    level
)