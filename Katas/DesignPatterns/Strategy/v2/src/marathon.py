from typing import List
from src.participant import Participant

class Marathon:
    def __init__(self, participants: List[Participant]| None = None):
        self.participants = participants or list()

    def add_participant(self, name, age):
        self.participants.append((name, age))

    def current_state(self):
        return '\n'.join([f'{participant}' for participant in self.participants])