from datetime import datetime, timedelta
import swisseph as swe

def convert_to_utc(date, time, tz):
    dt = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")

    if tz.upper() == "IST":
        offset = 5.5
    elif tz.upper() == "UTC":
        offset = 0
    else:
        offset = float(tz)

    return dt - timedelta(hours=offset)


def get_julian_day(dt):
    return swe.julday(
        dt.year,
        dt.month,
        dt.day,
        dt.hour + dt.minute / 60.0  # keep float precision
    )