import streamlit as st
from src.core.planner import TravelPlanner
import os
from dotenv import load_dotenv

st.set_page_config(page_title="Travel Planner", page_icon="🗺")
st.title("Travel Planner")
st.write("Plan your day trip itineary by entering your city and interests")

load_dotenv()

with st.form("planner_form"):
    city=st.text_input("Enter your city name for your trip")
    interests=st.text_input("Enter your interests for your trip(comma-separted)")
    submitted=st.form_submit_button("Generate itineary")

    if submitted:
        if city and interests:
            planner=TravelPlanner()
            planner.set_city(city)
            planner.set_interests(interests)
            itineary=planner.create_itineary()
            
            st.subheader("Your Itineary")
            st.markdown(itineary)
        else:
            st.warning("Please enter both city and interests")