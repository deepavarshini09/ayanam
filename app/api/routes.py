from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.core.geo_engine import get_coordinates
from app.core.time_utils import convert_to_utc, get_julian_day
from app.core.chart_engine import get_raasi_from_longitude
from app.core.nakshathra_engine import get_nakshathra
from app.core.lagna_engine import get_lagna
from app.core.planet_engine import get_all_planets
from app.core.house_engine import get_house_number
from app.core.aspect_engine import get_all_aspects

from app.data.constants import RAASI_TAMIL, NAKSHATHRA_TAMIL
from app.data.house_meanings import HOUSE_MEANINGS

from app.presentation.chart_view import build_house_chart

from app.analysis.house_strength import get_house_strength
from app.analysis.dasha_house_linker import analyze_dasha_effect
from app.analysis.event_classifier import classify_events
from app.analysis.event_intensity import (
    calculate_event_intensity,
    classify_intensity
)
from app.analysis.prediction_synthesizer import synthesize_prediction

from app.dasha.dasha_engine import generate_dasha_table
from app.dasha.antardasha_engine import generate_antardasha
from app.dasha.current_dasha import (
    get_current_age,
    find_current_dasha,
    find_current_antardasha
)

import swisseph as swe

swe.set_sid_mode(swe.SIDM_LAHIRI)

app = FastAPI(
    title="Ayanam API",
    description="Vedic astrology predictions engine",
    version="1.0.0"
)


# ---------------- REQUEST MODEL ----------------

class BirthInput(BaseModel):
    date: str       # "YYYY-MM-DD"
    time: str       # "HH:MM"
    place: str      # "Erode"
    timezone: str   # "IST"


# ---------------- SHARED BUILDER ----------------

def build_full_chart(data: BirthInput):
    """
    Core pipeline shared across all endpoints.
    Returns all computed chart data as a dict.
    """

    # Geo
    lat, lon = get_coordinates(data.place)

    # Time
    utc_time = convert_to_utc(
        data.date, data.time, data.timezone
    )
    jd = get_julian_day(utc_time)

    # Planets
    planet_positions = get_all_planets(jd)

    # Moon
    moon_lon = planet_positions["Moon"]
    raasi = get_raasi_from_longitude(moon_lon)
    nakshathra, paadha = get_nakshathra(moon_lon)

    # Lagna
    lagna_lon = get_lagna(jd, lat, lon)
    lagna_raasi = get_raasi_from_longitude(lagna_lon)

    # House map
    house_map = build_house_chart(
        planet_positions,
        lagna_raasi,
        get_raasi_from_longitude,
        get_house_number
    )

    # Strength and aspects
    strength = get_house_strength(house_map)
    aspect_map = get_all_aspects(house_map)

    # Dasha
    dasha_timeline = generate_dasha_table(nakshathra)
    current_age = get_current_age(data.date)

    current_dasha = find_current_dasha(
        dasha_timeline, current_age
    )
    current_mahadasha = current_dasha["planet"]
    current_dasha_start = current_dasha["start"]
    current_dasha_years = (
        current_dasha["end"] - current_dasha["start"]
    )

    antardashas = generate_antardasha(
        current_mahadasha,
        current_dasha_years,
        current_dasha_start
    )

    current_antardasha = find_current_antardasha(
        antardashas, current_age
    )
    current_antardasha_name = current_antardasha["antardasha"]

    # Dasha analysis
    dasha_result = analyze_dasha_effect(
        house_map,
        current_mahadasha,
        current_antardasha_name,
        HOUSE_MEANINGS
    )

    mah_house = dasha_result["maha_house"]
    ant_house = dasha_result["antara_house"]

    # Events
    events = classify_events(
        mah_house, ant_house,
        current_mahadasha, current_antardasha_name
    )

    # Intensity
    score = calculate_event_intensity(
        mah_house, ant_house, strength
    )
    level = classify_intensity(score)

    # Predictions
    predictions = synthesize_prediction(
        current_mahadasha,
        current_antardasha_name,
        mah_house,
        ant_house
    )

    return {
        "raasi": raasi,
        "tamil_raasi": RAASI_TAMIL[raasi],
        "nakshathra": nakshathra,
        "tamil_nakshathra": NAKSHATHRA_TAMIL[nakshathra],
        "paadha": paadha,
        "lagna": lagna_raasi,
        "tamil_lagna": RAASI_TAMIL[lagna_raasi],
        "house_map": {
            str(h): [
                {"planet": p, "raasi": r}
                for p, r in entries
            ]
            for h, entries in house_map.items()
        },
        "aspects": {
            str(h): planets
            for h, planets in aspect_map.items()
        },
        "strength": {
            str(h): s
            for h, s in strength.items()
        },
        "dasha_timeline": dasha_timeline,
        "current_age": current_age,
        "current_mahadasha": current_mahadasha,
        "current_antardasha": current_antardasha_name,
        "antardashas": antardashas,
        "maha_house": mah_house,
        "antara_house": ant_house,
        "events": events,
        "intensity_score": score,
        "intensity_level": level,
        "predictions": predictions
    }


# ---------------- ENDPOINTS ----------------

@app.post("/chart")
def get_chart(data: BirthInput):
    """
    Returns basic birth chart —
    raasi, nakshatra, lagna, house map.
    """
    try:
        result = build_full_chart(data)

        return {
            "raasi": result["raasi"],
            "tamil_raasi": result["tamil_raasi"],
            "nakshathra": result["nakshathra"],
            "tamil_nakshathra": result["tamil_nakshathra"],
            "paadha": result["paadha"],
            "lagna": result["lagna"],
            "tamil_lagna": result["tamil_lagna"],
            "house_map": result["house_map"],
            "aspects": result["aspects"],
            "strength": result["strength"]
        }

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=str(e)
        )


@app.post("/dasha")
def get_dasha(data: BirthInput):
    """
    Returns full Vimshottari dasha timeline
    and current active Mahadasha + Antardasha.
    """
    try:
        result = build_full_chart(data)

        return {
            "current_age": result["current_age"],
            "current_mahadasha": result["current_mahadasha"],
            "current_antardasha": result["current_antardasha"],
            "dasha_timeline": result["dasha_timeline"],
            "antardashas": result["antardashas"]
        }

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=str(e)
        )


@app.post("/predictions")
def get_predictions(data: BirthInput):
    """
    Returns synthesized predictions, event
    classification and intensity for current period.
    """
    try:
        result = build_full_chart(data)

        return {
            "current_mahadasha": result["current_mahadasha"],
            "current_antardasha": result["current_antardasha"],
            "maha_house": result["maha_house"],
            "antara_house": result["antara_house"],
            "events": result["events"],
            "intensity_score": result["intensity_score"],
            "intensity_level": result["intensity_level"],
            "predictions": result["predictions"]
        }

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=str(e)
        )


@app.post("/full")
def get_full_reading(data: BirthInput):
    """
    Returns everything in one call.
    """
    try:
        return build_full_chart(data)

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=str(e)
        )


@app.get("/health")
def health():
    return {"status": "ok"}