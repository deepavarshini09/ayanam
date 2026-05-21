NAKSHATHRAS = [
    "Ashwini","Bharani","Krittika","Rohini","Mrigashira","Ardra",
    "Punarvasu","Pushya","Ashlesha","Magha","Purva Phalguni",
    "Uttara Phalguni","Hasta","Chitra","Swati","Vishakha",
    "Anuradha","Jyeshtha","Mula","Purva Ashadha","Uttara Ashadha",
    "Shravana","Dhanishta","Shatabhisha","Purva Bhadrapada",
    "Uttara Bhadrapada","Revati"
]

def get_nakshathra(moon_lon):
    segment = 360 / 27
    index = int(moon_lon // segment)
    paadha = int((moon_lon % segment) // (segment / 4)) + 1
    return NAKSHATHRAS[index], paadha