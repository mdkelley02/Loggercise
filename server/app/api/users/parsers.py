from flask_restx import reqparse

def create_user_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True)
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('first_name', type=str, required=True)
    parser.add_argument('last_name', type=str, required=True)
    parser.add_argument('current_weight', type=str, required=True)
    parser.add_argument('height', type=str, required=True)
    return parser

def update_user_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=False)
    parser.add_argument('email', type=str, required=False)
    parser.add_argument('first_name', type=str, required=False)
    parser.add_argument('last_name', type=str, required=False)
    parser.add_argument('current_weight', type=str, required=False)
    parser.add_argument('height', type=str, required=False)
    return parser