from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY
from src.utils.weather import get_weather_info, get_weather_recommendations

llm=ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0.3,
)

itinerary_prompt=ChatPromptTemplate([
    ("system", """You are a helpful travel assistant. Create a {days}-day trip itinerary for {city} based on:
    - User interests: {interests}
    - Budget level: {budget}
    - Current weather: {weather}
    - Weather recommendations: {weather_rec}
    
    Format the response as:
    **Day X: [Theme/Focus]**
    - Morning: [Activity with time and brief description]
    - Afternoon: [Activity with time and brief description] 
    - Evening: [Activity with time and brief description]
    
    Include budget-appropriate suggestions and weather-suitable activities. Add practical tips."""),
    ("human", "Create an itinerary for my trip")
])

def generate_itineary(city: str, interests: list[str], days: int = 1, budget: str = "medium") -> str:
    weather = get_weather_info(city)
    weather_rec = get_weather_recommendations(city)
    
    response = llm.invoke(
        itinerary_prompt.format_messages(
            city=city, 
            interests=', '.join(interests),
            days=days,
            budget=budget,
            weather=weather,
            weather_rec=weather_rec
        )
    )
    return response.content













    