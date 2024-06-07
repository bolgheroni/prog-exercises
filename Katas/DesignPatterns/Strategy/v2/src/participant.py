from src.participant_state import ParticipantState
from src.constant_runner import ConstantRunner

class Participant:
    def __init__(self, name, age, state=None):
        self.name = name
        self.age = age
        self.state = ParticipantState(0) if state == None else state
        self.action_strategy = ConstantRunner(1)

    def set_state(self, state):
        self.state = state

    def act(self):
        self.action_strategy.act(self)

    def __str__(self):
        return f'{self.name} ({self.age}) - {self.state}'
