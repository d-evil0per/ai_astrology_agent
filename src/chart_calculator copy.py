#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Core Astrological Chart Calculation Engine"""

import swisseph as swe
import datetime
import pytz
from timezonefinder import TimezoneFinder
import requests
import json 
import os
from dotenv import load_dotenv
load_dotenv()

# --- Constants ---
PLANETS = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mercury": swe.MERCURY,
    "Venus": swe.VENUS,
    "Mars": swe.MARS,
    "Jupiter": swe.JUPITER,
    "Saturn": swe.SATURN,
    "Uranus": swe.URANUS,
    "Neptune": swe.NEPTUNE,
    "Pluto": swe.PLUTO,
    "MeanNode": swe.MEAN_NODE, # North Node
    "TrueNode": swe.TRUE_NODE,
    "Chiron": swe.CHIRON,
    "Lilith": swe.MEAN_APOG,     # Black Moon Lilith (Mean)
   # Calculated
    # Optional: Add asteroids using ephemeris numbers
    # "Ceres": 10001,
    # "Pallas": 10002,
    # "Juno": 10003,
    # "Vesta": 10004
}

ASPECT_DEGREES = {
    "Conjunction": 0,
    "Sextile": 60,
    "Square": 90,
    "Trine": 120,
    "Opposition": 180
}

ORBS = {
    # Luminaries
    "Sun": {"Conjunction": 10, "Sextile": 6, "Square": 8, "Trine": 8, "Opposition": 10},
    "Moon": {"Conjunction": 10, "Sextile": 6, "Square": 8, "Trine": 8, "Opposition": 10},

    # Inner planets
    "Mercury": {"Conjunction": 7, "Sextile": 4, "Square": 6, "Trine": 6, "Opposition": 7},
    "Venus": {"Conjunction": 7, "Sextile": 4, "Square": 6, "Trine": 6, "Opposition": 7},
    "Mars": {"Conjunction": 8, "Sextile": 5, "Square": 7, "Trine": 7, "Opposition": 8},

    # Outer planets
    "Jupiter": {"Conjunction": 9, "Sextile": 5, "Square": 7, "Trine": 7, "Opposition": 9},
    "Saturn": {"Conjunction": 8, "Sextile": 4, "Square": 6, "Trine": 6, "Opposition": 8},
    "Uranus": {"Conjunction": 5, "Sextile": 3, "Square": 5, "Trine": 5, "Opposition": 5},
    "Neptune": {"Conjunction": 5, "Sextile": 3, "Square": 5, "Trine": 5, "Opposition": 5},
    "Pluto": {"Conjunction": 5, "Sextile": 2, "Square": 4, "Trine": 4, "Opposition": 5},

    # Lunar Nodes
    "MeanNode": {"Conjunction": 3, "Sextile": 2, "Square": 3, "Trine": 3, "Opposition": 3},
    "TrueNode": {"Conjunction": 3, "Sextile": 2, "Square": 3, "Trine": 3, "Opposition": 3},

    # Asteroids & Points
    "Chiron": {"Conjunction": 3, "Sextile": 2, "Square": 3, "Trine": 3, "Opposition": 3},
    "Lilith": {"Conjunction": 2, "Sextile": 1, "Square": 2, "Trine": 2, "Opposition": 2},
    "TrueLilith": {"Conjunction": 2, "Sextile": 1, "Square": 2, "Trine": 2, "Opposition": 2},

    # Angles
    "Ascendant": {"Conjunction": 6, "Sextile": 3, "Square": 5, "Trine": 5, "Opposition": 6},
    "Midheaven": {"Conjunction": 6, "Sextile": 3, "Square": 5, "Trine": 5, "Opposition": 6},
}

DEFAULT_ORB = {
    "Conjunction": 3,
    "Sextile": 2,
    "Square": 3,
    "Trine": 3,
    "Opposition": 3
}
SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
EPHEMERIS_PATH = os.path.join(project_dir, "data","ephe")
GEOCODE_API_KEY = os.environ.get('GEOCODE_KEY')



# --- Helper Functions ---
def degree_to_dms_sign(longitude):
    """Converts a decimal degree longitude to sign, degree, minute, second."""
    sign_index = int(longitude / 30)
    sign = SIGNS[sign_index]
    pos_in_sign = longitude % 30
    deg = int(pos_in_sign)
    minute_decimal = (pos_in_sign - deg) * 60
    minute = int(minute_decimal)
    second_decimal = (minute_decimal - minute) * 60
    second = int(round(second_decimal))
    if second == 60:
        minute += 1
        second = 0
    if minute == 60:
        deg +=1
        minute = 0
    # if deg == 30, it rolls over, but this should be handled by sign_index already
    return sign, deg, minute, second

