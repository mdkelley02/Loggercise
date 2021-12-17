from app.models.exercise import Exercise

class ExercisesService:
    @staticmethod
    def get_exercise_by_id(exercise_id):
        """Gets specified exercise"""
        try:
            return Exercise.query.filter_by(exercise_id=exercise_id).first()
        except Exception as e:
            return e
        

    @staticmethod
    def create_and_add_set_to_exercise(exercise_id, **set_data):
        """creates and adds set to specified exercise\n
            returns updated exercise.
        """
        try:
            exercise = ExercisesService.get_exercise(exercise_id)
            if exercise is None:
                raise Exception("Exercise not found")
            exercise.create_and_add_set(**set_data)
            return exercise
        except Exception as e:
            return e
