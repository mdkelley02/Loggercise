from app.extensions.extensions import db, ma

class MuscleGroup(db.Model):
    __tablename__ = 'muscle_group'
    muscle_group_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __init__(self, name):
        self.name = name

    def update(self, name):
        self.name = name
        db.session.commit()
        return self

class MuscleGroupSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MuscleGroup