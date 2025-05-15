#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Vedic Astrology Chart Calculation Engine"""

import swisseph as swe
import datetime
import pytz
from timezonefinder import TimezoneFinder
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

# --- Vedic Constants ---
PLANETS = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mercury": swe.MERCURY,
    "Venus": swe.VENUS,
    "Mars": swe.MARS,
    "Jupiter": swe.JUPITER,
    "Saturn": swe.SATURN,
    "Rahu": swe.MEAN_NODE,  # North Node (MeanNode renamed to Rahu)
    "Ketu": swe.MEAN_NODE,  # South Node (calculated as 180° opposite Rahu)
    # Removed Uranus, Neptune, Pluto, Chiron, Lilith for Vedic focus
}

SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

NAKSHATRAS = [
    ("Ashwini", 0, 13 + 20/60), ("Bharani", 13 + 20/60, 26 + 40/60),
    ("Krittika", 26 + 40/60, 40), ("Rohini", 40, 53 + 20/60),
    ("Mrigashira", 53 + 20/60, 66 + 40/60), ("Ardra", 66 + 40/60, 80),
    ("Punarvasu", 80, 93 + 20/60), ("Pushya", 93 + 20/60, 106 + 40/60),
    ("Ashlesha", 106 + 40/60, 120), ("Magha", 120, 133 + 20/60),
    ("Purva Phalguni", 133 + 20/60, 146 + 40/60), ("Uttara Phalguni", 146 + 40/60, 160),
    ("Hasta", 160, 173 + 20/60), ("Chitra", 173 + 20/60, 186 + 40/60),
    ("Swati", 186 + 40/60, 200), ("Vishakha", 200, 213 + 20/60),
    ("Anuradha", 213 + 20/60, 226 + 40/60), ("Jyeshtha", 226 + 40/60, 240),
    ("Mula", 240, 253 + 20/60), ("Purva Ashadha", 253 + 20/60, 266 + 40/60),
    ("Uttara Ashadha", 266 + 40/60, 280), ("Shravana", 280, 293 + 20/60),
    ("Dhanishta", 293 + 20/60, 306 + 40/60), ("Shatabhisha", 306 + 40/60, 320),
    ("Purva Bhadrapada", 320, 333 + 20/60), ("Uttara Bhadrapada", 333 + 20/60, 346 + 40/60),
    ("Revati", 346 + 40/60, 360)
]

# Vedic aspects (sign-based, no orbs)
VEDIC_ASPECTS = {
    "Sun": [7],  # Aspects 7th house
    "Moon": [7],
    "Mercury": [7],
    "Venus": [7],
    "Mars": [4, 7, 8],  # Special aspects: 4th, 8th
    "Jupiter": [5, 7, 9],  # Special aspects: 5th, 9th
    "Saturn": [3, 7, 10],  # Special aspects: 3rd, 10th
    "Rahu": [7],  # Optional: [5, 7, 9] in some traditions
    "Ketu": [7],  # Optional: [5, 7, 9]
}