# --- Core Functions ---
class ChartCalculator:
    def __init__(self, ephemeris_path=EPHEMERIS_PATH, geocode_api_key=GEOCODE_API_KEY):
        swe.set_ephe_path(ephemeris_path)
        try:
            # with open(geocode_api_key_path, "r") as f:
            self.geocode_api_key = GEOCODE_API_KEY
        except FileNotFoundError:
            print(f"ERROR: Geocode API key file not found ")
            self.geocode_api_key = None
        self.tf = TimezoneFinder()

    def get_coordinates_and_timezone(self, city_country_str):
        """Gets latitude, longitude, and timezone for a given city, country string."""
        if not self.geocode_api_key:
            raise ValueError("Geocode API key is not set.")
        
        url = f"https://geocode.maps.co/search?q={city_country_str}&api_key={self.geocode_api_key}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            if data and isinstance(data, list) and len(data) > 0:
                location = data[0]
                lat = float(location.get("lat"))
                lon = float(location.get("lon"))

                timezone_str = self.tf.timezone_at(lng=lon, lat=lat)
                if not timezone_str:
                    # Fallback if timezonefinder fails
                    offset_hours = int(lon / 15)
                    timezone_str = f"Etc/GMT{+offset_hours:+d}"  # Fixed sign direction
                    print(f"Warning: Could not determine precise timezone for {city_country_str}. Using estimated {timezone_str}.")
                
                return lat, lon, timezone_str
            else:
                raise ValueError(f"Could not geocode location: {city_country_str}. Response: {data}")
        
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Geocoding API request failed: {e}")
        
        except (json.JSONDecodeError, KeyError, IndexError, TypeError, ValueError) as e:
            raise ValueError(f"Error processing geocoding API response: {e}. Response: {response.text if 'response' in locals() else 'No response'}")
    def get_utc_datetime_and_julian_day(self, year, month, day, hour, minute, lat, lon, timezone_str, second=0):
        """Converts local time to UTC and calculates Julian Day (UT)."""
        try:
            local_tz = pytz.timezone(timezone_str)
        except pytz.exceptions.UnknownTimeZoneError:
            raise ValueError(f"Unknown timezone: {timezone_str}")

        local_dt = datetime.datetime(year, month, day, hour, minute, second)
        
        try:
            # Handle ambiguous or non-existent local times (DST)
            localized_dt = local_tz.localize(local_dt, is_dst=None)
        except (pytz.exceptions.AmbiguousTimeError, pytz.exceptions.NonExistentTimeError) as e:
            try:
                localized_dt = local_tz.localize(local_dt, is_dst=False)
                print(f"Warning: Ambiguous or non-existent local time {local_dt} in {timezone_str}. Used standard time. Details: {e}")
            except Exception as e_inner:
                raise ValueError(f"Could not resolve ambiguous/non-existent local time {local_dt} in {timezone_str}: {e_inner}")

        utc_dt = localized_dt.astimezone(pytz.utc)

        # Convert to Julian Day (ET, UT) — we're using UT (index [1])
        jd_et, jd_ut = swe.utc_to_jd(
            utc_dt.year, utc_dt.month, utc_dt.day,
            utc_dt.hour, utc_dt.minute, utc_dt.second, 1  # 1 for Gregorian calendar
        )

        return utc_dt, jd_ut

    def calculate_natal_chart(self, year, month, day, hour, minute, city_country_str):
        """Calculates a full natal chart."""
        lat, lon, timezone_str = self.get_coordinates_and_timezone(city_country_str)
        utc_dt, jd_ut = self.get_utc_datetime_and_julian_day(year, month, day, hour, minute, lat, lon, timezone_str)
        print(lat, lon, timezone_str)
        chart_data = {
            "birth_data": {
                "date": f"{year:04d}-{month:02d}-{day:02d}",
                "time": f"{hour:02d}:{minute:02d}",
                "city_country": city_country_str,
                "latitude": lat,
                "longitude": lon,
                "timezone_str": timezone_str,
                "utc_datetime": utc_dt.isoformat(),
                "julian_day_ut": jd_ut
            },
            "planets": [],
            "houses": [],
            "aspects": [],
            "ascendant": {},
            "midheaven": {}
        }

        # Calculate Planets
        swe.set_topo(lon, lat, 0) # Topocentric correction
        iflag = swe.FLG_SWIEPH | swe.FLG_SPEED # Use Swiss Ephemeris, calculate speed for retrograde
        
        planet_positions_for_aspects = {}

        for name, p_id in PLANETS.items():
            xx, rflags = swe.calc_ut(jd_ut, p_id, iflag)
            longitude = xx[0]
            is_retrograde = xx[3] < 0
            sign, deg, min_arc, sec_arc = degree_to_dms_sign(longitude)
            
            # House placement will be determined after houses are calculated
            chart_data["planets"].append({
                "name": name,
                "longitude": longitude,
                "sign": sign,
                "sign_long_deg": deg, # Degree within the sign
                "sign_min": min_arc,
                "sign_sec": sec_arc,
                "is_retrograde": is_retrograde,
                "speed": xx[3],
                "house_number": None # Placeholder
            })
            planet_positions_for_aspects[name] = longitude

        # Calculate Houses (Placidus system by default)
        # For house calculation, swe.houses_ex needs Julian Day in ET (Ephemeris Time)
        # Delta T is the difference ET - UT. swe.get_tid_acc() can give it, or swe.deltat(jd_ut)
        delta_t = swe.deltat(jd_ut) 
        jd_et = jd_ut + delta_t
        # Before the swe.houses_ex call
        print(f"jd_et: {jd_et}")
        print(f"lat: {lat}, lon: {lon}")
        print(f"iflag: {iflag}")
        # House cusps, ascendant, mc, armc, vertex
        # Note: swe.houses returns cusps 1-12, Asc, MC, ARMC, Vertex, Equatorial Asc, co-Asc Koch, co-Asc Munkasey, Polar Asc
        # We are interested in cusps[1] to cusps[12] for house cusps 1-12
        # ascmc is an array: Asc, MC, ARMC, Vertex, Equat. Asc., Co-Asc. (Koch), Co-Asc. (Munkasey), Polar Asc.
        cusps, ascmc = swe.houses_ex(jd_et, lat, lon, b'P', iflag) # 'P' for Placidus
        print(f"cusps: {cusps}")
        print(f"ascmc: {ascmc}")

        # Check the length of cusps
        if len(cusps) < 12:
            raise ValueError(f"Expected 13 cusps (0-12), but got {len(cusps)}: {cusps}")
        for i in range(12):
            sign, deg, min_arc, sec_arc = degree_to_dms_sign(cusps[i])
            chart_data["houses"].append({
                "house_number": i+1,
                "longitude": cusps[i],
                "sign": sign,
                "sign_long_deg": deg,
                "sign_min": min_arc,
                "sign_sec": sec_arc
            })
        
        # Ascendant and Midheaven
        asc_long = ascmc[0]
        mc_long = ascmc[1]
        sign_asc, deg_asc, min_asc, sec_asc = degree_to_dms_sign(asc_long)
        sign_mc, deg_mc, min_mc, sec_mc = degree_to_dms_sign(mc_long)

        chart_data["ascendant"] = {"longitude": asc_long, "sign": sign_asc, "sign_long_deg": deg_asc, "sign_min": min_asc, "sign_sec": sec_asc}
        chart_data["midheaven"] = {"longitude": mc_long, "sign": sign_mc, "sign_long_deg": deg_mc, "sign_min": min_mc, "sign_sec": sec_mc}
        
        planet_positions_for_aspects["Ascendant"] = asc_long
        planet_positions_for_aspects["Midheaven"] = mc_long

        # Determine planet house positions
        for planet_entry in chart_data["planets"]:
            planet_long = planet_entry["longitude"]
            house_num = None
            # Iterate through house cusps to find the house
            # A planet is in house H if its longitude is between cusp H and cusp H+1 (circularly)
            for i in range(12):
                cusp_current_long = chart_data["houses"][i]["longitude"]
                cusp_next_idx = (i + 1) % 12
                cusp_next_long = chart_data["houses"][cusp_next_idx]["longitude"]
                
                # Handle wrap-around 0/360 degrees for cusp ranges
                if cusp_current_long <= cusp_next_long: # Normal case, e.g. cusp1=10, cusp2=40
                    if cusp_current_long <= planet_long < cusp_next_long:
                        house_num = i + 1
                        break
                else: # Wrap-around case, e.g. cusp12=330, cusp1=20
                    if planet_long >= cusp_current_long or planet_long < cusp_next_long:
                        house_num = i + 1
                        break
            planet_entry["house_number"] = house_num

        # Calculate Aspects
        # Consider aspects between all PLANETS and also to Ascendant and Midheaven
        # For simplicity, only major aspects: Conjunction, Sextile, Square, Trine, Opposition
        
        # Create a list of (name, longitude) for all bodies involved in aspects
        bodies_for_aspects = []
        for p_name, p_long in planet_positions_for_aspects.items():
            bodies_for_aspects.append((p_name, p_long))
        
        # Avoid duplicate aspects (e.g. Sun-Moon is same as Moon-Sun)
        calculated_aspect_pairs = set()

        for i in range(len(bodies_for_aspects)):
            body1_name, body1_long = bodies_for_aspects[i]
            for j in range(i + 1, len(bodies_for_aspects)):
                body2_name, body2_long = bodies_for_aspects[j]
                
                pair_key = tuple(sorted((body1_name, body2_name)))
                if pair_key in calculated_aspect_pairs:
                    continue

                angular_separation = abs(body1_long - body2_long)
                if angular_separation > 180:
                    angular_separation = 360 - angular_separation
                
                for aspect_name, aspect_degree in ASPECT_DEGREES.items():
                    # Determine orb: prioritize specific body1, then body2, then default
                    orb1 = ORBS.get(body1_name, DEFAULT_ORB).get(aspect_name, DEFAULT_ORB.get(aspect_name, 1))
                    orb2 = ORBS.get(body2_name, DEFAULT_ORB).get(aspect_name, DEFAULT_ORB.get(aspect_name, 1))
                    # Use the tighter orb of the two planets involved, or a general orb if one is an angle
                    # For simplicity, let's average them or take the smaller one. Taking smaller one for stricter aspects.
                    # A more common approach is to use the orb of the faster moving planet, or a combined orb.
                    # For now, let's use a simplified approach: use the orb of body1 if it's a planet, else body2, else default.
                    # A better approach: use the orb associated with the *aspect type* for the *pair* of bodies.
                    # For now, we'll use the orb of the first planet in the pair for that aspect type.
                    # A common way is to sum half orbs of each planet.
                    # Let's use a simpler method: take the orb of the first planet listed in ORBS for that aspect.
                    # Or, more simply, use the orb defined for the first planet in the pair.
                    
                    # Simplified orb: use the orb of the first planet in the pair for that aspect type
                    # If body1 is an angle, its orb might be different. We defined orbs for Asc/MC too.
                    current_orb = ORBS.get(body1_name, {}).get(aspect_name, ORBS.get(body2_name, {}).get(aspect_name, DEFAULT_ORB.get(aspect_name,1)))
                    
                    if abs(angular_separation - aspect_degree) <= current_orb:
                        # To determine applying/separating, we need speeds. We have speeds for planets.
                        # For Asc/MC, speed is not directly applicable in the same way.
                        # For now, we'll skip applying/separating for aspects to Asc/MC.
                        is_applying = None
                        if body1_name in PLANETS and body2_name in PLANETS:
                            speed1 = next(p["speed"] for p in chart_data["planets"] if p["name"] == body1_name)
                            speed2 = next(p["speed"] for p in chart_data["planets"] if p["name"] == body2_name)
                            # This is a simplified check. True applying/separating is more complex.
                            # If faster planet is moving towards aspect with slower, it's applying.
                            # This needs to consider relative speeds and direction to the exact aspect degree.
                            # For now, a placeholder or a very basic check.
                            # A common simplification: if the faster planet has not yet reached the aspect degree but is within orb, it's applying.
                            # If it has passed the aspect degree but is still within orb, it's separating.
                            # This requires knowing which planet is faster and their relative positions to the exact aspect.
                            # For simplicity, we'll leave it None for now or implement a basic version later.
                            pass # is_applying logic needs more refinement

                        chart_data["aspects"].append({
                            "body1": body1_name,
                            "body2": body2_name,
                            "aspect_type": aspect_name,
                            "orb": round(abs(angular_separation - aspect_degree), 2),
                            "is_applying": is_applying # Placeholder
                        })
                        calculated_aspect_pairs.add(pair_key)
                        break # Found an aspect, move to next pair
        swe.close()
        return chart_data

