import json
import os
from workout import Workout
 
class Storage:
    def __init__(self, filename="workouts.json"):
        self.filename = filename
 
    def save_data(self, workouts):
        data = [workout.to_dict() for workout in workouts]
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
 
    def load_data(self):
        if not os.path.exists(self.filename):
            return []
 
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Workout.from_dict(item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []