import streamlit as st
from src.core.planner import TravelPlanner
import os
from dotenv import load_dotenv
from src.utils.weather import get_weather_info

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(page_title="Travel Planner", page_icon="🗺")

# Custom CSS for white labels in form
st.markdown("""
<style>
/* Change text color of input labels to white */
div.stTextInput > label, div.stTextInput > label > span,
div.stSelectbox > label, div.stSelectbox > label > span,
div.stSlider > label, div.stSlider > label > span {
    color: white !important;
    font-weight: bold;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# Add custom background image
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://i.pinimg.com/originals/2e/38/06/2e38062cdfc83526ac2cd5257a933d16.gif");
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
        <p style="font-size:20px;">Plan your perfect multi-day trip itinerary with weather and budget considerations!</p>
    </div>
    """, unsafe_allow_html=True
)

st.write("")  # spacing

# Input form with enhanced features
st.markdown("""
<style>
.stForm {
    background-color: rgba(0, 0, 0, 0.7) !important;
    padding: 20px !important;
    border-radius: 15px !important;
    backdrop-filter: blur(10px) !important;
}
</style>
""", unsafe_allow_html=True)

with st.form("planner_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        city = st.text_input(
            "🏙 City",
            placeholder="e.g., Paris",
            help="Enter the city you want to visit"
        )
        days = st.slider(
            "📅 Number of Days",
            min_value=1,
            max_value=7,
            value=1,
            help="Select trip duration (1-7 days)"
        )
    
    with col2:
        interests = st.text_input(
            "🎯 Interests",
            placeholder="e.g., museums, food, parks",
            help="Enter your interests separated by commas"
        )
        budget = st.selectbox(
            "💰 Budget Level",
            options=["low", "medium", "high"],
            index=1,
            help="Select your budget preference"
        )
    
    # Weather preview
    if city:
        with st.expander("🌤 Current Weather Preview"):
            weather_info = get_weather_info(city)
            st.info(f"Weather in {city}: {weather_info}")
    
    submitted = st.form_submit_button("✨ Generate Itinerary")

# Process form submission
if submitted:
    if city and interests:
        with st.spinner("🔄 Creating your personalized itinerary..."):
            planner = TravelPlanner()
            planner.set_city(city)
            planner.set_interests(interests)
            planner.set_days(days)
            planner.set_budget(budget)
            itinerary = planner.create_itineary()
        
        # Display weather info
        weather_info = get_weather_info(city)
        
        st.markdown(f"""
                <div style="
                     background-color: rgba(0, 0, 0, 0.6);
                     padding: 20px; 
                     border-radius: 15px; 
                     margin-top: 20px;
                ">
                    <h2 style="color: white;">📝 Your {days}-Day Itinerary for {city}</h2>
                    <p style="color: #FFD700; font-size: 16px;">🌤 Current Weather: {weather_info}</p>
                    <p style="color: #90EE90; font-size: 16px;">💰 Budget Level: {budget.title()}</p>
                    <div style="font-size:16px; color: white; line-height: 1.6;">{itinerary}</div>
                </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter both city and interests")
