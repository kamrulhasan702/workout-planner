class Workout:
    def __init__(self, workout_id, name, category, duration, difficulty, calories, day, completed=False):
        self.workout_id = workout_id
        self.name = name
        self.category = category
        self.duration = duration
        self.difficulty = difficulty
        self.calories = calories
        self.day = day
        self.completed = completed

    def to_dict(self):
        return {
            "workout_id": self.workout_id,
            "name": self.name,
            "category": self.category,
            "duration": self.duration,
            "difficulty": self.difficulty,
            "calories": self.calories,
            "day": self.day,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Workout(
            data["workout_id"],
            data["name"],
            data["category"],
            data["duration"],
            data["difficulty"],
            data["calories"],
            data["day"],
            data.get("completed", False)
        )