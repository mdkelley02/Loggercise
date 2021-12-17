from app.extensions.extensions import db, ma

class Set(db.Model):
    __tablename__ = 'sets'
    set_id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    rpe = db.Column(db.Integer)
    notes = db.Column(db.String(255))

class SetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Set



