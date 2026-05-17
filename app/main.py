from geo_engine import get_coordinates
from time_utils import convert_to_utc, get_julian_day

from chart_engine import get_moon_longitude, get_raasi_from_longitude
from nakshathra_engine import get_nakshathra
from lagna_engine import get_lagna

from constants import RAASI_TAMIL, NAKSHATHRA_TAMIL

from planet_engine import get_all_planets
from house_engine import get_house_number
from house_meanings import HOUSE_MEANINGS

import swisseph as swe

swe.set_sid_mode(swe.SIDM_LAHIRI)

# ---------------- INPUT ----------------
date = input("Enter birth date (YYYY-MM-DD): ")
time = input("Enter birth time (HH:MM): ")
place = input("Enter birth place: ")
timezone = input("Enter timezone (IST/UTC/+5.5): ")

# ---------------- GEO ----------------
lat, lon = get_coordinates(place)

# ---------------- TIME ----------------
utc_time = convert_to_utc(date, time, timezone)
jd = get_julian_day(utc_time)

# ---------------- ASTRO (MOON + BASIC) ----------------
moon_lon = get_moon_longitude(jd)

raasi = get_raasi_from_longitude(moon_lon)
nakshathra, paadha = get_nakshathra(moon_lon)

lagna_lon = get_lagna(jd, lat, lon)
lagna_raasi = get_raasi_from_longitude(lagna_lon)

# ---------------- TAMIL ----------------
tamil_raasi = RAASI_TAMIL[raasi]
tamil_lagna = RAASI_TAMIL[lagna_raasi]
tamil_nakshathra = NAKSHATHRA_TAMIL[nakshathra]

# ---------------- OUTPUT BASIC ----------------
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

# ---------------- PLANETS ----------------
planet_positions = get_all_planets(jd)

print("\n🪐 PLANETARY POSITIONS (WITH HOUSES)\n")

for planet, lon in planet_positions.items():

    planet_raasi = get_raasi_from_longitude(lon)

    house = get_house_number(lagna_raasi, planet_raasi)

    meaning = HOUSE_MEANINGS[house]

print(f"{planet}: {planet_raasi} → House {house}")
print(f"   Meaning: {meaning}\n")