# --- Example Usage (for testing) ---
if __name__ == "__main__":
    calculator = ChartCalculator()
    # try:
        # Test 1: Albert Einstein
    # print("\nCalculating for Albert Einstein (Ulm, Germany, March 14, 1879, 11:30 AM)")
    # einstein_chart = calculator.calculate_natal_chart(1879, 3, 14, 11, 30, "Ulm, Germany")
    # print(json.dumps(einstein_chart, indent=2))

    # Test 2: A known example, e.g., from Astro.com for verification
    # Example: New York, NY, USA, Jan 1, 2000, 12:00 PM
    print("\nCalculating for New York, Jan 1, 2000, 12:00 PM")
    ny_chart = calculator.calculate_natal_chart(1994, 3, 24, 00, 40, "Jamshedpur, Jharkhand, India")
    print(json.dumps(ny_chart, indent=2))
        
        # Test 3: Location that might cause timezone issues or geocoding challenges
        # print("\nCalculating for Kiritimati, Kiribati, Jan 1, 2000, 00:00 AM")
        # kiritimati_chart = calculator.calculate_natal_chart(2000, 1, 1, 0, 0, "Kiritimati, Kiribati")
        # print(json.dumps(kiritimati_chart, indent=2))

    # except ValueError as e:
    #     print(f"Error: {e}")
    # except Exception as e:
    #     print(f"An unexpected error occurred: {e}")

