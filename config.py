# input args
FROM_DATE = None
TO_DATE = None

URL = "http://www.varmelast.dk/api/v1/heatdata/historical"
DATA_DICT = {
    "Kraftvarmeanlæg": "Cogeneration plant",
    "VEKS": "VEKS",
    "Biogas": "Biogas",
    "Geotermi": "Geothermal",
    "Industriel overskudsvarme": "Industrial waste heat",
    "Spidslast gas": "Peak load gas",
    "Lokal produktion": "Local production",
    "Solvarme": "Solar heating",
    "Spidslast el": "Peak load el",
    "Varmepumper": "Heat pumps",
    "CTR": "CTR",
    "Spidslast træpiller": "Peak load wood pellets",
    "Affaldsenergianlæg": "Waste energy plant",
    "Produktion i alt": "Total production",
    "Spidslast olie": "Peak load oil",
    "CO2 - Udledning": "CO2 - Emission",
}

INPUT_DICT = {
    1: "Cogeneration plant",
    2: "VEKS",
    3: "Biogas",
    4: "Geothermal",
    5: "Industrial waste heat",
    6: "Peak load gas",
    7: "Local production",
    8: "Solar heating",
    9: "Peak load el",
    10: "Heat pumps",
    11: "CTR",
    12: "Peak load wood pellets",
    13: "Waste energy plant",
    14: "Total production",
    15: "Peak load oil",
    16: "CO2 - Emission",
}

# Other
DATE_FORMAT = r"%Y-%m-%d"
ERRORS = []