# Interpretations (from previous artifact, adapted for Vedic)
PLANET_IN_SIGN_INTERPRETATIONS_VEDIC = {
    "Sun": {
        "Aries": (
            "Sun in Aries in the sidereal zodiac signifies a bold, ambitious, and leadership-oriented personality. You are driven to take initiative and excel in competitive environments, but should guard against impulsiveness."
        ),
        "Taurus": (
            "Sun in Taurus indicates a stable, determined, and material-focused identity. You seek security and comfort, with a strong appreciation for beauty, but may resist change or become overly attached to possessions."
        ),
        "Gemini": (
            "Sun in Gemini suggests a curious, intellectual, and communicative nature. You thrive in versatile environments and excel at multitasking, but may struggle with indecision or scattered energy."
        ),
        "Cancer": (
            "Sun in Cancer reflects a nurturing, emotional, and family-oriented identity. You are deeply connected to your roots and seek emotional security, but may be overly sensitive or protective."
        ),
        "Leo": (
            "Sun in Leo, its own sign, denotes a confident, charismatic, and authoritative personality. You shine in leadership roles and crave recognition, but should avoid arrogance or domineering tendencies."
        ),
        "Virgo": (
            "Sun in Virgo indicates a practical, analytical, and service-oriented nature. You excel in detail-oriented tasks and value efficiency, but may become overly critical or perfectionistic."
        ),
        "Libra": (
            "Sun in Libra, its debilitation sign, suggests a diplomatic, harmonious, and relationship-focused identity. You seek balance and fairness, but may struggle with indecision or over-dependence on others."
        ),
        "Scorpio": (
            "Sun in Scorpio signifies an intense, transformative, and secretive personality. You are driven by deep emotions and seek power, but should avoid obsession or vindictiveness."
        ),
        "Sagittarius": (
            "Sun in Sagittarius reflects an optimistic, adventurous, and philosophical nature. You are drawn to exploration and higher knowledge, but may be overly blunt or restless."
        ),
        "Capricorn": (
            "Sun in Capricorn indicates a disciplined, ambitious, and responsible identity. You are focused on long-term goals and social status, but may become overly serious or detached."
        ),
        "Aquarius": (
            "Sun in Aquarius suggests an innovative, humanitarian, and independent personality. You value freedom and social causes, but may seem aloof or overly detached."
        ),
        "Pisces": (
            "Sun in Pisces reflects a compassionate, intuitive, and spiritual nature. You are deeply empathetic and imaginative, but may struggle with escapism or lack of direction."
        ),
    },
    "Moon": {
        "Aries": (
            "Moon in Aries indicates a passionate, impulsive, and energetic emotional nature. You react quickly and seek excitement, but may struggle with impatience or emotional volatility."
        ),
        "Taurus": (
            "Moon in Taurus, its exaltation sign, suggests a stable, sensual, and comfort-seeking emotional nature. You value security and beauty, but may resist emotional change."
        ),
        "Gemini": (
            "Moon in Gemini reflects a curious, communicative, and adaptable emotional nature. You thrive on intellectual stimulation, but may experience restless or inconsistent emotions."
        ),
        "Cancer": (
            "Moon in Cancer in the sidereal zodiac indicates a deeply nurturing, emotional, and intuitive nature. "
            "You are strongly connected to home, family, and emotional security, with a protective and empathetic demeanor."
        ),
        "Leo": (
            "Moon in Leo signifies a warm, expressive, and dramatic emotional nature. You seek recognition and love to shine, but may be overly sensitive to criticism."
        ),
        "Virgo": (
            "Moon in Virgo suggests a practical, analytical, and service-oriented emotional nature. You seek order and efficiency, but may worry excessively or be overly critical."
        ),
        "Libra": (
            "Moon in Libra indicates a harmonious, diplomatic, and relationship-focused emotional nature. You seek balance and beauty, but may avoid confrontation or depend too much on others."
        ),
        "Scorpio": (
            "Moon in Scorpio, its debilitation sign, reflects an intense, secretive, and transformative emotional nature. You feel deeply and seek emotional depth, but may struggle with jealousy or obsession."
        ),
        "Sagittarius": (
            "Moon in Sagittarius suggests an optimistic, adventurous, and freedom-loving emotional nature. You seek truth and exploration, but may avoid emotional depth or commitment."
        ),
        "Capricorn": (
            "Moon in Capricorn indicates a reserved, disciplined, and duty-bound emotional nature. You value stability and responsibility, but may suppress emotions or feel isolated."
        ),
        "Aquarius": (
            "Moon in Aquarius reflects a detached, intellectual, and humanitarian emotional nature. You value independence and social ideals, but may seem emotionally distant."
        ),
        "Pisces": (
            "Moon in Pisces suggests a compassionate, intuitive, and dreamy emotional nature. You are highly empathetic and spiritual, but may struggle with boundaries or escapism."
        ),
    },
    "Mercury": {
        "Aries": (
            "Mercury in Aries indicates a quick, bold, and assertive communication style. You think and speak decisively, but may be impulsive or overlook details."
        ),
        "Taurus": (
            "Mercury in Taurus suggests a deliberate, practical, and grounded communication style. You value clarity and stability in thought, but may be stubborn or slow to adapt."
        ),
        "Gemini": (
            "Mercury in Gemini, its own sign, reflects a sharp, versatile, and communicative mind. You excel in learning and networking, but may be restless or superficial."
        ),
        "Cancer": (
            "Mercury in Cancer indicates an intuitive, emotional, and nurturing communication style. You think with your heart, but may be overly sensitive or subjective."
        ),
        "Leo": (
            "Mercury in Leo suggests a confident, dramatic, and creative communication style. You express ideas with flair, but may be overly opinionated or seek attention."
        ),
        "Virgo": (
            "Mercury in Virgo, its own and exaltation sign, signifies a precise, analytical, and detail-oriented mind. You excel in problem-solving, but may be overly critical."
        ),
        "Libra": (
            "Mercury in Libra reflects a diplomatic, balanced, and aesthetically inclined communication style. You seek fairness in ideas, but may struggle with indecision."
        ),
        "Scorpio": (
            "Mercury in Scorpio indicates a penetrating, secretive, and investigative communication style. You seek truth and depth, but may be overly suspicious or sharp-tongued."
        ),
        "Sagittarius": (
            "Mercury in Sagittarius suggests an optimistic, philosophical, and broad-minded communication style. You love big ideas, but may overlook details or be blunt."
        ),
        "Capricorn": (
            "Mercury in Capricorn reflects a disciplined, practical, and goal-oriented communication style. You think strategically, but may be overly serious or rigid."
        ),
        "Aquarius": (
            "Mercury in Aquarius indicates an innovative, intellectual, and unconventional communication style. You value originality, but may seem detached or eccentric."
        ),
        "Pisces": (
            "Mercury in Pisces, its debilitation sign, suggests an intuitive, imaginative, and poetic communication style. You think creatively, but may struggle with clarity or focus."
        ),
    },
    "Venus": {
        "Aries": (
            "Venus in Aries indicates a passionate, impulsive, and bold approach to love and beauty. You pursue relationships with enthusiasm, but may be impatient or self-focused."
        ),
        "Taurus": (
            "Venus in Taurus, its own sign, suggests a sensual, loyal, and comfort-seeking approach to love. You value stability and beauty, but may be possessive or resistant to change."
        ),
        "Gemini": (
            "Venus in Gemini reflects a playful, communicative, and versatile approach to love. You seek intellectual connection, but may be inconsistent or detached."
        ),
        "Cancer": (
            "Venus in Cancer indicates a nurturing, emotional, and family-oriented approach to love. You seek emotional security, but may be overly sensitive or clingy."
        ),
        "Leo": (
            "Venus in Leo suggests a warm, dramatic, and generous approach to love. You seek admiration and romance, but may be overly demanding or prideful."
        ),
        "Virgo": (
            "Venus in Virgo, its debilitation sign, reflects a practical, service-oriented, and reserved approach to love. You value loyalty, but may be overly critical or shy."
        ),
        "Libra": (
            "Venus in Libra, its own sign, indicates a harmonious, diplomatic, and aesthetically inclined approach to love. You seek balance and beauty, but may avoid conflict."
        ),
        "Scorpio": (
            "Venus in Scorpio suggests an intense, passionate, and transformative approach to love. You seek deep connections, but may struggle with jealousy or obsession."
        ),
        "Sagittarius": (
            "Venus in Sagittarius reflects an adventurous, optimistic, and freedom-loving approach to love. You seek growth and exploration, but may avoid commitment."
        ),
        "Capricorn": (
            "Venus in Capricorn indicates a serious, loyal, and status-conscious approach to love. You value long-term commitment, but may be emotionally reserved."
        ),
        "Aquarius": (
            "Venus in Aquarius suggests an unconventional, intellectual, and independent approach to love. You value freedom and friendship, but may seem detached."
        ),
        "Pisces": (
            "Venus in Pisces, its exaltation sign, reflects a compassionate, romantic, and spiritual approach to love. You are deeply empathetic, but may idealize partners."
        ),
    },
    "Mars": {
        "Aries": (
            "Mars in Aries, its own sign, indicates a bold, assertive, and energetic nature. You are a natural leader and thrive in action, but may be impulsive or aggressive."
        ),
        "Taurus": (
            "Mars in Taurus suggests a determined, sensual, and persistent drive. You pursue goals steadily, but may be stubborn or overly focused on material gains."
        ),
        "Gemini": (
            "Mars in Gemini reflects a versatile, intellectual, and communicative drive. You channel energy into ideas and multitasking, but may lack focus."
        ),
        "Cancer": (
            "Mars in Cancer, its debilitation sign, indicates an emotional, protective, and nurturing drive. You act with heart, but may be moody or indirect."
        ),
        "Leo": (
            "Mars in Leo suggests a confident, dramatic, and ambitious drive. You pursue goals with passion and flair, but may be domineering or seek attention."
        ),
        "Virgo": (
            "Mars in Virgo reflects a precise, analytical, and efficient drive. You excel in detailed tasks, but may be overly critical or perfectionistic."
        ),
        "Libra": (
            "Mars in Libra indicates a diplomatic, relationship-focused, and balanced drive. You seek harmony in action, but may avoid confrontation or indecision."
        ),
        "Scorpio": (
            "Mars in Scorpio, its own sign, suggests an intense, transformative, and strategic drive. You pursue goals with depth, but may be secretive or vengeful."
        ),
        "Sagittarius": (
            "Mars in Sagittarius reflects an adventurous, optimistic, and freedom-loving drive. You seek exploration and truth, but may be reckless or blunt."
        ),
        "Capricorn": (
            "Mars in Capricorn, its exaltation sign, indicates a disciplined, ambitious, and strategic drive. You pursue long-term goals, but may be overly serious."
        ),
        "Aquarius": (
            "Mars in Aquarius suggests an innovative, humanitarian, and independent drive. You channel energy into social causes, but may be erratic or detached."
        ),
        "Pisces": (
            "Mars in Pisces reflects a compassionate, intuitive, and spiritual drive. You act with empathy, but may lack assertiveness or clarity."
        ),
    },
    "Jupiter": {
        "Aries": (
            "Jupiter in Aries indicates an optimistic, bold, and pioneering approach to wisdom and growth. You inspire others with enthusiasm, but may be overly impulsive."
        ),
        "Taurus": (
            "Jupiter in Taurus suggests a practical, generous, and material-focused approach to growth. You seek abundance and stability, but may indulge excessively."
        ),
        "Gemini": (
            "Jupiter in Gemini reflects a curious, communicative, and versatile approach to wisdom. You excel in learning, but may be scattered or superficial."
        ),
        "Cancer": (
            "Jupiter in Cancer, its exaltation sign, indicates a nurturing, protective, and spiritual approach to growth. You inspire through empathy, but may be overly emotional."
        ),
        "Leo": (
            "Jupiter in Leo suggests a confident, generous, and charismatic approach to wisdom. You lead with inspiration, but may be prideful or extravagant."
        ),
        "Virgo": (
            "Jupiter in Virgo reflects a practical, analytical, and service-oriented approach to growth. You seek improvement, but may be overly critical."
        ),
        "Libra": (
            "Jupiter in Libra indicates a harmonious, diplomatic, and justice-oriented approach to wisdom. You promote balance, but may avoid hard truths."
        ),
        "Scorpio": (
            "Jupiter in Scorpio suggests a deep, transformative, and investigative approach to growth. You seek truth and power, but may be secretive or intense."
        ),
        "Sagittarius": (
            "Jupiter in Sagittarius, its own sign, reflects an optimistic, philosophical, and adventurous approach to wisdom. You inspire through exploration, but may be dogmatic."
        ),
        "Capricorn": (
            "Jupiter in Capricorn, its debilitation sign, indicates a disciplined, practical, and ambitious approach to growth. You seek success, but may be overly cautious."
        ),
        "Aquarius": (
            "Jupiter in Aquarius suggests an innovative, humanitarian, and intellectual approach to wisdom. You promote progress, but may be detached."
        ),
        "Pisces": (
            "Jupiter in Pisces, its own sign, reflects a compassionate, spiritual, and intuitive approach to growth. You inspire through empathy, but may lack boundaries."
        ),
    },
    "Saturn": {
        "Aries": (
            "Saturn in Aries, its debilitation sign, indicates a disciplined yet challenged approach to action. You work hard to overcome obstacles, but may struggle with impulsiveness."
        ),
        "Taurus": (
            "Saturn in Taurus suggests a patient, practical, and material-focused approach to responsibility. You build stability, but may be overly cautious or attached."
        ),
        "Gemini": (
            "Saturn in Gemini reflects a disciplined, intellectual, and communicative approach to duty. You excel in structured learning, but may be rigid in thought."
        ),
        "Cancer": (
            "Saturn in Cancer indicates a reserved, protective, and duty-bound approach to emotions. You seek emotional stability, but may feel isolated or burdened."
        ),
        "Leo": (
            "Saturn in Leo suggests a disciplined, authoritative, and responsible approach to leadership. You work hard for recognition, but may struggle with pride."
        ),
        "Virgo": (
            "Saturn in Virgo reflects a meticulous, service-oriented, and practical approach to duty. You excel in organization, but may be overly perfectionistic."
        ),
        "Libra": (
            "Saturn in Libra, its exaltation sign, indicates a balanced, diplomatic, and justice-oriented approach to responsibility. You promote fairness, but may avoid conflict."
        ),
        "Scorpio": (
            "Saturn in Scorpio suggests a deep, transformative, and disciplined approach to challenges. You face hardships with resilience, but may be secretive or intense."
        ),
        "Sagittarius": (
            "Saturn in Sagittarius reflects a disciplined, philosophical, and ethical approach to duty. You seek truth, but may be rigid or dogmatic."
        ),
        "Capricorn": (
            "Saturn in Capricorn, its own sign, indicates a responsible, ambitious, and strategic approach to duty. You excel in long-term planning, but may be overly serious."
        ),
        "Aquarius": (
            "Saturn in Aquarius, its own sign, suggests a disciplined, humanitarian, and innovative approach to responsibility. You promote progress, but may be detached."
        ),
        "Pisces": (
            "Saturn in Pisces reflects a compassionate, spiritual, and disciplined approach to challenges. You face hardships with empathy, but may struggle with boundaries."
        ),
    },
    "Rahu": {
        "Aries": (
            "Rahu in Aries suggests an ambitious, pioneering, and intense drive for individuality. You seek recognition and action, but may be impulsive or overly aggressive."
        ),
        "Taurus": (
            "Rahu in Taurus indicates a strong desire for material wealth and sensual pleasures. You pursue comfort and beauty, but may become obsessed with possessions."
        ),
        "Gemini": (
            "Rahu in Gemini reflects an intense curiosity and communicative drive. You seek knowledge and connections, but may be scattered or manipulative."
        ),
        "Cancer": (
            "Rahu in Cancer suggests a deep craving for emotional security and family ties. You pursue nurturing environments, but may be overly clingy or manipulative."
        ),
        "Leo": (
            "Rahu in Leo indicates a powerful desire for recognition and leadership. You seek fame and creativity, but may be arrogant or overly dramatic."
        ),
        "Virgo": (
            "Rahu in Virgo reflects an intense focus on perfection and service. You pursue efficiency and detail, but may become obsessive or overly critical."
        ),
        "Libra": (
            "Rahu in Libra suggests a strong desire for relationships and harmony. You pursue partnerships and beauty, but may be overly dependent or manipulative."
        ),
        "Scorpio": (
            "Rahu in Scorpio suggests an intense, transformative drive toward your karmic goals. You may be drawn to "
            "power, mystery, and hidden knowledge, with a strong desire to explore the depths of life. This placement "
            "encourages breaking taboos but warns against obsession or manipulation."
        ),
        "Sagittarius": (
            "Rahu in Sagittarius indicates a passionate pursuit of knowledge and adventure. You seek truth and exploration, but may be dogmatic or reckless."
        ),
        "Capricorn": (
            "Rahu in Capricorn suggests an ambitious drive for status and achievement. You pursue long-term goals, but may be overly materialistic or ruthless."
        ),
        "Aquarius": (
            "Rahu in Aquarius reflects a desire for innovation and social change. You pursue humanitarian ideals, but may be erratic or detached."
        ),
        "Pisces": (
            "Rahu in Pisces indicates a spiritual and imaginative drive. You seek transcendence and compassion, but may be prone to escapism or delusion."
        ),
    },
    "Ketu": {
        "Aries": (
            "Ketu in Aries suggests a detachment from personal ambition and assertiveness. You seek spiritual growth over ego, but may feel directionless."
        ),
        "Taurus": (
            "Ketu in Taurus indicates a detachment from material comforts and a spiritual inclination. You may feel "
            "disconnected from wealth or sensuality, seeking deeper meaning beyond physical pleasures."
        ),
        "Gemini": (
            "Ketu in Gemini reflects a detachment from intellectual pursuits and communication. You seek inner wisdom, but may feel scattered or uninspired."
        ),
        "Cancer": (
            "Ketu in Cancer suggests a detachment from emotional attachments and family. You seek spiritual security, but may feel isolated or emotionally distant."
        ),
        "Leo": (
            "Ketu in Leo indicates a detachment from fame and leadership. You seek humility and inner light, but may struggle with self-expression."
        ),
        "Virgo": (
            "Ketu in Virgo reflects a detachment from perfectionism and service. You seek spiritual clarity, but may feel unmotivated in routine tasks."
        ),
        "Libra": (
            "Ketu in Libra suggests a detachment from relationships and harmony. You seek inner balance, but may feel disconnected from partnerships."
        ),
        "Scorpio": (
            "Ketu in Scorpio indicates a detachment from intensity and transformation. You seek spiritual liberation, but may feel lost in emotional depths."
        ),
        "Sagittarius": (
            "Ketu in Sagittarius reflects a detachment from philosophy and adventure. You seek inner truth, but may feel restless or uninspired."
        ),
        "Capricorn": (
            "Ketu in Capricorn suggests a detachment from ambition and status. You seek spiritual purpose, but may feel unmotivated in worldly pursuits."
        ),
        "Aquarius": (
            "Ketu in Aquarius indicates a detachment from social ideals and innovation. You seek inner freedom, but may feel isolated or eccentric."
        ),
        "Pisces": (
            "Ketu in Pisces reflects a spiritual, intuitive, and detached nature. You seek liberation and transcendence, but may struggle with grounding."
        ),
    }
}

