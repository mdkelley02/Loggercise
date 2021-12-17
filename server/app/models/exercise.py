from app.extensions.extensions import db, ma

class Set(db.Model):
    """Set Model"""
    __tablename__ = 'sets'
    set_id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    rpe = db.Column(db.Integer)
    notes = db.Column(db.String(255))
    set_number = db.Column(db.Integer)

def save(self):
    """Save a set to the database"""
    db.session.add(self)
    db.session.commit()

class SetSchema(ma.SQLAlchemyAutoSchema):
    rpe = ma.Integer(required=True, validate=lambda x: x >= 0 and x <= 10)
    weight = ma.Integer(required=True, validate=lambda x: x >= 0 and x <= 1000)
    reps = ma.Integer(required=True, validate=lambda x: x >= 0 and x <= 1000)
    notes = ma.String(required=False)
    class Meta:
        model = Set


exercises_sets = db.Table(
    'exercises_sets',
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercises.exercise_id'), nullable=False),
    db.Column('set_id', db.Integer, db.ForeignKey('sets.set_id'), nullable=False)
)

class Exercise(db.Model):
    """Exercise Model"""
    __tablename__ = 'exercises'
    exercise_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    sets = db.relationship('Set', secondary=exercises_sets, backref=db.backref('exercises', lazy='dynamic'))


    def __init__(self, data):
        for key, value in data.items():
            setattr(self, key, value)

    def get_number_of_sets(self):
        return len(self.sets)

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        db.session.commit()
        return self

    def get_dict(self):
        return ExerciseSchema().dump(self)

    def create_and_add_set(self, **set_data):
        new_set = Set(**set_data)
        exercise = self.sets.append(new_set).save()
        return exercise

class ExerciseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Exercise

        