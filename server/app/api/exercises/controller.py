from . import api
from flask_restx import Resource
from .parsers import create_set_parser
from .service import ExercisesService

@api.route('/exercises/<int:exercise_id>/sets/')
class ExerciseSetsPost(Resource):
    def post(self, exercise_id):
        request_args = create_set_parser().parse_args()
        return ExercisesService.create_and_add_set_to_exercise(exercise_id, **request_args)

# endpoint to handle getting an exercise by an exercise id
@api.route('/exercises/<int:exercise_id>/')
class ExerciseGet(Resource):
    """Get an exercise by an exercise id\n
    returns exercise or none"""
    def get(self, exercise_id):
        return ExercisesService.get_exercise_by_id(exercise_id)