from flask_restx import reqparse

def create_set_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('notes', type=str, required=False)
    parser.add_argument('reps', type=int, required=True)
    parser.add_argument('weight', type=int, required=True)
    parser.add_argument('rpe', type=int, required=True)
    parser.add_argument('lift_type_id', type=int, required=True)
    parser.add_argument('set_number', type=int, required=True)
    return parser