PLANET_IN_HOUSE_INTERPRETATIONS_VEDIC = {
    "Sun": {
        1: (
            "Sun in the 1st house signifies a strong, confident, and authoritative personality. You shine as a natural leader, but may struggle with ego or arrogance."
        ),
        2: (
            "Sun in the 2nd house indicates a focus on wealth, speech, and family pride. You excel in financial leadership, but should avoid being overly materialistic."
        ),
        3: (
            "Sun in the 3rd house suggests boldness, communication skills, and initiative. You thrive in creative expression, but may be overly dominant in interactions."
        ),
        4: (
            "Sun in the 4th house reflects a strong connection to home, mother, and inner happiness. You seek domestic authority, but may face challenges with emotional balance."
        ),
        5: (
            "Sun in the 5th house signifies creativity, intelligence, and leadership in education or children. You shine in speculative ventures, but may be prideful."
        ),
        6: (
            "Sun in the 6th house indicates success in overcoming enemies and health challenges. You excel in service and discipline, but may face conflicts with authority."
        ),
        7: (
            "Sun in the 7th house suggests a charismatic, influential presence in partnerships. You seek powerful relationships, but may dominate or face ego clashes."
        ),
        8: (
            "Sun in the 8th house reflects a focus on transformation, secrets, and longevity. You are drawn to deep mysteries, but may face sudden challenges or power struggles."
        ),
        9: (
            "Sun in the 9th house signifies a strong connection to dharma, higher learning, and spirituality. You shine as a teacher or guide, but may be dogmatic."
        ),
        10: (
            "Sun in the 10th house indicates a powerful, authoritative career and public recognition. You excel in leadership roles, but should avoid being overly ambitious."
        ),
        11: (
            "Sun in the 11th house suggests success in social networks, gains, and aspirations. You shine in group endeavors, but may prioritize status over relationships."
        ),
        12: (
            "Sun in the 12th house reflects a spiritual, introspective nature with interest in liberation. You may excel in foreign lands, but could feel isolated or lack recognition."
        ),
    },
    "Moon": {
        1: (
            "Moon in the 1st house indicates a nurturing, emotional, and intuitive personality. You are deeply sensitive and charismatic, but may be overly moody."
        ),
        2: (
            "Moon in the 2nd house suggests emotional attachment to wealth, family, and speech. You seek financial security, but may face fluctuating resources."
        ),
        3: (
            "Moon in the 3rd house reflects a communicative, curious, and emotionally expressive nature. You excel in creative writing, but may be restless."
        ),
        4: (
            "Moon in the 4th house signifies a deep connection to home, mother, and emotional comfort. You thrive in nurturing environments, but may be overly attached."
        ),
        5: (
            "Moon in the 5th house indicates emotional creativity, love for children, and romantic sensitivity. You shine in artistic pursuits, but may be overly dramatic."
        ),
        6: (
            "Moon in the 6th house suggests emotional investment in service, health, and overcoming challenges. You excel in caregiving, but may worry excessively."
        ),
        7: (
            "Moon in the 7th house reflects a nurturing, emotionally driven approach to partnerships. You seek harmonious relationships, but may be overly dependent."
        ),
        8: (
            "Moon in the 8th house indicates emotional depth, interest in mysteries, and transformation. You are intuitive, but may face emotional upheavals."
        ),
        9: (
            "Moon in the 9th house suggests an emotional connection to spirituality, travel, and higher learning. You seek wisdom, but may be swayed by emotions."
        ),
        10: (
            "Moon in the 10th house signifies a public, nurturing, and emotionally driven career. You shine in caregiving roles, but may face public scrutiny."
        ),
        11: (
            "Moon in the 11th house reflects emotional fulfillment through social networks and aspirations. You thrive in group settings, but may seek validation."
        ),
        12: (
            "Moon in the 12th house indicates a spiritual, intuitive, and private emotional nature. You seek solitude, but may struggle with emotional isolation."
        ),
    },
    "Mercury": {
        1: (
            "Mercury in the 1st house signifies a sharp, communicative, and intellectual personality. You excel in self-expression, but may be restless or talkative."
        ),
        2: (
            "Mercury in the 2nd house suggests a talent for financial communication and intellectual wealth. You shine in business, but may overanalyze finances."
        ),
        3: (
            "Mercury in the 3rd house indicates a strong, versatile, and communicative mind. You excel in writing and learning, but may be overly curious."
        ),
        4: (
            "Mercury in the 4th house reflects an intellectual connection to home and education. You thrive in domestic learning, but may be emotionally scattered."
        ),
        5: (
            "Mercury in the 5th house signifies creativity, intelligence, and playful communication. You shine in teaching or arts, but may lack focus."
        ),
        6: (
            "Mercury in the 6th house suggests analytical skills in service, health, and conflict resolution. You excel in problem-solving, but may worry excessively."
        ),
        7: (
            "Mercury in the 7th house indicates a communicative, intellectual approach to partnerships. You seek mental connection, but may overthink relationships."
        ),
        8: (
            "Mercury in the 8th house reflects a probing, investigative mind drawn to secrets. You excel in research, but may be secretive or suspicious."
        ),
        9: (
            "Mercury in the 9th house signifies a curious, philosophical, and communicative approach to wisdom. You shine in teaching, but may be scattered."
        ),
        10: (
            "Mercury in the 10th house suggests a career in communication, intellect, or commerce. You excel in public roles, but may change paths frequently."
        ),
        11: (
            "Mercury in the 11th house indicates success in intellectual networks and group endeavors. You shine in social communication, but may be superficial."
        ),
        12: (
            "Mercury in the 12th house reflects a private, intuitive, and imaginative mind. You excel in spiritual pursuits, but may struggle with clarity."
        ),
    },
    "Venus": {
        1: (
            "Venus in the 1st house signifies a charming, attractive, and harmonious personality. You draw others with grace, but may be overly focused on appearance."
        ),
        2: (
            "Venus in the 2nd house suggests a love for wealth, beauty, and luxurious possessions. You excel in financial arts, but may be indulgent."
        ),
        3: (
            "Venus in the 3rd house reflects a charming, artistic, and communicative nature. You shine in creative expression, but may seek constant admiration."
        ),
        4: (
            "Venus in the 4th house indicates a love for home, comfort, and aesthetic environments. You create a beautiful domestic life, but may be overly attached."
        ),
        5: (
            "Venus in the 5th house signifies a romantic, creative, and pleasure-seeking nature. You shine in arts and romance, but may be overly indulgent."
        ),
        6: (
            "Venus in the 6th house suggests a harmonious approach to service, health, and work. You excel in caregiving, but may face relationship conflicts."
        ),
        7: (
            "Venus in the 7th house indicates a strong focus on harmonious, loving partnerships. You thrive in relationships, but may depend too much on partners."
        ),
        8: (
            "Venus in the 8th house reflects a passionate, transformative approach to love and shared resources. You seek deep connections, but may face jealousy."
        ),
        9: (
            "Venus in the 9th house suggests a love for travel, philosophy, and cultural beauty. You shine in spiritual pursuits, but may idealize beliefs."
        ),
        10: (
            "Venus in the 10th house indicates a career in arts, beauty, or diplomacy. You shine publicly, but may prioritize status over passion."
        ),
        11: (
            "Venus in the 11th house reflects success in social networks and artistic aspirations. You attract influential friends, but may seek validation."
        ),
        12: (
            "Venus in the 12th house signifies a private, spiritual, and romantic nature. You seek transcendent love, but may face secret affairs or isolation."
        ),
    },
    "Mars": {
        1: (
            "Mars in the 1st house signifies a bold, energetic, and assertive personality. You are a natural leader, but may be aggressive or impulsive."
        ),
        2: (
            "Mars in the 2nd house suggests a driven, competitive approach to wealth and speech. You pursue financial goals aggressively, but may be reckless."
        ),
        3: (
            "Mars in the 3rd house reflects courage, initiative, and dynamic communication. You excel in bold expression, but may be argumentative."
        ),
        4: (
            "Mars in the 4th house indicates a protective, energetic approach to home and family. You defend your roots, but may face domestic conflicts."
        ),
        5: (
            "Mars in the 5th house signifies a passionate, creative, and competitive nature. You shine in sports or arts, but may be overly dominant."
        ),
        6: (
            "Mars in the 6th house suggests strength in overcoming enemies, health issues, and work challenges. You excel in discipline, but may be combative."
        ),
        7: (
            "Mars in the 7th house indicates a passionate, assertive approach to partnerships. You seek dynamic relationships, but may face conflicts."
        ),
        8: (
            "Mars in the 8th house reflects a transformative, intense approach to secrets and shared resources. You face challenges with courage, but may be secretive."
        ),
        9: (
            "Mars in the 9th house suggests a bold, adventurous approach to spirituality and learning. You pursue truth aggressively, but may be dogmatic."
        ),
        10: (
            "Mars in the 10th house indicates a dynamic, ambitious career in leadership or action-oriented fields. You shine publicly, but may be overly competitive."
        ),
        11: (
            "Mars in the 11th house reflects a driven, competitive approach to social networks and gains. You achieve through groups, but may clash with friends."
        ),
        12: (
            "Mars in the 12th house suggests a hidden, spiritual drive or repressed energy. You excel in private pursuits, but may face subconscious conflicts."
        ),
    },
    "Jupiter": {
        1: (
            "Jupiter in the 1st house signifies a wise, optimistic, and charismatic personality. You inspire others, but may be overly confident."
        ),
        2: (
            "Jupiter in the 2nd house suggests abundance, generosity, and wisdom in wealth and speech. You attract prosperity, but may be extravagant."
        ),
        3: (
            "Jupiter in the 3rd house reflects a communicative, philosophical, and curious nature. You excel in teaching, but may be overly verbose."
        ),
        4: (
            "Jupiter in the 4th house indicates a blessed, nurturing home life and spiritual connection. You create comfort, but may be overly protective."
        ),
        5: (
            "Jupiter in the 5th house signifies wisdom, creativity, and blessings in children or education. You shine in teaching, but may be indulgent."
        ),
        6: (
            "Jupiter in the 6th house suggests success in service, health, and overcoming challenges. You excel in caregiving, but may overextend."
        ),
        7: (
            "Jupiter in the 7th house indicates a wise, harmonious approach to partnerships. You attract beneficial relationships, but may idealize partners."
        ),
        8: (
            "Jupiter in the 8th house reflects a spiritual, transformative approach to secrets and longevity. You gain through shared resources, but may face hidden challenges."
        ),
        9: (
            "Jupiter in the 9th house signifies a strong connection to dharma, spirituality, and higher learning. You shine as a guru, but may be dogmatic."
        ),
        10: (
            "Jupiter in the 10th house indicates a blessed, authoritative career in teaching or leadership. You gain public respect, but may be overly ambitious."
        ),
        11: (
            "Jupiter in the 11th house suggests success in social networks, gains, and spiritual aspirations. You attract prosperity, but may over-rely on groups."
        ),
        12: (
            "Jupiter in the 12th house reflects a spiritual, compassionate nature with a focus on liberation. You excel in solitude, but may face financial losses."
        ),
    },
    "Saturn": {
        1: (
            "Saturn in the 1st house signifies a disciplined, serious, and responsible personality. You work hard to define yourself, but may feel restricted."
        ),
        2: (
            "Saturn in the 2nd house suggests a cautious, disciplined approach to wealth and speech. You build stability slowly, but may face financial delays."
        ),
        3: (
            "Saturn in the 3rd house reflects a disciplined, focused approach to communication and effort. You excel in perseverance, but may be overly serious."
        ),
        4: (
            "Saturn in the 4th house indicates a responsible, duty-bound approach to home and mother. You seek stability, but may face domestic challenges."
        ),
        5: (
            "Saturn in the 5th house suggests a serious, disciplined approach to creativity and children. You work hard for joy, but may feel restricted in fun."
        ),
        6: (
            "Saturn in the 6th house signifies success in overcoming enemies, health issues, and work challenges. You excel in discipline, but may overwork."
        ),
        7: (
            "Saturn in the 7th house indicates a serious, committed approach to partnerships. You seek lasting relationships, but may face delays or burdens."
        ),
        8: (
            "Saturn in the 8th house reflects a disciplined, resilient approach to transformation and longevity. You face challenges with patience, but may fear change."
        ),
        9: (
            "Saturn in the 9th house suggests a serious, ethical approach to spirituality and learning. You seek truth through effort, but may be rigid."
        ),
        10: (
            "Saturn in the 10th house indicates a disciplined, ambitious career with lasting success. You shine in leadership, but may face delays or burdens."
        ),
        11: (
            "Saturn in the 11th house reflects a patient, disciplined approach to social networks and gains. You achieve slowly, but may feel isolated."
        ),
        12: (
            "Saturn in the 12th house signifies a spiritual, disciplined approach to liberation and solitude. You excel in introspection, but may face losses."
        ),
    },
    "Rahu": {
        1: (
            "Rahu in the 1st house suggests an intense, ambitious drive to define your identity. You appear magnetic, but may be restless or self-focused."
        ),
        2: (
            "Rahu in the 2nd house indicates a strong desire for wealth, speech, and material gains. You pursue luxury, but may face financial instability."
        ),
        3: (
            "Rahu in the 3rd house reflects an ambitious, communicative, and curious nature. You seek influence through expression, but may be manipulative."
        ),
        4: (
            "Rahu in the 4th house suggests a craving for emotional security and home comforts. You pursue domestic success, but may face unrest."
        ),
        5: (
            "Rahu in the 5th house indicates an intense drive for creativity, romance, and recognition. You seek fame, but may take risky ventures."
        ),
        6: (
            "Rahu in the 6th house suggests success in overcoming enemies and health challenges through ambition. You excel in service, but may create conflicts."
        ),
        7: (
            "Rahu in the 7th house reflects an intense desire for partnerships and influence. You attract dynamic relationships, but may face deception."
        ),
        8: (
            "Rahu in the 8th house indicates a fascination with secrets, transformation, and shared resources. You seek power, but may face sudden upheavals."
        ),
        9: (
            "Rahu in the 9th house suggests an ambitious pursuit of spirituality, travel, and higher learning. You seek wisdom, but may be dogmatic."
        ),
        10: (
            "Rahu in the 10th house reflects a powerful drive for career success and public recognition. You shine in ambitious roles, but may take shortcuts."
        ),
        11: (
            "Rahu in the 11th house indicates a powerful desire for social connections, wealth, and group achievements. "
            "You may pursue ambitious goals through networks but should avoid overattachment to material gains."
        ),
        12: (
            "Rahu in the 12th house suggests an intense drive for spirituality, foreign lands, or liberation. You seek transcendence, but may face confusion."
        ),
    },
    "Ketu": {
        1: (
            "Ketu in the 1st house indicates a spiritual, detached approach to identity. You seek inner truth, but may feel disconnected or directionless."
        ),
        2: (
            "Ketu in the 2nd house suggests detachment from wealth, speech, and material possessions. You seek spiritual values, but may face financial uncertainty."
        ),
        3: (
            "Ketu in the 3rd house reflects a detached, intuitive approach to communication and effort. You seek inner wisdom, but may lack motivation."
        ),
        4: (
            "Ketu in the 4th house indicates detachment from home, mother, and emotional security. You seek spiritual comfort, but may feel rootless."
        ),
        5: (
            "Ketu in the 5th house suggests detachment from creative expression or children, with a spiritual focus on inner wisdom. "
            "You may feel disconnected from romance or speculative ventures."
        ),
        6: (
            "Ketu in the 6th house reflects a spiritual approach to service, health, and challenges. You overcome obstacles intuitively, but may avoid conflict."
        ),
        7: (
            "Ketu in the 7th house suggests detachment from partnerships and worldly relationships. You seek spiritual bonds, but may feel isolated."
        ),
        8: (
            "Ketu in the 8th house indicates a spiritual, detached approach to transformation and secrets. You seek liberation, but may avoid emotional depth."
        ),
        9: (
            "Ketu in the 9th house reflects a detached, intuitive approach to spirituality and learning. You seek inner truth, but may lack direction."
        ),
        10: (
            "Ketu in the 10th house suggests detachment from career and public recognition. You seek spiritual purpose, but may feel unmotivated professionally."
        ),
        11: (
            "Ketu in the 11th house indicates detachment from social networks and material gains. You seek spiritual aspirations, but may feel isolated."
        ),
        12: (
            "Ketu in the 12th house reflects a spiritual, intuitive nature focused on liberation and solitude. You excel in moksha, but may face subconscious fears."
        ),
    }
}

