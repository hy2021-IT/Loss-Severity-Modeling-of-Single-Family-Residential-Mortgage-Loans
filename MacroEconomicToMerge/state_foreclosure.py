
us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "District of Columbia": "DC",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Puerto Rico" : "PR",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virgin Islands" : "VI",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}
# invert the dictionary
abbrev_to_us_state = dict(map(reversed, us_state_to_abbrev.items()))
##print(abbrev_to_us_state)

method_of_foreclosurer = {
    "AL": "Power-of-Sale",
    "AK": "Power-of-Sale",
    "AZ": "Power-of-Sale",
    "AR": "Power-of-Sale",
    "CA": "Power-of-Sale",
    "CO": "Power-of-Sale",
    "CT": "Strict Foreclosure",
    "DE": "Judicial",
    "FL": "Judicial",
    "GA": "Power-of-Sale",
    "HI": "Judicial",
    "ID": "Judicial",
    "IL": "Judicial",
    "IN": "Judicial",
    "IA": "Judicial",
    "KS": "Judicial",
    "KY": "Judicial",
    "LA": "Judicial",
    "ME": "Entry and Possession",
    "MD": "Power-of-Sale",
    "MA": "Power-of-Sale",
    "MI": "Power-of-Sale",
    "MN": "Power-of-Sale",
    "MS": "Power-of-Sale",
    "MO": "Power-of-Sale",
    "MT": "Power-of-Sale",
    "NE": "Judicial",
    "NV": "Power-of-Sale",
    "NH": "Power-of-Sale",
    "NJ": "Judicial",
    "NM": "Judicial",
    "NY": "Judicial",
    "NC": "Power-of-Sale",
    "ND": "Judicial",
    "OH": "Judicial",
    "OK": "Judicial",
    "OR": "Power-of-Sale",
    "PA": "Judicial",
    "RI": "Power-of-Sale",
    "SC": "Judicial",
    "SD": "Judicial",
    "TN": "Power-of-Sale",
    "TX": "Power-of-Sale",
    "UT": "Power-of-Sale",
    "VT": "Strict Foreclosure",
    "VA": "Power-of-Sale",
    "WA": "Power-of-Sale",
    "WV": "Power-of-Sale",
    "WI": "Power-of-Sale",
    "WY": "Power-of-Sale",
    "DC": "Judicial"
}

state_time_frame = {
    "AL": "420",
    "AK": "480",
    "AZ": "450",
    "AR": "420",
    "CA": "480",
    "CO": "450",
    "CT": "660",
    "DE": "720",
    "FL": "810",
    "GA": "330",
    "HI": "900",
    "ID": "630",
    "IL": "630",
    "IN": "540",
    "IA": "570",
    "KS": "450",
    "KY": "570",
    "LA": "540",
    "ME": "1320",
    "MD": "660",
    "MA": "960",
    "MI": "390",
    "MN": "330",
    "MS": "330",
    "MO": "450",
    "MT": "450",
    "NE": "480",
    "NV": "930",
    "NH": "480",
    "NJ": "1530",
    "NM": "930",
    "NY": "1740",
    "NC": "420",
    "ND": "630",
    "OH": "510",
    "OK": "570",
    "OR": "960",
    "PA": "690",
    "RI": "900",
    "SC": "570",
    "SD": "540",
    "TN": "420",
    "TX": "390",
    "UT": "540",
    "VT": "1050",
    "VA": "450",
    "WA": "630",
    "WV": "450",
    "WI": "540",
    "WY": "360",
    "DC": "1230"
}

method_of_foreclosure_and_time = { (
    "AL", "Power-of-Sale", 420) , (
    "AK", "Power-of-Sale", 480) , (
    "AZ", "Power-of-Sale", 450) , (
    "AR", "Power-of-Sale", 420) , (
    "CA", "Power-of-Sale", 480) , (
    "CO", "Power-of-Sale", 450) , (
    "CT", "Strict Foreclosure", 660) , (
    "DE", "Judicial", 720) , (
    "FL", "Judicial", 810) , (
    "GA", "Power-of-Sale", 330) , (
    "HI", "Judicial", 900) , (
    "ID", "Judicial", 630) , (
    "IL", "Judicial", 630) , (
    "IN", "Judicial", 540) , (
    "IA", "Judicial", 570) , (
    "KS", "Judicial", 450) , (
    "KY", "Judicial", 570) , (
    "LA", "Judicial", 540) , (
    "ME", "Entry and Possession", 1320) , (
    "MD", "Power-of-Sale", 660) , (
    "MA", "Power-of-Sale", 960) , (
    "MI", "Power-of-Sale", 390) , (
    "MN", "Power-of-Sale", 330) , (
    "MS", "Power-of-Sale", 330) , (
    "MO", "Power-of-Sale", 450) , (
    "MT", "Power-of-Sale", 450) , (
    "NE", "Judicial", 480) , (
    "NV", "Power-of-Sale", 930) , (
    "NH", "Power-of-Sale", 480) , (
    "NJ", "Judicial", 1530) , (
    "NM", "Judicial", 930) , (
    "NY", "Judicial", 1740) , (
    "NC", "Power-of-Sale", 420) , (
    "ND", "Judicial", 630) , (
    "OH", "Judicial", 510) , (
    "OK", "Judicial", 570) , (
    "OR", "Power-of-Sale", 960) , (
    "PA", "Judicial", 690) , (
    "RI", "Power-of-Sale", 900) , (
    "SC", "Judicial", 570) , (
    "SD", "Judicial", 540) , (
    "TN", "Power-of-Sale", 420) , (
    "TX", "Power-of-Sale", 390) , (
    "UT", "Power-of-Sale", 540) , (
    "VT", "Strict Foreclosure", 1050) , (
    "VA", "Power-of-Sale", 450) , (
    "WA", "Power-of-Sale", 630) , (
    "WV", "Power-of-Sale", 450) , (
    "WI", "Power-of-Sale", 540) , (
    "WY", "Power-of-Sale", 360) , (  
    "DC", "Judicial" , 1230)
}