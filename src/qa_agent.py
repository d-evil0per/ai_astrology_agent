#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""AI Question Answering Agent for Astrology Charts"""

import spacy
from .interpretation_generator import InterpretationGenerator # Assuming it's in the same directory or package
from .chart_calculator import PLANETS as ASTRO_PLANETS_DETAILS # Import for planet names
from .chart_calculator import SIGNS as ASTRO_SIGNS_DETAILS # Import for sign names

# Load spaCy model
# Ensure you have run: python -m spacy download en_core_web_sm
NLP = spacy.load("en_core_web_sm")

# Keywords for life areas and their mapping to chart elements
LIFE_AREA_KEYWORDS = {
    "career": ["10th house", "midheaven", "mc", "saturn"],
    "love": ["venus", "5th house", "7th house"],
    "relationships": ["venus", "7th house", "descendant"],
    "money": ["2nd house", "venus", "jupiter"],
    "finances": ["2nd house", "8th house", "pluto"],
    "health": ["6th house", "1st house", "ascendant"],
    "self": ["1st house", "ascendant", "sun", "rising sign"],
    "emotions": ["moon", "cancer", "4th house"],
    "communication": ["mercury", "3rd house", "gemini"],
    "home": ["4th house", "moon", "cancer"],
    "family": ["4th house", "moon"],
    "creativity": ["5th house", "venus", "leo"],
    "children": ["5th house"],
    "work": ["6th house", "mercury", "virgo"],
    "partnerships": ["7th house", "venus", "libra"],
    "transformation": ["8th house", "pluto", "scorpio"],
    "shared resources": ["8th house"],
    "philosophy": ["9th house", "jupiter", "sagittarius"],
    "travel": ["9th house", "jupiter"],
    "higher education": ["9th house"],
    "public image": ["10th house", "midheaven", "mc"],
    "ambition": ["10th house", "saturn", "mars"],
    "friendships": ["11th house", "uranus", "aquarius"],
    "groups": ["11th house"],
    "spirituality": ["12th house", "neptune", "pisces"],
    "subconscious": ["12th house"]
}

# Standardize entity names for internal use
PLANET_NAMES_STANDARDIZED = {name.lower(): name for name in ASTRO_PLANETS_DETAILS.keys()}
PLANET_NAMES_STANDARDIZED["north node"] = "MeanNode"
PLANET_NAMES_STANDARDIZED["true node"] = "TrueNode" # If you decide to use it
PLANET_NAMES_STANDARDIZED["chiron"] = "Chiron" # If you decide to use it
PLANET_NAMES_STANDARDIZED["asc"] = "Ascendant"
PLANET_NAMES_STANDARDIZED["mc"] = "Midheaven"
PLANET_NAMES_STANDARDIZED["rising sign"] = "Ascendant"

SIGN_NAMES_STANDARDIZED = {name.lower(): name for name in ASTRO_SIGNS_DETAILS}

HOUSE_KEYWORDS = {}
for i in range(1, 13):
    HOUSE_KEYWORDS[f"{i}st house" if i == 1 else f"{i}nd house" if i == 2 else f"{i}rd house" if i == 3 else f"{i}th house"] = i
    HOUSE_KEYWORDS[f"house {i}"] = i

ASPECT_NAMES_STANDARDIZED = {
    "conjunction": "Conjunction", "conjunct": "Conjunction",
    "sextile": "Sextile",
    "square": "Square",
    "trine": "Trine",
    "opposition": "Opposition", "opposed": "Opposition"
}

ASTROLOGICAL_ENTITY_KEYWORDS = list(PLANET_NAMES_STANDARDIZED.keys()) + \
                               list(SIGN_NAMES_STANDARDIZED.keys()) + \
                               list(HOUSE_KEYWORDS.keys()) + \
                               list(ASPECT_NAMES_STANDARDIZED.keys())