NAKSHATRA_INTERPRETATIONS = {
    "Ashwini": (
        "Moon in Ashwini Nakshatra indicates a dynamic, healing, and pioneering emotional nature. You are quick to act and inspire others, but may struggle with impulsiveness."
    ),
    "Bharani": (
        "Moon in Bharani Nakshatra suggests a passionate, disciplined, and transformative emotional nature. You seek growth through challenges, but should avoid being overly intense."
    ),
    "Krittika": (
        "Moon in Krittika Nakshatra reflects a sharp, ambitious, and purifying emotional nature. You strive for excellence, but may be overly critical or fiery."
    ),
    "Rohini": (
        "Moon in Rohini Nakshatra indicates a sensual, nurturing, and creative emotional nature. You attract abundance and beauty, but may become attached to comforts."
    ),
    "Mrigashira": (
        "Moon in Mrigashira Nakshatra suggests a curious, restless, and seeking emotional nature. You pursue knowledge and connections, but may lack emotional stability."
    ),
    "Ardra": (
        "Moon in Ardra Nakshatra reflects a stormy, transformative, and intellectual emotional nature. You embrace change, but may struggle with emotional turbulence."
    ),
    "Punarvasu": (
        "Moon in Punarvasu Nakshatra indicates a nurturing, adaptable, and optimistic emotional nature. You foster renewal and growth, but may avoid emotional depth."
    ),
    "Pushya": (
        "Moon in Pushya Nakshatra suggests a deeply nourishing, spiritual, and protective emotional nature. You provide care and wisdom, but may feel burdened by responsibilities."
    ),
    "Ashlesha": (
        "Moon in Ashlesha Nakshatra indicates a sharp, intuitive, and transformative emotional nature. You may be deeply perceptive "
        "but should guard against manipulation or emotional intensity."
    ),
    "Magha": (
        "Moon in Magha Nakshatra reflects a regal, authoritative, and ancestral emotional nature. You seek respect and legacy, but may struggle with pride."
    ),
    "Purva Phalguni": (
        "Moon in Purva Phalguni Nakshatra suggests a romantic, creative, and pleasure-seeking emotional nature. You shine in love and arts, but may be overly indulgent."
    ),
    "Uttara Phalguni": (
        "Moon in Uttara Phalguni Nakshatra indicates a generous, disciplined, and relationship-focused emotional nature. You foster harmony, but may prioritize duty over emotions."
    ),
    "Hasta": (
        "Moon in Hasta Nakshatra reflects a skillful, precise, and resourceful emotional nature. You excel in craftsmanship, but may be overly critical or anxious."
    ),
    "Chitra": (
        "Moon in Chitra Nakshatra suggests a creative, charismatic, and ambitious emotional nature. You shine in artistic or architectural pursuits, but may seek constant admiration."
    ),
    "Swati": (
        "Moon in Swati Nakshatra indicates an independent, diplomatic, and adaptable emotional nature. You thrive in freedom, but may struggle with indecision."
    ),
    "Vishakha": (
        "Moon in Vishakha Nakshatra reflects a determined, ambitious, and goal-oriented emotional nature. You pursue success with passion, but may be overly competitive."
    ),
    "Anuradha": (
        "Moon in Anuradha Nakshatra suggests a loyal, compassionate, and socially connected emotional nature. You foster friendships, but may feel emotionally burdened."
    ),
    "Jyeshtha": (
        "Moon in Jyeshtha Nakshatra indicates a protective, authoritative, and intense emotional nature. You lead with strength, but may struggle with jealousy or control."
    ),
    "Mula": (
        "Moon in Mula Nakshatra reflects a deep, transformative, and truth-seeking emotional nature. You uncover hidden truths, but may face emotional upheaval."
    ),
    "Purva Ashadha": (
        "Moon in Purva Ashadha Nakshatra suggests an optimistic, ambitious, and socially driven emotional nature. You pursue goals with vigor, but may be overly idealistic."
    ),
    "Uttara Ashadha": (
        "Moon in Uttara Ashadha Nakshatra indicates a disciplined, responsible, and success-oriented emotional nature. You achieve through perseverance, but may suppress emotions."
    ),
    "Shravana": (
        "Moon in Shravana Nakshatra reflects a perceptive, communicative, and learning-oriented emotional nature. You seek wisdom through listening, but may be overly sensitive."
    ),
    "Dhanishta": (
        "Moon in Dhanishta Nakshatra suggests a dynamic, ambitious, and socially influential emotional nature. You excel in leadership, but may prioritize status over emotions."
    ),
    "Shatabhisha": (
        "Moon in Shatabhisha Nakshatra indicates a mystical, independent, and healing emotional nature. You seek truth and solitude, but may feel emotionally detached."
    ),
    "Purva Bhadrapada": (
        "Moon in Purva Bhadrapada Nakshatra reflects a spiritual, intense, and transformative emotional nature. You pursue higher ideals, but may struggle with inner conflict."
    ),
    "Uttara Bhadrapada": (
        "Moon in Uttara Bhadrapada Nakshatra suggests a compassionate, wise, and introspective emotional nature. You foster peace, but may carry hidden emotional burdens."
    ),
    "Revati": (
        "Moon in Revati Nakshatra indicates a nurturing, spiritual, and empathetic emotional nature. You guide others with compassion, but may struggle with boundaries."
    ),
}

