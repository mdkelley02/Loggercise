from app.models.workout import Workout
from app.extensions.extensions import db

class WorkoutService:
    @staticmethod
    def create_workout(**workout_data):
        try:
            workout = Workout(**workout_data)
            workout = workout.save()
            return workout
        except Exception as e:
            return e

    @staticmethod
    def get_workout_by_id(workout_id):
        try:
            workout = Workout.query.filter_by(workout_id=workout_id).first()
            if not workout:
                return None
            return workout
        except Exception as e:
            return e

    @staticmethod
    def add_exercise_to_workout(workout_id, **exercise_data):
        try:
            workout = WorkoutService.get_workout_by_id(workout_id)
            workout.create_and_add_exercise(**exercise_data)
            return workout
        except Exception as e:
            return e

    @staticmethod
    def get_all_workouts():
        try:
            workouts = Workout.query.all()
            return workouts
        except Exception as e:
            return e

    @staticmethod
    def get_all_workouts_by_user_id(user_id):
        try:
            workouts = Workout.query.filter_by(user_id=user_id).all()
            return workouts
        except Exception as e:
            return e


