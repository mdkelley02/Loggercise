from app.extensions.extensions import db, ma

users_workouts = db.Table(
    'users_workouts',
    db.Column('user_id', db.Integer, db.ForeignKey('users.user_id')),
    db.Column('workout_id', db.Integer, db.ForeignKey('workouts.workout_id'))
)

users_user_defined_lift_types = db.Table(
    'users_custom_lifts',
    db.Column('user_id', db.Integer, db.ForeignKey('users.user_id')),
    db.Column('lift_type_id', db.Integer, db.ForeignKey('lift_types.lift_type_id'))
)

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    historic_weight = db.relationship('HistoricWeight', backref='user', lazy=True)
    height = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    workouts = db.relationship('Workout', backref='user', lazy=True)
    user_defined_lift_types = db.relationship('users_user_defined_lift_types', backref='user', lazy=True)
