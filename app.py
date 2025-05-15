#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Streamlit UI for AI Astrologer Agent
A production-ready astrology app with a celestial-themed UI, icons, and responsive design.
"""

import streamlit as st
import datetime
import json
from src.chart_calculator import ChartCalculator

# Set page configuration with a celestial favicon and title
st.set_page_config(
    layout="wide",
    page_title="🌌 AI AstroAgent",
    page_icon="🌙",
    initial_sidebar_state="expanded"
)

# Astrology-themed CSS for styling
st.markdown("""
    <style>
    /* Global styles */
    .stApp {
        background: #000;
        color: #e6e6fa;
        font-family: 'Georgia', serif;
    }
    .main-header {
        color: #ffd700;
        font-size: 2.5rem;
        text-align: center;
        text-shadow: 0 0 10px #b8860b;
    }
    .sub-header {
        color: #e6e6fa;
        font-size: 1.5rem;
        margin-top: 1rem;
        display: flex;
        justify-content: center;
    }
    .st-emotion-cache-k2z1pe, .st-emotion-cache-1ihwvbb  {
        background: #000 !important;
            }
    .sidebar .sidebar-content {
        background: #000;
        border-right: 2px solid #ffd700;
    }
    .stButton>button {
        background-color: #ffd700;
        color: #1a0b3b;
        border-radius: 10px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #b8860b;
        color: #ffffff;
    }
    .stTextInput>div>input, .stDateInput>div>input, .stTimeInput>div>input {
        background-color: #000;
        color: #e6e6fa;
        border: 1px solid #ffd700;
        border-radius: 5px;
    }
    .stMetric {
        background-color: #000;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .stExpander {
        background-color: #000;
        border-radius: 10px;
        border: 1px solid #ffd700;
    }
    .stTabs [data-baseweb="tab"] {
        color: #e6e6fa;
        background-color: #000;
        border-radius: 5px 5px 0 0;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #ffd700;
        color: #1a0b3b;
        font-weight: bold;
    }
    /* Celestial icons for sections */
    .section-icon {
        font-size: 1.2rem;
        margin-right: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
def initialize_session_state():
    defaults = {
        "chart_data": None,
        "interpretations": None,
        "qa_agent": None,
        "error_message": None,
        "qna_history": []
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

initialize_session_state()

# Astrology-themed color palette
COLORS = {
    "primary": "#ffd700",  # Gold for celestial accents
    "background": "#1a0b3b",  # Deep cosmic purple
    "text": "#e6e6fa",  # Light lavender for text
    "secondary": "#000"  # Dark blue-purple for containers
}

# --- UI Layout ---
def render_header():
    st.markdown('<h1 class="main-header">🌌 AI AstroAgent</h1>', unsafe_allow_html=True)
    st.markdown('<span class="sub-header">Discover your cosmic blueprint with Vedic astrology insights</span>', unsafe_allow_html=True)

def render_sidebar():
    with st.sidebar:
        st.markdown('<h2 class="sub-header">✨ Birth Details</h2>', unsafe_allow_html=True)
        with st.form(key="birth_input_form"):
            user_name = st.text_input("Full Name", placeholder="Enter your name", help="Your name for personalized reports")
            birth_date = st.date_input(
                "Birth Date",
                value=datetime.date(1990, 1, 1),
                min_value=datetime.date(1900, 1, 1),
                max_value=datetime.date.today(),
                help="Select your date of birth"
            )
            birth_time = st.time_input(
                "Birth Time (24-hour)",
                value=datetime.time(12, 0),
                step=300,
                help="Enter exact time of birth"
            )
            birth_location = st.text_input(
                "Birth Location",
                value="New York, NY, USA",
                placeholder="e.g., City, State, Country",
                help="Enter city and country or city, state, country"
            )
            submit = st.form_submit_button("🌠 Calculate Chart")
        st.markdown("---")
        st.markdown(
            """
            **Disclaimer:** This AI Astrologer is for entertainment and informational purposes only. 
            Astrological insights are subjective and not a substitute for professional advice.
            """,
            unsafe_allow_html=True
        )
    return user_name, birth_date, birth_time, birth_location, submit

def render_chart_metrics(chart_data, user_name):
    st.markdown(f'<h2 class="sub-header">🌟 Vedic Report for {user_name}</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="sub-header"><span class="section-icon">🪐</span>Key Chart Points</h3>', unsafe_allow_html=True)
    
    sun_planet = next((p for p in chart_data.get("planets", []) if p["name"] == "Sun"), None)
    moon_planet = next((p for p in chart_data.get("planets", []) if p["name"] == "Moon"), None)
    asc = chart_data.get("ascendant", {})
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if sun_planet:
            st.metric("☉ Sun Sign", f"{sun_planet.get('sign', 'N/A')} {sun_planet.get('sign_long_deg', '')}°")
    with col2:
        if moon_planet:
            st.metric("☾ Moon Sign", f"{moon_planet.get('sign', 'N/A')} {moon_planet.get('sign_long_deg', '')}°")
    with col3:
        if asc:
            st.metric("⬆ Ascendant", f"{asc.get('sign', 'N/A')} {asc.get('sign_long_deg', '')}°")
    
    with st.expander("📜 Full Chart Data (JSON)"):
        st.json(chart_data)

def render_interpretations(interpretations):
    st.markdown('<h3 class="sub-header"><span class="section-icon">🔮</span>Astrological Interpretations</h3>', unsafe_allow_html=True)
    
    tab_titles = [
        f"🪐 Planets in Signs ({len(interpretations.get('planets_in_signs', []))})",
        f"🏛 Planets in Houses ({len(interpretations.get('planets_in_houses', []))})",
        f"🔗 Aspects ({len(interpretations.get('aspects', []))})",
        f"🌙 Nakshatras ({len(interpretations.get('nakshatras', []))})"
    ]
    tabs = st.tabs(tab_titles)
    
    with tabs[0]:
        for interp in interpretations.get("planets_in_signs", []):
            st.markdown(f"✨ **{interp.get('planet')} in {interp.get('sign')}**: {interp.get('interpretation')}")
    
    with tabs[1]:
        for interp in interpretations.get("planets_in_houses", []):
            st.markdown(f"🏠 **{interp.get('planet')} in {interp.get('house')}**: {interp.get('interpretation')}")
    
    with tabs[2]:
        for interp in interpretations.get("aspects", []):
            st.markdown(f"🔗 {interp.get('interpretation')}")
    
    with tabs[3]:
        for interp in interpretations.get("nakshatras", []):
            st.markdown(f"🌟 {interp.get('interpretation')}")

def main():
    render_header()
    user_name, birth_date, birth_time, birth_location, calculate_button = render_sidebar()
    
    if calculate_button:
        # Reset session state
        st.session_state.chart_data = None
        st.session_state.interpretations = None
        st.session_state.qa_agent = None
        st.session_state.error_message = None
        st.session_state.qna_history = []
        
        if not birth_location.strip():
            st.session_state.error_message = "Birth location cannot be empty."
        else:
            try:
                with st.spinner("🌌 Calculating your natal chart..."):
                    calculator = ChartCalculator()
                    st.session_state.chart_data = calculator.calculate_natal_chart(
                        year=birth_date.year,
                        month=birth_date.month,
                        day=birth_date.day,
                        hour=birth_time.hour,
                        minute=birth_time.minute,
                        city_country_str=birth_location
                    )
                
                if st.session_state.chart_data and not st.session_state.chart_data.get("error"):
                    with st.spinner("🔮 Generating interpretations..."):
                        st.session_state.interpretations = st.session_state.chart_data.get('interpretations')
                    st.success("🌟 Chart and interpretations generated successfully!")
                else:
                    st.session_state.error_message = st.session_state.chart_data.get("error", "Unknown error during chart calculation.")
            
            except ValueError as ve:
                st.session_state.error_message = f"Input Error: {ve}"
            except Exception as e:
                st.session_state.error_message = f"Unexpected Error: {e}"
    
    if st.session_state.error_message:
        st.error(f"🚫 {st.session_state.error_message}")
    
    if st.session_state.chart_data and not st.session_state.error_message:
        render_chart_metrics(st.session_state.chart_data, user_name)
        
        if st.session_state.interpretations and not st.session_state.interpretations.get("error"):
            render_interpretations(st.session_state.interpretations)
        elif st.session_state.interpretations and st.session_state.interpretations.get("error"):
            st.warning(f"⚠ Could not generate interpretations: {st.session_state.interpretations.get('error')}")

if __name__ == "__main__":
    main()