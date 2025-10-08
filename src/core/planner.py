from langchain_core.messages import HumanMessage,AIMessage
from src.chains.itinerary_chain import generate_itineary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages=[]
        self.city=""
        self.interests=[]
        self.days=1
        self.budget="medium"
        self.itineary=""

        logger.info("Initialized TravelPlanner instance")

    def set_city(self,city:str):
        try:
            self.city = city
            self.messages.append(HumanMessage(content=city))
            logger.info("City set successfully")
        except Exception as e:
            logger.error(f"error while setting city : {e}")
            raise CustomException("Failed to set city" , e)
        
    def set_interests(self,interests_str:str):
        try:
            self.interests = [i.strip() for i in interests_str.split(",")]
            self.messages.append(HumanMessage(content=interests_str))
            logger.info("Interest also set successfully..")
        except Exception as e:
            logger.error(f"error while setting interests : {e}")
            raise CustomException("Failed to set interest" , e)
    
    def set_days(self, days: int):
        try:
            self.days = days
            logger.info(f"Days set to {days}")
        except Exception as e:
            logger.error(f"error while setting days : {e}")
            raise CustomException("Failed to set days" , e)
    
    def set_budget(self, budget: str):
        try:
            self.budget = budget
            logger.info(f"Budget set to {budget}")
        except Exception as e:
            logger.error(f"error while setting budget : {e}")
            raise CustomException("Failed to set budget" , e)
        
    def create_itineary(self):
        try:
            logger.info(f"Generating itinerary for {self.city} for {self.days} days with {self.budget} budget and interests: {self.interests}")
            itineary = generate_itineary(self.city, self.interests, self.days, self.budget)
            self.itineary = itineary
            self.messages.append(AIMessage(content=itineary))
            logger.info("Itinerary generated successfully..")
            return itineary
        except Exception as e:
            logger.error(f"error while creating itinerary : {e}")
            raise CustomException("Failed to create itinerary" , e)