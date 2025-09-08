from datetime import datetime
from zoneinfo import ZoneInfo
import threading
def current_time()->dict:
    '''
    returns the current time in dict {day: "year/month/day" , minute: "year/month/day/hour/minute"} in PT time zone ; google use PT time zone for counting the calls for the models apis
    '''
    pt_time = datetime.now(ZoneInfo("America/Los_Angeles"))

    return {
        "day": pt_time.strftime("%Y/%m/%d"),
        "minute": pt_time.strftime("%Y/%m/%d/%H/%M")
    }


class ModelsManager:
    def __init__(self):
        self._lock = threading.Lock()
        current: dict = current_time()
        self.models: dict = {
            "gemini-2.5-pro": { # working only in thinkning mode add it later
                "day_limit": 25,
                "minute_limit": 5,
                "current_day": current['day'],
                "current_minute": current['minute'],
                "day_count": 0,
                "minute_count": 0
            },
            "gemini-2.5-flash": {
                "day_limit": 500,
                "minute_limit": 10,
                "current_day": current['day'],
                "current_minute": current['minute'],
                "day_count": 0,
                "minute_count": 0
            },
            "gemini-2.5-flash-lite": {
                "day_limit": 1000,
                "minute_limit": 30,
                "current_day": current['day'],
                "current_minute": current['minute'],
                "day_count": 0,
                "minute_count": 0
            },
            "gemini-2.0-flash": {
                "day_limit": 200,
                "minute_limit": 15,
                "current_day": current['day'],
                "current_minute": current['minute'],
                "day_count": 0,
                "minute_count": 0
            },
            "gemini-2.0-flash-lite": {
                "day_limit": 200,
                "minute_limit": 30,
                "current_day": current['day'],
                "current_minute": current['minute'],
                "day_count": 0,
                "minute_count": 0
            },
            "gemini-1.5-flash": {
                "day_limit": 50,
                "minute_limit": 15,
                "current_day": current['day'],
                "current_minute": current['minute'],
                "day_count": 0,
                "minute_count": 0
            }
        }
        # the rank is based on max usage per minute and day, and the 1.5 as fallback
        self.models_map_rank = [
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-2.0-flash-lite",

            "gemini-2.0-flash",
            #"gemini-2.5-pro",
            "gemini-1.5-flash"
        ]
        self.current_model: int = 0

    def _cleanup_counts(self, model_name: str):
        '''
        Cleanup the usage counts for the specified model if the day or minute has changed.
        '''
        current: dict = current_time()
        model = self.models.get(model_name)
        if model:
            if model['current_day'] != current['day']:
                model['current_day'] = current['day']
                model['day_count'] = 0
            if model['current_minute'] != current['minute']:
                model['current_minute'] = current['minute']
                model['minute_count'] = 0
    
    def check_models_availability(self, model_name:str) -> bool:
        '''
        Check the availability of a model based on their usage limits.
        '''
        model = self.models.get(model_name)
        self._cleanup_counts(model_name)
        print (f"Model {model_name} usage: day_count={model['day_count']}/{model['day_limit']}, minute_count={model['minute_count']}/{model['minute_limit']}")
        if model['day_count'] < model['day_limit'] and model['minute_count'] < model['minute_limit']:
            return True
        return False
    
    def switch_model(self):
        '''
        Switch to the highest available model in the rank list.
        '''
        available_model = None
        for idx, model_name in enumerate(self.models_map_rank):
            model = self.models.get(model_name)
            if model and self.check_models_availability(model_name):
                self.current_model = idx
                available_model = model_name
                print(f"Switched to model: {model_name}")
                return
        if not available_model:
            raise Exception("No available models at the moment. Please try again later.")
    def get_model(self) -> str:
        '''
        Get the current model based on availability.
        '''
        with self._lock:
            current_model = self.models_map_rank[self.current_model]
            if not self.check_models_availability(current_model):
                self.switch_model()
                current_model = self.models_map_rank[self.current_model]
            self.add_model_call(current_model)
            print(f"Using model: {current_model}")
            return current_model

    def add_model_call(self, model_name: str):
        '''
        Increment the usage counts for the specified model.
        '''

        model = self.models.get(model_name)
        if model:
            self._cleanup_counts(model_name)
            model['day_count'] += 1
            model['minute_count'] += 1
        print(f"Model {model_name} usage updated: day_count={model['day_count']}, minute_count={model['minute_count']}")


Models_manager = ModelsManager()