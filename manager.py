class WorkoutManager:
    def __init__(self, storage):
        self.storage = storage
        self.workouts = self.storage.load_data()

    def add_workout(self, workout):
        self.workouts.append(workout)
        self.storage.save_data(self.workouts)

    def get_all_workouts(self):
        return self.workouts

    def find_workout_by_id(self, workout_id):
        for workout in self.workouts:
            if workout.workout_id == workout_id:
                return workout
        return None

    def update_workout(self, workout_id, name, category, duration, difficulty, calories, day):
        workout = self.find_workout_by_id(workout_id)
        if workout:
            workout.name = name
            workout.category = category
            workout.duration = duration
            workout.difficulty = difficulty
            workout.calories = calories
            workout.day = day
            self.storage.save_data(self.workouts)
            return True
        return False

    def delete_workout(self, workout_id):
        workout = self.find_workout_by_id(workout_id)
        if workout:
            self.workouts.remove(workout)
            self.storage.save_data(self.workouts)
            return True
        return False

    def search_workouts(self, keyword):
        keyword = keyword.lower()
        results = []
        for workout in self.workouts:
            if (
                keyword in workout.name.lower()
                or keyword in workout.category.lower()
                or keyword in workout.day.lower()
                or keyword in workout.difficulty.lower()
            ):
                results.append(workout)
        return results

    def mark_completed(self, workout_id):
        workout = self.find_workout_by_id(workout_id)
        if workout:
            workout.completed = True
            self.storage.save_data(self.workouts)
            return True
        return False

    def generate_report(self):
        total_workouts = len(self.workouts)
        completed = sum(1 for w in self.workouts if w.completed)
        pending = total_workouts - completed
        total_duration = sum(w.duration for w in self.workouts)
        average_duration = total_duration / total_workouts if total_workouts > 0 else 0
        total_calories = sum(w.calories for w in self.workouts)

        categories = {}
        for workout in self.workouts:
            categories[workout.category] = categories.get(workout.category, 0) + 1

        top_category = "N/A"
        if categories:
            top_category = max(categories, key=categories.get)

        return {
            "total_workouts": total_workouts,
            "completed": completed,
            "pending": pending,
            "total_duration": total_duration,
            "average_duration": average_duration,
            "total_calories": total_calories,
            "top_category": top_category
        }
