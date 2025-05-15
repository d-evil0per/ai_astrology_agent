#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Streamlit UI for AI Astrologer Agent"""

import streamlit as st
import datetime
import json # For pretty printing chart data initially

# Adjust import paths if necessary based on where this app.py is run from.
# Assuming app.py is in /home/ubuntu/ai_astrology_agent/ and modules are in /home/ubuntu/ai_astrology_agent/src/
from src.chart_calculator import ChartCalculator
from src.interpretation_generator import InterpretationGenerator
from src.qa_agent import QAAgent

st.set_page_config(layout="wide", page_title="AI Astrologer")

# Initialize session state variables
if "chart_data" not in st.session_state:
    st.session_state.chart_data = None
if "interpretations" not in st.session_state:
    st.session_state.interpretations = None
if "qa_agent" not in st.session_state:
    st.session_state.qa_agent = None
if "error_message" not in st.session_state:
    st.session_state.error_message = None
if "qna_history" not in st.session_state:
    st.session_state.qna_history = []

# --- UI Layout ---
st.title("AI Astrologer Agent")
st.markdown("Enter your birth details to generate your natal chart and ask questions about it.")

# --- Input Form (Sidebar) ---
st.sidebar.header("Birth Details")
with st.sidebar.form(key="birth_input_form"):
    birth_date = st.date_input("Birth Date", value=datetime.date(1990, 1, 1))
    birth_time = st.time_input("Birth Time (24-hour format)", value=datetime.time(12, 0),step=300)
    birth_location = st.text_input("Birth Location (e.g., City, Country or City, State, Country)", value="New York, NY, USA")
    calculate_button = st.form_submit_button(label="Calculate Chart")

# --- Main Area --- 
if calculate_button:
    st.session_state.chart_data = None # Reset previous data
    st.session_state.interpretations = None
    st.session_state.qa_agent = None
    st.session_state.error_message = None
    st.session_state.qna_history = []

    if not birth_location.strip():
        st.session_state.error_message = "Birth location cannot be empty."
    else:
        try:
            with st.spinner("Calculating your natal chart..."):
                calculator = ChartCalculator() # Uses default ephe path and API key path
                st.session_state.chart_data = calculator.calculate_natal_chart(
                    year=birth_date.year,
                    month=birth_date.month,
                    day=birth_date.day,
                    hour=birth_time.hour,
                    minute=birth_time.minute,
                    city_country_str=birth_location
                )
            
            if st.session_state.chart_data and not st.session_state.chart_data.get("error"):
                with st.spinner("Generating interpretations..."):
                    interpreter = InterpretationGenerator()
                    st.session_state.interpretations = interpreter.generate_full_interpretation(st.session_state.chart_data)
                
                with st.spinner("Initializing Q&A Agent..."):
                    st.session_state.qa_agent = QAAgent(st.session_state.chart_data)
                st.success("Chart calculated and interpretations generated!")
            else:
                st.session_state.error_message = st.session_state.chart_data.get("error", "An unknown error occurred during chart calculation.")

        except ValueError as ve:
            st.session_state.error_message = f"Input Error: {ve}"
        except Exception as e:
            st.session_state.error_message = f"An unexpected error occurred: {e}"

if st.session_state.error_message:
    st.error(st.session_state.error_message)

if st.session_state.chart_data and not st.session_state.error_message:
    st.header("Your Natal Chart Insights")

    # Section 2: Chart Display (Simplified)
    st.subheader("Key Chart Points")
    bd = st.session_state.chart_data.get("birth_data", {})
    asc = st.session_state.chart_data.get("ascendant", {})
    mc = st.session_state.chart_data.get("midheaven", {})
    sun_planet = next((p for p in st.session_state.chart_data.get("planets", []) if p["name"] == "Sun"), None)
    moon_planet = next((p for p in st.session_state.chart_data.get("planets", []) if p["name"] == "Moon"), None)

    col1, col2, col3 = st.columns(3)
    if sun_planet:
        col1.metric("Sun Sign", f"{sun_planet.get('sign', 'N/A')} {sun_planet.get('sign_long_deg', '')}°")
    if moon_planet:
        col2.metric("Moon Sign", f"{moon_planet.get('sign', 'N/A')} {moon_planet.get('sign_long_deg', '')}°")
    if asc:
        col3.metric("Ascendant (Rising)", f"{asc.get('sign', 'N/A')} {asc.get('sign_long_deg', '')}°")
    
    with st.expander("Full Chart Data (JSON)"):
        st.json(st.session_state.chart_data)

    # Section 3: Interpretations
    if st.session_state.interpretations and not st.session_state.interpretations.get("error"):
        st.subheader("Astrological Interpretations")
        
        tab_titles = [
            f"Planets in Signs ({len(st.session_state.interpretations.get('planets_in_signs',[]))})", 
            f"Planets in Houses ({len(st.session_state.interpretations.get('planets_in_houses',[]))})", 
            f"Aspects ({len(st.session_state.interpretations.get('aspects',[]))})", 
            f"House Cusps ({len(st.session_state.interpretations.get('house_cusps',[]))})"
        ]
        planets_signs_tab, planets_houses_tab, aspects_tab, house_cusps_tab = st.tabs(tab_titles)

        with planets_signs_tab:
            for interp in st.session_state.interpretations.get("planets_in_signs", []):
                st.markdown(f"- {interp}")
        
        with planets_houses_tab:
            for interp in st.session_state.interpretations.get("planets_in_houses", []):
                st.markdown(f"- {interp}")

        with aspects_tab:
            for interp in st.session_state.interpretations.get("aspects", []):
                st.markdown(f"- {interp}")
        
        with house_cusps_tab:
            for interp in st.session_state.interpretations.get("house_cusps", []):
                st.markdown(f"- {interp}")
    elif st.session_state.interpretations and st.session_state.interpretations.get("error"):
        st.warning(f"Could not generate full interpretations: {st.session_state.interpretations.get('error')}")

    # Section 4: Q&A with AI Agent
    if st.session_state.qa_agent:
        st.subheader("Ask the AI Astrologer")
        
        # Display Q&A history
        for i, entry in enumerate(st.session_state.qna_history):
            st.markdown(f"**You:** {entry['question']}")
            st.markdown(f"**AI Astrologer:** {entry['answer']}")
            st.markdown("---")

        user_question = st.text_input("Ask a question about your chart:", key="user_qna_input")
        if st.button("Ask", key="ask_button") and user_question:
            with st.spinner("Thinking..."):
                answer = st.session_state.qa_agent.answer_question(user_question)
                st.session_state.qna_history.append({"question": user_question, "answer": answer})
                # Rerun to update the display of Q&A history immediately
                st.rerun()
    
st.sidebar.markdown("---")
st.sidebar.markdown("**Disclaimer:** This AI Astrologer is for entertainment and informational purposes only. Astrological interpretations are subjective and should not be taken as absolute truth or professional advice (e.g., medical, financial, legal).")


