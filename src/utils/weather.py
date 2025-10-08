import requests
from src.utils.logger import get_logger

logger = get_logger(__name__)

def get_weather_info(city: str) -> str:
    """Get current weather information for a city"""
    try:
        # Using free OpenWeatherMap API (requires API key)
        # For demo purposes, using a free weather service
        url = f"http://wttr.in/{city}?format=3"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            weather_info = response.text.strip()
            logger.info(f"Weather info retrieved for {city}")
            return weather_info
        else:
            logger.warning(f"Could not fetch weather for {city}")
            return f"Weather information unavailable for {city}"
            
    except Exception as e:
        logger.error(f"Error fetching weather: {e}")
        return "Weather information currently unavailable"

def get_weather_recommendations(city: str) -> str:
    """Get weather-based activity recommendations"""
    try:
        weather = get_weather_info(city)
        
        # Simple weather-based recommendations
        if "rain" in weather.lower() or "shower" in weather.lower():
            return "Consider indoor activities like museums, galleries, or shopping centers due to rainy weather."
        elif "snow" in weather.lower():
            return "Perfect weather for winter activities! Consider ice skating, winter markets, or cozy cafes."
        elif "sunny" in weather.lower() or "clear" in weather.lower():
            return "Great weather for outdoor activities! Perfect for parks, walking tours, and outdoor dining."
        else:
            return "Check the weather and dress appropriately for outdoor activities."
            
    except Exception as e:
        logger.error(f"Error getting weather recommendations: {e}")
        return "Consider checking local weather before your trip."