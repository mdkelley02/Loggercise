from app.static_data.lift_types import lift_types
from app.static_data.muscle_groups import muscle_groups
from app.models.muscle_group import MuscleGroup

def get_static_data():
    return {
        "lifts": lift_types,
        "muscle_groups": muscle_groups
    }

def insert_initial_data(db):
    for muscle_group_name in muscle_groups:
        db.session.add(MuscleGroup(name=muscle_group_name))
    db.session.commit()
