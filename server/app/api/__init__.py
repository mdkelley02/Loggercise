from flask_restx import Api
from flask import Blueprint

# Namespaces
from .workouts.controller import api as workouts_ns
from .exercises.controller import api as exercises_ns
from .users.controller import api as users_ns

api_bp = Blueprint('api', __name__)

api = Api(api_bp, title="Loggercise API", description="Loggercise core routes")


# Add namespaces to Api
api.add_namespace(workouts_ns)
api.add_namespace(exercises_ns)
api.add_namespace(users_ns)