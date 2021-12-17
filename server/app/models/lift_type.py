from app.extensions.extensions import db, ma


lift_types_muscle_groups = db.Table(
    'lift_types_muscle_groups',
    db.Column('lift_type_id', db.Integer, db.ForeignKey('lift_types.lift_type_id')),
    db.Column('muscle_group_id', db.Integer, db.ForeignKey('muscle_groups.muscle_group_id'))
)

class LiftType(db.Model):
    __tablename__ = 'lift_types'
    lift_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    muscle_groups = db.relationship('MuscleGroup', secondary='lift_type_muscle_groups', backref=db.backref('lift_types', lazy='dynamic'))

class LiftTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LiftType