VEDIC_ASPECT_INTERPRETATIONS = {
    "Sun": {
        ("Moon", 7): (
            "Sun aspecting Moon by 7th house aspect illuminates your emotions with confidence and authority. You may seek emotional recognition, but could struggle with emotional sensitivity."
        ),
        ("Mercury", 7): (
            "Sun aspecting Mercury by 7th house aspect enhances your intellect with clarity and leadership. You communicate with authority, but may be overly opinionated."
        ),
        ("Venus", 7): (
            "Sun aspecting Venus by 7th house aspect infuses your relationships with warmth and pride. You seek harmonious partnerships, but may dominate or demand admiration."
        ),
        ("Mars", 7): (
            "Sun aspecting Mars by 7th house aspect fuels your drive with ambition and authority. You pursue goals boldly, but may face conflicts or ego clashes."
        ),
        ("Jupiter", 7): (
            "Sun aspecting Jupiter by 7th house aspect blends wisdom with confidence, promoting spiritual growth. You inspire others, but may be overly dogmatic."
        ),
        ("Saturn", 7): (
            "Sun aspecting Saturn by 7th house aspect creates tension between authority and discipline. You work hard for respect, but may feel restricted or burdened."
        ),
        ("Rahu", 7): (
            "Sun aspecting Rahu by 7th house aspect intensifies your ambition for recognition. You chase fame boldly, but may face illusions or ego-driven challenges."
        ),
        ("Ketu", 7): (
            "Sun aspecting Ketu by 7th house aspect encourages detachment from ego and worldly recognition. You seek spiritual clarity, but may feel disconnected from authority."
        ),
        ("Ascendant", 7): (
            "Sun aspecting Ascendant by 7th house aspect enhances your personality with confidence and charisma. You shine in partnerships, but may overshadow others."
        ),
        ("Midheaven", 7): (
            "Sun aspecting Midheaven by 7th house aspect boosts your career with authority and visibility. You excel in leadership, but may prioritize status over balance."
        ),
    },
    "Moon": {
        ("Sun", 7): (
            "Moon aspecting Sun by 7th house aspect balances your emotions with confidence and authority. You seek emotional harmony, but may struggle with ego sensitivity."
        ),
        ("Mercury", 7): (
            "Moon aspecting Mercury by 7th house aspect enhances your intellect with emotional intuition. You communicate sensitively, but may be overly subjective."
        ),
        ("Venus", 7): (
            "Moon aspecting Venus by 7th house aspect fosters nurturing and harmonious relationships. You seek emotional connection, but may be overly dependent."
        ),
        ("Mars", 7): (
            "Moon aspecting Mars by 7th house aspect infuses your drive with emotional passion. You act with heart, but may face mood-driven conflicts."
        ),
        ("Jupiter", 7): (
            "Moon aspecting Jupiter by 7th house aspect promotes emotional wisdom and spiritual growth. You nurture others, but may idealize relationships."
        ),
        ("Saturn", 7): (
            "Moon aspecting Saturn by 7th house aspect brings emotional discipline and responsibility. You seek stability, but may feel emotionally restricted."
        ),
        ("Rahu", 7): (
            "Moon aspecting Rahu by 7th house aspect intensifies your emotional desires and ambitions. You crave fulfillment, but may face restlessness."
        ),
        ("Ketu", 7): (
            "Moon aspecting Ketu by 7th house aspect encourages emotional detachment and spiritual growth. You seek inner peace, but may feel emotionally distant."
        ),
        ("Ascendant", 7): (
            "Moon aspecting Ascendant by 7th house aspect enhances your personality with sensitivity and intuition. You connect emotionally, but may be overly reactive."
        ),
        ("Midheaven", 7): (
            "Moon aspecting Midheaven by 7th house aspect brings emotional nurturing to your career. You shine in caregiving roles, but may face public emotional challenges."
        ),
    },
    "Mercury": {
        ("Sun", 7): (
            "Mercury aspecting Sun by 7th house aspect sharpens your intellect with confidence and clarity. You communicate authoritatively, but may be overly assertive."
        ),
        ("Moon", 7): (
            "Mercury aspecting Moon by 7th house aspect blends intellect with emotional intuition. You express feelings clearly, but may overanalyze emotions."
        ),
        ("Venus", 7): (
            "Mercury aspecting Venus by 7th house aspect enhances your relationships with charm and wit. You communicate lovingly, but may be superficial."
        ),
        ("Mars", 7): (
            "Mercury aspecting Mars by 7th house aspect fuels your drive with intellectual energy. You act decisively, but may be argumentative."
        ),
        ("Jupiter", 7): (
            "Mercury aspecting Jupiter by 7th house aspect promotes wisdom through clear communication. You teach effectively, but may be overly verbose."
        ),
        ("Saturn", 7): (
            "Mercury aspecting Saturn by 7th house aspect brings disciplined thinking and communication. You plan meticulously, but may be overly cautious."
        ),
        ("Rahu", 7): (
            "Mercury aspecting Rahu by 7th house aspect intensifies your intellectual ambitions. You pursue knowledge aggressively, but may be manipulative."
        ),
        ("Ketu", 7): (
            "Mercury aspecting Ketu by 7th house aspect encourages detachment from intellectual pursuits. You seek intuitive wisdom, but may lack focus."
        ),
        ("Ascendant", 7): (
            "Mercury aspecting Ascendant by 7th house aspect enhances your personality with wit and intellect. You communicate effectively, but may be restless."
        ),
        ("Midheaven", 7): (
            "Mercury aspecting Midheaven by 7th house aspect boosts your career with communication skills. You excel in intellectual roles, but may change paths frequently."
        ),
    },
    "Venus": {
        ("Sun", 7): (
            "Venus aspecting Sun by 7th house aspect infuses your identity with charm and harmony. You shine in relationships, but may seek excessive admiration."
        ),
        ("Moon", 7): (
            "Venus aspecting Moon by 7th house aspect fosters emotional harmony and love. You nurture relationships, but may be overly attached."
        ),
        ("Mercury", 7): (
            "Venus aspecting Mercury by 7th house aspect enhances your communication with charm and diplomacy. You speak beautifully, but may avoid hard truths."
        ),
        ("Mars", 7): (
            "Venus aspecting Mars by 7th house aspect blends passion with harmony in your actions. You pursue love dynamically, but may face conflicts."
        ),
        ("Jupiter", 7): (
            "Venus aspecting Jupiter by 7th house aspect promotes wisdom through harmonious relationships. You attract beneficial partnerships, but may idealize."
        ),
        ("Saturn", 7): (
            "Venus aspecting Saturn by 7th house aspect brings discipline to your relationships. You seek lasting love, but may face delays or restrictions."
        ),
        ("Rahu", 7): (
            "Venus aspecting Rahu by 7th house aspect intensifies your desire for love and luxury. You pursue beauty, but may face illusions."
        ),
        ("Ketu", 7): (
            "Venus aspecting Ketu by 7th house aspect encourages detachment from worldly love. You seek spiritual bonds, but may feel disconnected."
        ),
        ("Ascendant", 7): (
            "Venus aspecting Ascendant by 7th house aspect enhances your personality with charm and grace. You attract others, but may focus on appearances."
        ),
        ("Midheaven", 7): (
            "Venus aspecting Midheaven by 7th house aspect boosts your career in arts or diplomacy. You shine publicly, but may prioritize aesthetics."
        ),
    },
    "Mars": {
        ("Sun", 4): (
            "Mars aspecting Sun by 4th house aspect energizes your identity with courage and protection. You defend your ego, but may face domestic conflicts."
        ),
        ("Moon", 4): (
            "Mars aspecting Moon by 4th house aspect fuels your emotions with passion and protectiveness. You guard your heart, but may be overly reactive."
        ),
        ("Mercury", 4): (
            "Mars aspecting Mercury by 4th house aspect sharpens your intellect with decisive energy. You communicate boldly, but may be argumentative."
        ),
        ("Venus", 4): (
            "Mars aspecting Venus by 4th house aspect infuses your relationships with passion and energy. You love intensely, but may face domestic tension."
        ),
        ("Jupiter", 4): (
            "Mars aspecting Jupiter by 4th house aspect blends wisdom with protective energy. You defend beliefs, but may be overly aggressive."
        ),
        ("Saturn", 4): (
            "Mars aspecting Saturn by 4th house aspect creates tension between action and discipline. You work hard, but may face delays or frustration."
        ),
        ("Rahu", 4): (
            "Mars aspecting Rahu by 4th house aspect intensifies your ambitions with aggressive energy. You pursue goals boldly, but may face instability."
        ),
        ("Ketu", 4): (
            "Mars aspecting Ketu by 4th house aspect encourages detachment from worldly drives. You act spiritually, but may lack direction."
        ),
        ("Ascendant", 4): (
            "Mars aspecting Ascendant by 4th house aspect enhances your personality with energy and courage. You protect your identity, but may be combative."
        ),
        ("край", 4): (
            "Mars aspecting Midheaven by 4th house aspect boosts your career with dynamic energy. You excel in action-oriented roles, but may face conflicts."
        ),
        ("Sun", 7): (
            "Mars aspecting Sun by 7th house aspect fuels your identity with assertive energy. You lead boldly, but may face ego conflicts."
        ),
        ("Moon", 7): (
            "Mars aspecting Moon by 7th house aspect intensifies your emotions with passion. You act with heart, but may face emotional conflicts."
        ),
        ("Mercury", 7): (
            "Mars aspecting Mercury by 7th house aspect sharpens your intellect with assertive communication. You speak decisively, but may be confrontational."
        ),
        ("Venus", 7): (
            "Mars aspecting Venus by 7th house aspect infuses your relationships with passion and drive. You love dynamically, but may face disputes."
        ),
        ("Jupiter", 7): (
            "Mars aspecting Jupiter by 7th house aspect blends wisdom with assertive energy. You pursue beliefs boldly, but may be dogmatic."
        ),
        ("Saturn", 7): (
            "Mars aspecting Saturn by 7th house aspect creates tension between action and discipline. You strive for goals, but may face resistance."
        ),
        ("Rahu", 7): (
            "Mars aspecting Rahu by 7th house aspect intensifies your ambitions with aggressive drive. You chase goals, but may face illusions."
        ),
        ("Ketu", 7): (
            "Mars aspecting Ketu by 7th house aspect encourages detachment from worldly drives. You act spiritually, but may lack focus."
        ),
        ("Ascendant", 7): (
            "Mars aspecting Ascendant by 7th house aspect enhances your personality with assertiveness. You lead dynamically, but may be confrontational."
        ),
        ("Midheaven", 7): (
            "Mars aspecting Midheaven by 7th house aspect boosts your career with competitive energy. You excel in leadership, but may face rivalry."
        ),
        ("Sun", 8): (
            "Mars aspecting Sun by 8th house aspect fuels your identity with transformative energy. You face challenges boldly, but may encounter power struggles."
        ),
        ("Moon", 8): (
            "Mars aspecting Moon by 8th house aspect intensifies your emotions with transformative passion. You feel deeply, but may face emotional upheavals."
        ),
        ("Mercury", 8): (
            "Mars aspecting Mercury by 8th house aspect sharpens your intellect with investigative energy. You probe deeply, but may be secretive."
        ),
        ("Venus", 8): (
            "Mars aspecting Venus by 8th house aspect infuses your relationships with intense passion. You love deeply, but may face jealousy."
        ),
        ("Jupiter", 8): (
            "Mars aspecting Jupiter by 8th house aspect blends wisdom with transformative energy. You seek truth, but may face hidden challenges."
        ),
        ("Saturn", 8): (
            "Mars aspecting Saturn by 8th house aspect creates tension between action and endurance. You face hardships, but may be overly intense."
        ),
        ("Rahu", 8): (
            "Mars aspecting Rahu by 8th house aspect intensifies your ambitions with transformative drive. You pursue power, but may face crises."
        ),
        ("Ketu", 8): (
            "Mars aspecting Ketu by 8th house aspect encourages spiritual transformation. You seek liberation, but may avoid emotional depth."
        ),
        ("Ascendant", 8): (
            "Mars aspecting Ascendant by 8th house aspect enhances your personality with transformative energy. You face challenges, but may be secretive."
        ),
        ("Midheaven", 8): (
            "Mars aspecting Midheaven by 8th house aspect boosts your career with transformative energy. You excel in intense roles, but may face upheaval."
        ),
    },
    "Jupiter": {
        ("Sun", 5): (
            "Jupiter aspecting Sun by 5th house aspect enhances your identity with wisdom and creativity. You inspire others, but may be overly confident."
        ),
        ("Moon", 5): (
            "Jupiter aspecting Moon by 5th house aspect fosters emotional wisdom and creativity. You nurture with optimism, but may idealize feelings."
        ),
        ("Mercury", 5): (
            "Jupiter aspecting Mercury by 5th house aspect sharpens your intellect with philosophical wisdom. You teach creatively, but may be verbose."
        ),
        ("Venus", 5): (
            "Jupiter aspecting Venus by 5th house aspect infuses your relationships with wisdom and harmony. You love generously, but may indulge."
        ),
        ("Mars", 5): (
            "Jupiter aspecting Mars by 5th house aspect blends wisdom with creative energy. You act with purpose, but may be overly zealous."
        ),
        ("Saturn", 5): (
            "Jupiter aspecting Saturn by 5th house aspect balances wisdom with discipline. You achieve through effort, but may face delays."
        ),
        ("Rahu", 5): (
            "Jupiter aspecting Rahu by 5th house aspect intensifies your ambitions with wisdom. You pursue goals creatively, but may face illusions."
        ),
        ("Ketu", 5): (
            "Jupiter aspecting Ketu by 5th house aspect encourages spiritual creativity. You seek inner wisdom, but may detach from worldly gains."
        ),
        ("Ascendant", 5): (
            "Jupiter aspecting Ascendant by 5th house aspect enhances your personality with wisdom and optimism. You inspire, but may be overly idealistic."
        ),
        ("Midheaven", 5): (
            "Jupiter aspecting Midheaven by 5th house aspect boosts your career with creative wisdom. You shine in teaching, but may overreach."
        ),
        ("Sun", 7): (
            "Jupiter aspecting Sun by 7th house aspect enhances your identity with wisdom and optimism. You lead harmoniously, but may be dogmatic."
        ),
        ("Moon", 7): (
            "Jupiter aspecting Moon by 7th house aspect fosters emotional wisdom and nurturing. You connect spiritually, but may idealize."
        ),
        ("Mercury", 7): (
            "Jupiter aspecting Mercury by 7th house aspect sharpens your intellect with philosophical insight. You communicate wisely, but may be verbose."
        ),
        ("Venus", 7): (
            "Jupiter aspecting Venus by 7th house aspect infuses your relationships with wisdom and harmony. You attract beneficial partners, but may idealize."
        ),
        ("Mars", 7): (
            "Jupiter aspecting Mars by 7th house aspect blends wisdom with assertive energy. You act with purpose, but may be overly aggressive."
        ),
        ("Saturn", 7): (
            "Jupiter aspecting Saturn by 7th house aspect balances wisdom with discipline. You achieve harmony, but may face delays."
        ),
        ("Rahu", 7): (
            "Jupiter aspecting Rahu by 7th house aspect intensifies your ambitions with wisdom. You pursue goals ethically, but may face illusions."
        ),
        ("Ketu", 7): (
            "Jupiter aspecting Ketu by 7th house aspect encourages spiritual detachment. You seek inner wisdom, but may disconnect."
        ),
        ("Ascendant", 7): (
            "Jupiter aspecting Ascendant by 7th house aspect enhances your personality with wisdom and grace. You attract harmony, but may be idealistic."
        ),
        ("Midheaven", 7): (
            "Jupiter aspecting Midheaven by 7th house aspect boosts your career with wisdom and ethics. You shine in leadership, but may overpromise."
        ),
        ("Sun", 9): (
            "Jupiter aspecting Sun by 9th house aspect enhances your identity with spiritual wisdom. You shine as a guide, but may be overly dogmatic."
        ),
        ("Moon", 9): (
            "Jupiter aspecting Moon by 9th house aspect fosters emotional wisdom and spirituality. You nurture through faith, but may idealize beliefs."
        ),
        ("Mercury", 9): (
            "Jupiter aspecting Mercury by 9th house aspect sharpens your intellect with philosophical depth. You teach profoundly, but may be scattered."
        ),
        ("Venus", 9): (
            "Jupiter aspecting Venus by 9th house aspect infuses your relationships with spiritual harmony. You love ethically, but may idealize."
        ),
        ("Mars", 9): (
            "Jupiter aspecting Mars by 9th house aspect blends wisdom with spiritual drive. You pursue truth, but may be zealous."
        ),
        ("Saturn", 9): (
            "Jupiter aspecting Saturn by 9th house aspect balances wisdom with disciplined faith. You achieve spiritually, but may face delays."
        ),
        ("Rahu", 9): (
            "Jupiter aspecting Rahu by 9th house aspect intensifies your ambitions with spiritual wisdom. You pursue truth, but may face illusions."
        ),
        ("Ketu", 9): (
            "Jupiter aspecting Ketu by 9th house aspect encourages spiritual liberation. You seek ultimate truth, but may detach from worldly goals."
        ),
        ("Ascendant", 9): (
            "Jupiter aspecting Ascendant by 9th house aspect enhances your personality with spiritual wisdom. You inspire, but may be overly idealistic."
        ),
        ("Midheaven", 9): (
            "Jupiter aspecting Midheaven by 9th house aspect boosts your career with spiritual leadership. You shine as a guide, but may overextend."
        ),
    },
    "Saturn": {
        ("Sun", 3): (
            "Saturn aspecting Sun by 3rd house aspect disciplines your identity with effort and perseverance. You achieve through hard work, but may feel restricted."
        ),
        ("Moon", 3): (
            "Saturn aspecting Moon by 3rd house aspect brings discipline to your emotions through effort. You seek stability, but may feel emotionally restrained."
        ),
        ("Mercury", 3): (
            "Saturn aspecting Mercury by 3rd house aspect sharpens your intellect with disciplined communication. You plan carefully, but may be overly cautious."
        ),
        ("Venus", 3): (
            "Saturn aspecting Venus by 3rd house aspect disciplines your relationships with responsibility. You value loyalty, but may face delays in love."
        ),
        ("Mars", 3): (
            "Saturn aspecting Mars by 3rd house aspect channels your drive with disciplined effort. You act methodically, but may face frustration."
        ),
        ("Jupiter", 3): (
            "Saturn aspecting Jupiter by 3rd house aspect balances wisdom with disciplined effort. You achieve through perseverance, but may be rigid."
        ),
        ("Rahu", 3): (
            "Saturn aspecting Rahu by 3rd house aspect disciplines your ambitions with hard work. You pursue goals steadily, but may face obstacles."
        ),
        ("Ketu", 3): (
            "Saturn aspecting Ketu by 3rd house aspect encourages detachment through disciplined effort. You seek spiritual clarity, but may feel isolated."
        ),
        ("Ascendant", 3): (
            "Saturn aspecting Ascendant by 3rd house aspect enhances your personality with discipline and effort. You persevere, but may feel restricted."
        ),
        ("Midheaven", 3): (
            "Saturn aspecting Midheaven by 3rd house aspect boosts your career with disciplined effort. You achieve steadily, but may face delays."
        ),
        ("Sun", 7): (
            "Saturn aspecting Sun by 7th house aspect disciplines your identity with responsibility. You seek respect, but may face ego challenges."
        ),
        ("Moon", 7): (
            "Saturn aspecting Moon by 7th house aspect brings emotional discipline and stability. You value commitment, but may feel emotionally burdened."
        ),
        ("Mercury", 7): (
            "Saturn aspecting Mercury by 7th house aspect sharpens your intellect with disciplined thinking. You communicate methodically, but may be rigid."
        ),
        ("Venus", 7): (
            "Saturn aspecting Venus by 7th house aspect disciplines your relationships with loyalty. You seek lasting bonds, but may face delays."
        ),
        ("Mars", 7): (
            "Saturn aspecting Mars by 7th house aspect channels your drive with discipline. You act responsibly, but may face conflicts."
        ),
        ("Jupiter", 7): (
            "Saturn aspecting Jupiter by 7th house aspect balances wisdom with responsibility. You achieve ethically, but may face restrictions."
        ),
        ("Rahu", 7): (
            "Saturn aspecting Rahu by 7th house aspect disciplines your ambitions with responsibility. You pursue goals steadily, but may face illusions."
        ),
        ("Ketu", 7): (
            "Saturn aspecting Ketu by 7th house aspect encourages spiritual detachment through discipline. You seek clarity, but may feel isolated."
        ),
        ("Ascendant", 7): (
            "Saturn aspecting Ascendant by 7th house aspect enhances your personality with discipline and responsibility. You lead steadily, but may feel burdened."
        ),
        ("Midheaven", 7): (
            "Saturn aspecting Midheaven by 7th house aspect boosts your career with disciplined leadership. You achieve lasting success, but may face delays."
        ),
        ("Sun", 10): (
            "Saturn aspecting Sun by 10th house aspect disciplines your identity with career responsibility. You achieve authority, but may face heavy duties."
        ),
        ("Moon", 10): (
            "Saturn aspecting Moon by 10th house aspect brings emotional discipline to your career. You nurture publicly, but may feel burdened."
        ),
        ("Mercury", 10): (
            "Saturn aspecting Mercury by 10th house aspect sharpens your intellect with career discipline. You plan strategically, but may be overly serious."
        ),
        ("Venus", 10): (
            "Saturn aspecting Venus by 10th house aspect disciplines your relationships with career focus. You value professional bonds, but may face delays."
        ),
        ("Mars", 10): (
            "Saturn aspecting Mars by 10th house aspect channels your drive with career discipline. You achieve through effort, but may face obstacles."
        ),
        ("Jupiter", 10): (
            "Saturn aspecting Jupiter by 10th house aspect balances wisdom with career responsibility. You achieve ethically, but may face delays."
        ),
        ("Rahu", 10): (
            "Saturn aspecting Rahu by 10th house aspect disciplines your ambitions with career focus. You pursue status, but may face setbacks."
        ),
        ("Ketu", 10): (
            "Saturn aspecting Ketu by 10th house aspect encourages detachment from worldly status. You seek spiritual purpose, but may feel unmotivated."
        ),
        ("Ascendant", 10): (
            "Saturn aspecting Ascendant by 10th house aspect enhances your personality with career discipline. You lead responsibly, but may feel burdened."
        ),
        ("Midheaven", 10): (
            "Saturn aspecting Midheaven by 10th house aspect boosts your career with enduring success. You excel in leadership, but may face heavy responsibilities."
        ),
    },
    "Rahu": {
        ("Sun", 7): (
            "Rahu aspecting Sun by 7th house aspect creates tension in your sense of self and authority. You may feel driven "
            "to seek recognition but face challenges with ego or power dynamics."
        ),
        ("Moon", 7): (
            "Rahu aspecting Moon by 7th house aspect intensifies your emotions and desires. You may experience restlessness or "
            "crave emotional fulfillment, needing to balance intensity with stability."
        ),
        ("Mercury", 7): (
            "Rahu aspecting Mercury by 7th house aspect amplifies your intellectual ambitions with intensity. You pursue knowledge aggressively, but may be manipulative or scattered."
        ),
        ("Venus", 7): (
            "Rahu aspecting Venus by 7th house aspect intensifies your desire for love and luxury. You chase beauty, but may face illusions or obsession."
        ),
        ("Mars", 7): (
            "Rahu aspecting Mars by 7th house aspect fuels your drive with intense ambition. You pursue goals boldly, but may face conflicts or deception."
        ),
        ("Jupiter", 7): (
            "Rahu aspecting Jupiter by 7th house aspect amplifies your pursuit of wisdom with intensity. You seek spiritual growth, but may face illusions or dogma."
        ),
        ("Saturn", 7): (
            "Rahu aspecting Saturn by 7th house aspect creates tension between ambition and discipline. You strive for goals, but may face delays or illusions."
        ),
        ("Ketu", 7): (
            "Rahu aspecting Ketu by 7th house aspect highlights the karmic axis, intensifying your spiritual journey. You seek balance, but may face inner conflict."
        ),
        ("Ascendant", 7): (
            "Rahu aspecting Ascendant by 7th house aspect intensifies your personality with ambition and magnetism. You attract attention, but may be restless."
        ),
        ("Midheaven", 7): (
            "Rahu aspecting Midheaven by 7th house aspect amplifies your career ambitions with intensity. You chase status, but may face illusions or setbacks."
        ),
    },
    "Ketu": {
        ("Sun", 7): (
            "Ketu aspecting Sun by 7th house aspect encourages detachment from ego and authority. You seek spiritual clarity, but may feel disconnected from recognition."
        ),
        ("Moon", 7): (
            "Ketu aspecting Moon by 7th house aspect promotes emotional detachment and spiritual growth. You seek inner peace, but may feel emotionally distant."
        ),
        ("Mercury", 7): (
            "Ketu aspecting Mercury by 7th house aspect encourages detachment from intellectual pursuits. You seek intuitive wisdom, but may lack focus."
        ),
        ("Venus", 7): (
            "Ketu aspecting Venus by 7th house aspect promotes detachment from worldly love and luxury. You seek spiritual bonds, but may feel disconnected."
        ),
        ("Mars", 7): (
            "Ketu aspecting Mars by 7th house aspect encourages detachment from aggressive drives. You act spiritually, but may lack motivation."
        ),
        ("Jupiter", 7): (
            "Ketu aspecting Jupiter by 7th house aspect promotes spiritual wisdom and detachment. You seek ultimate truth, but may disconnect from worldly goals."
        ),
        ("Saturn", 7): (
            "Ketu aspecting Saturn by 7th house aspect encourages detachment from worldly responsibilities. You seek spiritual clarity, but may feel isolated."
        ),
        ("Rahu", 7): (
            "Ketu aspecting Rahu by 7th house aspect highlights the karmic axis, promoting spiritual balance. You seek liberation, but may face inner tension."
        ),
        ("Ascendant", 7): (
            "Ketu aspecting Ascendant by 7th house aspect enhances your personality with spiritual detachment. You seek inner truth, but may feel disconnected."
        ),
        ("Midheaven", 7): (
            "Ketu aspecting Midheaven by 7th house aspect promotes detachment from career ambitions. You seek spiritual purpose, but may lack worldly drive."
        ),
    },
}

