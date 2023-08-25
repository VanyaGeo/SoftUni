class ExercisePlan:
    id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.id

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        duration_minutes = hours * 60
        return cls(trainer_id, equipment_id, duration_minutes)

    @staticmethod
    def get_next_id():
        ExercisePlan.id += 1
        return ExercisePlan.id - 1

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
