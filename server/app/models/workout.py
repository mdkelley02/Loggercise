from app.extensions.extensions import db, ma
from .exercise import Exercise
from datetime import datetime

workouts_exercises = db.Table(
    'workouts_exercises',
    db.Column('workout_id', db.Integer, db.ForeignKey('workouts.workout_id'), nullable=False),
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercises.exercise_id'), nullable=False)
)

class Workout(db.Model):
    __tablename__ = 'workouts'
    workout_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    duration = db.Column(db.Integer, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    exercises = db.relationship('Exercise', secondary=workouts_exercises, backref="workouts")

    def __init__(self, name, description=None, duration=None):
        self.name = name
        self.description = description
        self.duration = duration

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def add_exercise(self, exercise):
        self.exercises.append(exercise)
        db.session.commit()
        return self
    
    def __repr__(self):
        return f'<Workout {self.name}>'

    def get_exercises(self):
        return [exercise.get_dict() for exercise in self.exercises]

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        db.session.commit()
        return self

    def create_and_add_exercise(self, **exercise_data):
        exercise = Exercise(**exercise_data)
        self.add_exercise(exercise)
        self.save()
        return exercise

    def to_dict(self):
        return WorkoutSchema().dump(self)

class WorkoutSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Workout