script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
EPHEMERIS_PATH = os.path.join(project_dir, "data", "ephe")
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

def get_nakshatra(longitude):
    """Returns the Nakshatra for a given longitude."""
    longitude = longitude % 360
    for nakshatra, start, end in NAKSHATRAS:
        if start <= longitude < end:
            return nakshatra
    return NAKSHATRAS[-1][0]  # Revati if longitude is at 360°

# --- Core Functions ---
class VedicChartCalculator:
    def __init__(self, ephemeris_path=EPHEMERIS_PATH, geocode_api_key=GEOCODE_API_KEY):
        swe.set_ephe_path(ephemeris_path)
        self.geocode_api_key = geocode_api_key
        self.tf = TimezoneFinder()
        swe.set_sid_mode(swe.SIDM_LAHIRI)  # Set Lahiri Ayanamsa

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
                    offset_hours = int(lon / 15)
                    timezone_str = f"Etc/GMT{+offset_hours:+d}"
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
            localized_dt = local_tz.localize(local_dt, is_dst=None)
        except (pytz.exceptions.AmbiguousTimeError, pytz.exceptions.NonExistentTimeError) as e:
            try:
                localized_dt = local_tz.localize(local_dt, is_dst=False)
                print(f"Warning: Ambiguous or non-existent local time {local_dt} in {timezone_str}. Used standard time. Details: {e}")
            except Exception as e_inner:
                raise ValueError(f"Could not resolve ambiguous/non-existent local time {local_dt} in {timezone_str}: {e_inner}")

        utc_dt = localized_dt.astimezone(pytz.utc)
        jd_et, jd_ut = swe.utc_to_jd(
            utc_dt.year, utc_dt.month, utc_dt.day,
            utc_dt.hour, utc_dt.minute, utc_dt.second, 1
        )

        return utc_dt, jd_ut

    def calculate_natal_chart(self, year, month, day, hour, minute, city_country_str):
            """Calculates a Vedic natal chart."""
            lat, lon, timezone_str = self.get_coordinates_and_timezone(city_country_str)
            utc_dt, jd_ut = self.get_utc_datetime_and_julian_day(year, month, day, hour, minute, lat, lon, timezone_str)

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
                "midheaven": {},
                "interpretations": {}
            }

            # Calculate Ayanamsa
            ayanamsa = swe.get_ayanamsa_ut(jd_ut)

            # Calculate Planets
            swe.set_topo(lon, lat, 0)
            iflag = swe.FLG_SWIEPH | swe.FLG_SPEED | swe.FLG_SIDEREAL

            planet_positions_for_aspects = {}
            for name, p_id in PLANETS.items():
                xx, rflags = swe.calc_ut(jd_ut, p_id, iflag)
                longitude = xx[0]
                is_retrograde = xx[3] < 0
                sign, deg, min_arc, sec_arc = degree_to_dms_sign(longitude)
                nakshatra = get_nakshatra(longitude)

                if name == "Ketu":
                    longitude = (longitude + 180) % 360
                    sign, deg, min_arc, sec_arc = degree_to_dms_sign(longitude)
                    nakshatra = get_nakshatra(longitude)

                chart_data["planets"].append({
                    "name": name,
                    "longitude": longitude,
                    "sign": sign,
                    "sign_long_deg": deg,
                    "sign_min": min_arc,
                    "sign_sec": sec_arc,
                    "nakshatra": nakshatra,
                    "is_retrograde": is_retrograde,
                    "speed": xx[3],
                    "house_number": None
                })
                planet_positions_for_aspects[name] = longitude

            # Calculate Ascendant and Midheaven
            delta_t = swe.deltat(jd_ut)
            jd_et = jd_ut + delta_t
            cusps, ascmc = swe.houses_ex(jd_et, lat, lon, b'P', iflag)
            asc_long = ascmc[0]
            mc_long = ascmc[1]
            asc_long = (asc_long - ayanamsa) % 360
            mc_long = (mc_long - ayanamsa) % 360
            sign_asc, deg_asc, min_asc, sec_asc = degree_to_dms_sign(asc_long)
            sign_mc, deg_mc, min_mc, sec_mc = degree_to_dms_sign(mc_long)

            chart_data["ascendant"] = {
                "longitude": asc_long,
                "sign": sign_asc,
                "sign_long_deg": deg_asc,
                "sign_min": min_asc,
                "sign_sec": sec_asc
            }
            chart_data["midheaven"] = {
                "longitude": mc_long,
                "sign": sign_mc,
                "sign_long_deg": deg_mc,
                "sign_min": min_mc,
                "sign_sec": sec_mc
            }
            planet_positions_for_aspects["Ascendant"] = asc_long
            planet_positions_for_aspects["Midheaven"] = mc_long

            # Calculate Whole-Sign Houses
            asc_sign_index = SIGNS.index(sign_asc)
            for i in range(12):
                house_sign = SIGNS[(asc_sign_index + i) % 12]
                house_start = ((asc_sign_index + i) * 30) % 360
                sign, deg, min_arc, sec_arc = degree_to_dms_sign(house_start)
                chart_data["houses"].append({
                    "house_number": i + 1,
                    "longitude": house_start,
                    "sign": house_sign,
                    "sign_long_deg": deg,
                    "sign_min": min_arc,
                    "sign_sec": sec_arc
                })

            # Determine Planet House Positions
            for planet_entry in chart_data["planets"]:
                planet_sign = planet_entry["sign"]
                for house in chart_data["houses"]:
                    if planet_sign == house["sign"]:
                        planet_entry["house_number"] = house["house_number"]
                        break

            # Calculate Vedic Aspects
            for planet1 in chart_data["planets"]:
                planet1_name = planet1["name"]
                planet1_sign_index = SIGNS.index(planet1["sign"])
                aspects = VEDIC_ASPECTS.get(planet1_name, [7])

                for aspect_distance in aspects:
                    target_sign_index = (planet1_sign_index + aspect_distance - 1) % 12
                    target_sign = SIGNS[target_sign_index]

                    for planet2 in chart_data["planets"] + [
                        {"name": "Ascendant", "sign": sign_asc},
                        {"name": "Midheaven", "sign": sign_mc}
                    ]:
                        planet2_name = planet2["name"]
                        if planet1_name == planet2_name:
                            continue
                        if planet2["sign"] == target_sign:
                            chart_data["aspects"].append({
                                "body1": planet1_name,
                                "body2": planet2_name,
                                "aspect_type": f"{aspect_distance}th House",
                                "aspect_distance": aspect_distance,  # Store the numeric distance
                                "orb": None
                            })

            # Add Interpretations
            chart_data["interpretations"] = {
                "planets_in_signs": [],
                "planets_in_houses": [],
                "nakshatras": [],
                "aspects": []
            }
            for planet in chart_data["planets"]:
                planet_name = planet["name"]  # Fixed typo: 'pianeta' to 'planet'
                sign = planet["sign"]
                house = planet["house_number"]
                nakshatra = planet["nakshatra"]

                # Planet in Sign
                if planet_name in PLANET_IN_SIGN_INTERPRETATIONS_VEDIC and sign in PLANET_IN_SIGN_INTERPRETATIONS_VEDIC[planet_name]:
                    chart_data["interpretations"]["planets_in_signs"].append({
                        "planet": planet_name,
                        "sign": sign,
                        "interpretation": PLANET_IN_SIGN_INTERPRETATIONS_VEDIC[planet_name][sign]
                    })

                # Planet in House
                if planet_name in PLANET_IN_HOUSE_INTERPRETATIONS_VEDIC and house in PLANET_IN_HOUSE_INTERPRETATIONS_VEDIC[planet_name]:
                    chart_data["interpretations"]["planets_in_houses"].append({
                        "planet": planet_name,
                        "house": house,
                        "interpretation": PLANET_IN_HOUSE_INTERPRETATIONS_VEDIC[planet_name][house]
                    })

                # Nakshatra
                if nakshatra in NAKSHATRA_INTERPRETATIONS:
                    chart_data["interpretations"]["nakshatras"].append({
                        "planet": planet_name,
                        "nakshatra": nakshatra,
                        "interpretation": NAKSHATRA_INTERPRETATIONS[nakshatra]
                    })

            # Aspect Interpretations
            for aspect in chart_data["aspects"]:
                body1, body2, aspect_type = aspect["body1"], aspect["body2"], aspect["aspect_type"]
                aspect_distance = aspect["aspect_distance"]  # Use stored numeric distance
                if body1 in VEDIC_ASPECT_INTERPRETATIONS and (body2, aspect_distance) in VEDIC_ASPECT_INTERPRETATIONS[body1]:
                    chart_data["interpretations"]["aspects"].append({
                        "body1": body1,
                        "body2": body2,
                        "aspect_type": aspect_type,
                        "interpretation": VEDIC_ASPECT_INTERPRETATIONS[body1][(body2, aspect_distance)]
                    })

            swe.close()
            return chart_data

# --- Example Usage ---
if __name__ == "__main__":
    calculator = VedicChartCalculator()
    print("\nCalculating Vedic Chart for Jamshedpur, March 24, 1994, 00:40")
    chart = calculator.calculate_natal_chart(1994, 3, 24, 0, 40, "Jamshedpur, Jharkhand, India")
    print(json.dumps(chart, indent=2))