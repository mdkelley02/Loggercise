from flask_restx import reqparse

def create_workout_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True)
    parser.add_argument('description', type=str, required=False)
    parser.add_argument('duration', type=int, required=False)
    return parser

def create_exercise_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True)
    parser.add_argument('description', type=str, required=False)
    return parser