class QAAgent:
    def __init__(self, chart_data):
        self.chart_data = chart_data
        self.interpreter = InterpretationGenerator()
        # Generate interpretations once when the agent is initialized with chart data
        if self.chart_data and not self.chart_data.get("error"):
            self.full_interpretations = self.interpreter.generate_full_interpretation(self.chart_data)
        else:
            self.full_interpretations = {"error": "Chart data is invalid or missing."}

    def _extract_entities(self, question_text):
        doc = NLP(question_text.lower())
        entities = {
            "planets": set(),
            "signs": set(),
            "houses": set(), # Stores house numbers (int)
            "aspect_types": set(),
            "life_areas": set(),
            "raw_keywords": set() # For general keyword matching if specific entities are not clear
        }

        # Lemmatize and check for known astrological keywords
        lemmatized_tokens = [token.lemma_ for token in doc]
        question_lower = " ".join(lemmatized_tokens)

        for keyword in ASTROLOGICAL_ENTITY_KEYWORDS:
            if keyword in question_lower:
                if keyword in PLANET_NAMES_STANDARDIZED:
                    entities["planets"].add(PLANET_NAMES_STANDARDIZED[keyword])
                elif keyword in SIGN_NAMES_STANDARDIZED:
                    entities["signs"].add(SIGN_NAMES_STANDARDIZED[keyword])
                elif keyword in HOUSE_KEYWORDS:
                    entities["houses"].add(HOUSE_KEYWORDS[keyword])
                elif keyword in ASPECT_NAMES_STANDARDIZED:
                    entities["aspect_types"].add(ASPECT_NAMES_STANDARDIZED[keyword])
        
        # Check for life area keywords
        for area, area_keywords_list in LIFE_AREA_KEYWORDS.items():
            if any(ak_word in question_text.lower() for ak_word in area_keywords_list):
                entities["life_areas"].add(area)
        
        # Store all nouns and proper nouns as raw keywords for broader matching if needed
        for token in doc:
            if token.pos_ in ["NOUN", "PROPN"]:
                entities["raw_keywords"].add(token.lemma_)

        return entities

    def answer_question(self, question_text):
        if self.full_interpretations.get("error"):
            return f'I cannot answer questions right now because: {self.full_interpretations["error"]}'

        entities = self._extract_entities(question_text)
        answer_parts = []
        found_answer = False

        # 1. Direct question about a planet in a sign (e.g., "Sun in Aries")
        if len(entities["planets"]) == 1 and len(entities["signs"]) == 1 and not entities["houses"] and not entities["aspect_types"] and not entities["life_areas"]:
            planet = list(entities["planets"])[0]
            sign = list(entities["signs"])[0]
            for interp in self.full_interpretations.get("planets_in_signs", []):
                if planet.lower() in interp.lower() and sign.lower() in interp.lower():
                    answer_parts.append(interp)
                    found_answer = True
            if not found_answer:
                 answer_parts.append(f"Checking your chart for {planet} in {sign}... Based on your chart, your {planet} is in {self._get_planet_sign(planet)}. {self.interpreter.get_planet_in_sign_interpretation(planet, self._get_planet_sign(planet))}")
                 found_answer = True # Provided general info

        # 2. Direct question about a planet in a house (e.g., "Mars in 7th house")
        elif len(entities["planets"]) == 1 and len(entities["houses"]) == 1 and not entities["signs"] and not entities["aspect_types"] and not entities["life_areas"]:
            planet = list(entities["planets"])[0]
            house = list(entities["houses"])[0]
            for interp in self.full_interpretations.get("planets_in_houses", []):
                if planet.lower() in interp.lower() and (f"house {house}" in interp.lower() or f"House {house}" in interp.lower()):
                    answer_parts.append(interp)
                    found_answer = True
            if not found_answer:
                actual_house = self._get_planet_house(planet)
                if actual_house is not None:
                    answer_parts.append(f"Checking your chart for {planet} in house {house}... Your {planet} is in house {actual_house}. {self.interpreter.get_planet_in_house_interpretation(planet, actual_house)}")
                else:
                    answer_parts.append(f"I couldn\'t find {planet} in your chart data to confirm its house placement.")
                found_answer = True
        
        # 3. Question about a specific planet (e.g., "Tell me about my Sun")
        elif len(entities["planets"]) == 1 and not entities["signs"] and not entities["houses"] and not entities["aspect_types"] and not entities["life_areas"]:
            planet = list(entities["planets"])[0]
            p_sign = self._get_planet_sign(planet)
            p_house = self._get_planet_house(planet)
            if p_sign:
                answer_parts.append(self.interpreter.get_planet_in_sign_interpretation(planet, p_sign))
            if p_house is not None:
                 answer_parts.append(self.interpreter.get_planet_in_house_interpretation(planet, p_house))
            # Add aspects involving this planet
            for interp in self.full_interpretations.get("aspects", []):
                if planet.lower() in interp.lower(): # Simple check, might need refinement
                    answer_parts.append(interp)
            if answer_parts: found_answer = True

        # 4. Question about a specific house (e.g., "What about my 10th house?")
        elif len(entities["houses"]) == 1 and not entities["planets"] and not entities["signs"] and not entities["aspect_types"] and not entities["life_areas"]:
            house_num = list(entities["houses"])[0]
            # Get cusp interpretation
            cusp_sign = self._get_house_cusp_sign(house_num)
            if cusp_sign:
                answer_parts.append(self.interpreter.get_house_cusp_interpretation(house_num, cusp_sign))
            # Get planets in that house
            planets_in_house_text = []
            for p_data in self.chart_data.get("planets", []):
                if p_data.get("house_number") == house_num:
                    planet_name = p_data.get("name")
                    planet_sign = p_data.get("sign")
                    # Construct the ordinal string correctly
                    s = str(house_num)
                    if s.endswith("1") and not s.endswith("11"): suffix = "st"
                    elif s.endswith("2") and not s.endswith("12"): suffix = "nd"
                    elif s.endswith("3") and not s.endswith("13"): suffix = "rd"
                    else: suffix = "th"
                    planets_in_house_text.append(f"{planet_name} in {planet_sign} is in your {house_num}{suffix} house. {self.interpreter.get_planet_in_house_interpretation(planet_name, house_num)}")
            if planets_in_house_text:
                answer_parts.append("Planets in this house:")
                answer_parts.extend(planets_in_house_text)
            if answer_parts: found_answer = True

        # 5. Question about a life area (e.g., "Tell me about my career")
        elif entities["life_areas"]:
            for area in entities["life_areas"]:
                answer_parts.append(f"Regarding {area}:")
                related_chart_elements_keywords = LIFE_AREA_KEYWORDS.get(area, [])
                area_interps_found = False
                for element_keyword in related_chart_elements_keywords:
                    # Search for interpretations related to this element keyword
                    for category, interps_list in self.full_interpretations.items():
                        if isinstance(interps_list, list):
                            for interp_text_item in interps_list:
                                if element_keyword.lower() in interp_text_item.lower():
                                    answer_parts.append(f"- {interp_text_item}")
                                    area_interps_found = True
                if not area_interps_found:
                    answer_parts.append(f"I don't have a specific pre-generated interpretation for all aspects of '{area}' right now, but it's generally associated with elements like {', '.join(related_chart_elements_keywords)}. You can ask about these specific elements.")
            if answer_parts: found_answer = True
        
        # 6. Question about an aspect type or specific aspect
        elif entities["aspect_types"]:
            # If specific planets are also mentioned for the aspect
            if len(entities["planets"]) >= 2 and len(entities["aspect_types"]) == 1:
                p_list = list(entities["planets"])[:2]
                aspect_t = list(entities["aspect_types"])[0]
                for interp in self.full_interpretations.get("aspects", []):
                    # Check if both planets and the aspect type are in the interpretation string
                    if all(p.lower() in interp.lower() for p in p_list) and aspect_t.lower() in interp.lower():
                        answer_parts.append(interp)
                        found_answer = True
            # General question about an aspect type
            elif len(entities["aspect_types"]) == 1 and not entities["planets"]:
                aspect_t = list(entities["aspect_types"])[0]
                answer_parts.append(f"Aspects of type \'{aspect_t}\' in your chart:")
                aspects_found_for_type = False
                for interp in self.full_interpretations.get("aspects", []):
                    if aspect_t.lower() in interp.lower():
                        answer_parts.append(f"- {interp}")
                        aspects_found_for_type = True
                if not aspects_found_for_type:
                    answer_parts.append(f"No specific \'{aspect_t}\' aspects were highlighted in the general interpretation. You can ask about aspects between specific planets.")
                found_answer = True

        # Fallback or if no specific logic branch was fully satisfied
        if not found_answer or not answer_parts:
            if entities["raw_keywords"] and not found_answer:
                # Try a very general keyword search in interpretations if nothing else matched
                matched_by_keyword = False
                for kw in entities["raw_keywords"]:
                    for category, interps_list in self.full_interpretations.items():
                        if isinstance(interps_list, list):
                            for interp_text_item in interps_list:
                                if kw in interp_text_item.lower() and interp_text_item not in answer_parts:
                                    if not matched_by_keyword: # Add header only once
                                        answer_parts.append("Based on the keywords in your question, here are some potentially relevant interpretations from your chart:")
                                    answer_parts.append(f"- {interp_text_item}")
                                    matched_by_keyword = True
                if matched_by_keyword: found_answer = True
            
            if not found_answer:
                answer_parts = ["""I can provide information about specific planets, signs, houses, aspects, or general life areas in your chart. Could you please rephrase or specify what you\'d like to know? For example, 
                \'Tell me about my Sun in Aries\' or 
                \'What about my career prospects?\'"""] 

        return "\n".join(answer_parts)

    # Helper methods to get specific data from chart_data for QA logic
    def _get_planet_sign(self, planet_name_query):
        standard_name = PLANET_NAMES_STANDARDIZED.get(planet_name_query.lower())
        if not standard_name: return None
        if standard_name == "Ascendant":
            return self.chart_data.get("ascendant", {}).get("sign")
        if standard_name == "Midheaven":
            return self.chart_data.get("midheaven", {}).get("sign")
        for p in self.chart_data.get("planets", []):
            if p.get("name") == standard_name:
                return p.get("sign")
        return None

    def _get_planet_house(self, planet_name_query):
        standard_name = PLANET_NAMES_STANDARDIZED.get(planet_name_query.lower())
        if not standard_name: return None
        # Ascendant is cusp of 1st, Midheaven is cusp of 10th - not *in* a house itself by this logic
        if standard_name in ["Ascendant", "Midheaven"]: return None 
        for p in self.chart_data.get("planets", []):
            if p.get("name") == standard_name:
                return p.get("house_number")
        return None

    def _get_house_cusp_sign(self, house_num_query):
        if not isinstance(house_num_query, int): return None
        if house_num_query == 1 and "ascendant" in self.chart_data:
             return self.chart_data["ascendant"].get("sign")
        if house_num_query == 10 and "midheaven" in self.chart_data:
             return self.chart_data["midheaven"].get("sign")
        for h in self.chart_data.get("houses", []):
            if h.get("house_number") == house_num_query:
                return h.get("sign")
        return None

