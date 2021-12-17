from flask_restx import Resource
from .service import WorkoutService
from .parsers import create_exercise_parser, create_workout_parser
from . import api
from app.api.common.response import create_response

@api.route("/<int:workout_id>")
class WorkoutsGet(Resource):
    """Get a specifc workout by workout_id\n
    returns workout
    """
    def get(self, workout_id):
        print(workout_id)
        workout = WorkoutService.get_workout_by_id(workout_id)
        if not workout:
            return create_response(code=200, message="Workout not found")
        else:
            return create_response(code=200, data=workout.to_dict())

@api.route("")
class WorkoutsPost(Resource):
    """Create a workout\n 
    returns new workout."""
    def post(self):
        request_args = create_workout_parser().parse_args()
        workout = WorkoutService.create_workout(**request_args).to_dict()
        return create_response(code=201, data=workout)

@api.route("/<int:workout_id>/exercises")
class WorkoutsExercisesPost(Resource):
    """Create and add an exercise to a specific workout by workout_id\n
        returns the workout with the added exercise."""
    def post(self, workout_id):
        request_args = create_exercise_parser().parse_args()
        return WorkoutService.add_exercise_to_workout(workout_id, **request_args)

# get every workout
@api.route("/all")
class WorkoutsGetAll(Resource):
    """Get all workouts\n
    returns workouts"""
    def get(self):
        workouts = WorkoutService.get_all_workouts()
        if not workouts:
            return create_response(code=200, message="No workouts found")
        else:
            return create_response(code=200, data=workouts)



