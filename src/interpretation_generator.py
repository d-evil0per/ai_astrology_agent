#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Interpretation Generation Module"""


class InterpretationGenerator:
    def __init__(self):
        pass

    def get_planet_in_sign_interpretation(self, planet_name, sign_name):
        return PLANET_IN_SIGN_INTERPRETATIONS.get(planet_name, {}).get(sign_name, f"No specific interpretation for {planet_name} in {sign_name} available yet.")

    def get_planet_in_house_interpretation(self, planet_name, house_number):
        if not isinstance(house_number, int):
            return f"Invalid house number for {planet_name}."
        return PLANET_IN_HOUSE_INTERPRETATIONS.get(planet_name, {}).get(house_number, f"No specific interpretation for {planet_name} in House {house_number} available yet.")

    def get_aspect_interpretation(self, body1_name, body2_name, aspect_type):
        # Ensure consistent order for lookup
        # key_pair = tuple(sorted((body1_name, body2_name)))
        key_pair = tuple((body1_name, body2_name))
        print(key_pair)
        return ASPECT_INTERPRETATIONS.get(aspect_type, {}).get(key_pair, f"No specific interpretation for {body1_name} {aspect_type} {body2_name} available yet.")

    def get_house_cusp_interpretation(self, house_number, sign_name):
        if not isinstance(house_number, int):
            return f"Invalid house number for cusp interpretation."
        return HOUSE_CUSP_SIGN_INTERPRETATIONS.get(house_number, {}).get(sign_name, f"No specific interpretation for House {house_number} cusp in {sign_name} available yet.")

    def generate_full_interpretation(self, chart_data):
        """Generates a list of interpretations from the chart data."""
        if not chart_data or not isinstance(chart_data, dict):
            return {"error": "Invalid chart data provided."}

        interpretations = {
            "planets_in_signs": [],
            "planets_in_houses": [],
            "aspects": [],
            "house_cusps": []
        }

        # Planet in Sign and Planet in House
        for planet_data in chart_data.get("planets", []):
            p_name = planet_data.get("name")
            p_sign = planet_data.get("sign")
            p_house = planet_data.get("house_number")

            if p_name and p_sign:
                interp_sign = self.get_planet_in_sign_interpretation(p_name, p_sign)
                interpretations["planets_in_signs"].append(f"{p_name} in {p_sign}: {interp_sign}")
            
            if p_name and p_house is not None:
                interp_house = self.get_planet_in_house_interpretation(p_name, p_house)
                interpretations["planets_in_houses"].append(f"{p_name} in House {p_house}: {interp_house}")
        
        # Aspects
        for aspect_data in chart_data.get("aspects", []):
            b1 = aspect_data.get("body1")
            b2 = aspect_data.get("body2")
            a_type = aspect_data.get("aspect_type")
            if b1 and b2 and a_type:
                interp_aspect = self.get_aspect_interpretation(b1, b2, a_type)
                interpretations["aspects"].append(f"{b1} {a_type} {b2}: {interp_aspect}")

        # House Cusps
        for house_data in chart_data.get("houses", []):
            h_num = house_data.get("house_number")
            h_sign = house_data.get("sign")
            if h_num is not None and h_sign:
                interp_cusp = self.get_house_cusp_interpretation(h_num, h_sign)
                interpretations["house_cusps"].append(f"House {h_num} cusp in {h_sign}: {interp_cusp}")
        
        # Ascendant and Midheaven specific interpretations (can be treated as house cusps or special points)
        asc_data = chart_data.get("ascendant")
        if asc_data and asc_data.get("sign"):
            asc_interp = self.get_house_cusp_interpretation(1, asc_data.get("sign")) # Asc is cusp of 1st
            interpretations["house_cusps"].append(f"Ascendant in {asc_data.get('sign')}: {asc_interp}")

        mc_data = chart_data.get("midheaven")
        if mc_data and mc_data.get("sign"):
            mc_interp = self.get_house_cusp_interpretation(10, mc_data.get("sign")) # MC is cusp of 10th
            interpretations["house_cusps"].append(f"Midheaven (MC) in {mc_data.get('sign')}: {mc_interp}")

        return interpretations