# --- Example Usage (for testing, assuming chart_calculator and interpretation_generator are in the same path) ---
if __name__ == "__main__":
    # This requires chart_calculator.py and interpretation_generator.py to be accessible
    # For standalone testing, you might need to adjust imports or provide a mock chart_data
    # from chart_calculator import ChartCalculator # Assuming chart_calculator.py is in src

    # calculator = ChartCalculator() # Uses default ephe path and API key path
    sample_chart_data_for_qa = {
        "birth_data": {
            "date": "1990-01-01", "time": "12:00", "city_country": "New York, USA",
            "latitude": 40.7128, "longitude": -74.0060, "timezone_str": "America/New_York",
            "utc_datetime": "1990-01-01T17:00:00+00:00", "julian_day_ut": 2447892.2083333335
        },
        "planets": [
            {"name": "Sun", "longitude": 280.0, "sign": "Capricorn", "sign_long_deg": 10, "house_number": 10, "speed": 1.0},
            {"name": "Moon", "longitude": 15.0, "sign": "Aries", "sign_long_deg": 15, "house_number": 1, "speed": 12.0},
            {"name": "Mars", "longitude": 215.0, "sign": "Scorpio", "sign_long_deg": 5, "house_number": 7, "speed": 0.5}
        ],
        "houses": [
            {"house_number": 1, "longitude": 0.0, "sign": "Aries"}, 
            {"house_number": 7, "longitude": 180.0, "sign": "Libra"}, 
            {"house_number": 10, "longitude": 270.0, "sign": "Capricorn"}
        ],
        "aspects": [
            {"body1": "Sun", "body2": "Moon", "aspect_type": "Square", "orb": 1.0, "is_applying": False}
        ],
        "ascendant": {"longitude": 0.0, "sign": "Aries"},
        "midheaven": {"longitude": 270.0, "sign": "Capricorn"}
    }
    # In a real scenario, chart_data would come from ChartCalculator
    # try:
    #     # chart_data = calculator.calculate_natal_chart(1990, 1, 1, 12, 0, "New York, NY, USA")
    #     # For testing, ensure chart_calculator.py is runnable and produces expected output structure
    #     pass
    # except Exception as e:
    #     print(f"Error generating chart for QA test: {e}")
    #     # chart_data = sample_chart_data_for_qa # Fallback to sample if calculation fails

    qa_agent = QAAgent(sample_chart_data_for_qa)

    questions = [
        "Tell me about my Sun sign.",
        "What is my Sun in Capricorn like?",
        "What about Mars in my 7th house?",
        "How is my career looking?",
        "What does Sun square Moon mean?",
        "Tell me about my 1st house.",
        "What is my rising sign?",
        "gibberish question here"
    ]

    for q in questions:
        print(f"\nQ: {q}")
        answer = qa_agent.answer_question(q)
        print(f"A: {answer}")

