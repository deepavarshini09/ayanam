import swisseph as swe
from time_utils import convert_to_utc
from chart_engine import get_raasi_from_longitude

swe.set_ephe_path()

utc_time = convert_to_utc("2006-06-09", "19:10", 5.5)

jd = swe.julday(
    utc_time.year,
    utc_time.month,
    utc_time.day,
    utc_time.hour + utc_time.minute/60
)

sun_data = swe.calc_ut(jd, swe.SUN)
sun_lon = sun_data[0]   # 🌟 this is important

raasi = get_raasi_from_longitude(sun_lon)

print("Sun Longitude:", sun_lon)
print("Raasi:", raasi)