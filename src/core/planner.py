from langchain_core.messages import HumanMessage,AIMessage
from src.chains.itinerary_chain import generate_itineary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger=get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages=[]
        self.city=""
        self.interests=[]
        self.itinerary=""

        logger.info("TravelPlanner initialized")

    def set_city(self,city:str):
        try:
            self.city=city
            self.messages.append(HumanMessage(content=city))
            logger.info("City set successfuly")
        except Exception as e:
            logger.error(f"Error setting city: {e}")
            raise CustomException("Error setting city: e")
        
    def set_interests(self, interests_str:str):
        try:
            self.interests=[i.strip() for i in interests_str.split(",")]
            self.messages.append(HumanMessage(content=interests_str))
            logger.info("Interests set successfuly")
        except Exception as e:
            logger.error(f"Error setting interests: {e}")
            raise CustomException("Error setting interests: e")
        
    def create_itinerary(self):
        try:
            logger.info(f"Generating itinerary for {self.city} with interests: {self.interests}")
            itineary=generate_itineary(self.city, self.interests)
            self.itineary=itineary
            self.messages.append(AIMessage(content=itineary))
            logger.info("Itinerary generated successfuly")
            return itineary

        except Exception as e:
            logger.error(f"Error generating itinerary: {e}")
            raise CustomException("Error generating itinerary: e")
            