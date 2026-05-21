import requests

def get_coordinates(place):
    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": place,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "ayanam-app"
    }

    res = requests.get(url, params=params, headers=headers)
    data = res.json()

    if not data:
        raise Exception("Location not found")

    return float(data[0]["lat"]), float(data[0]["lon"])