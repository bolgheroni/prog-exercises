from src.participant_state import ParticipantState


class Participant:
    def __init__(self, name, age, state=None):
        self.name = name
        self.age = age
        self.state = ParticipantState(0) if state == None else state

    def set_state(self, state):
        self.state = state

    def __str__(self):
        return f'{self.name} ({self.age}) - {self.state}'
