import streamlit as st
from src.core.planner import TravelPlanner
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(page_title="Travel Planner", page_icon="🗺")

# Custom CSS for black labels
st.markdown("""
<style>
/* Change text color of input labels */
div.stTextInput > label, div.stTextInput > label > span {
    color: black;
    font-weight: bold;  /* optional: make it bold */
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# Add custom background image
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
background-size: cover;
background-position: center;
}
[data-testid="stHeader"] {visibility: hidden;}
[data-testid="stToolbar"] {visibility: hidden;}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Hero section
st.markdown(
    """
    <div style="text-align:center; padding: 30px; color: white; background-color: rgba(0,0,0,0.4); border-radius: 10px;">
        <h1 style="font-size:50px;">🗺 Travel Planner</h1>
        <p style="font-size:20px;">Plan your perfect day trip itinerary. Enter your city and interests, and we'll create a personalized plan for you!</p>
    </div>
    """, unsafe_allow_html=True
)

st.write("")  # spacing

# Input form with icons and placeholders
with st.form("planner_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        city = st.text_input(
            "🏙 City",
            placeholder="e.g., Paris",
            help="Enter the city you want to visit"
        )
    with col2:
        interests = st.text_input(
            "🎯 Interests",
            placeholder="e.g., museums, food, parks",
            help="Enter your interests separated by commas"
        )
    
    submitted = st.form_submit_button("✨ Generate Itinerary")

# Process form submission
if submitted:
    if city and interests:
        planner = TravelPlanner()
        planner.set_city(city)
        planner.set_interests(interests)
        itinerary = planner.create_itineary()
        
        st.markdown(f"""
                <div style="
                     background-color: rgba(0, 0, 0, 0.6);  /* semi-transparent black */
                     padding: 20px; 
                     border-radius: 15px; 
                     margin-top: 20px;
                ">
                    <h2 style="color: white;">📝 Your Itinerary for {city}</h2>
                    <p style="font-size:18px; color: white;">{itinerary}</p>
                </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter both city and interests")
