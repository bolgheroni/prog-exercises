from typing import List
from src.participant import Participant

class Marathon:
    def __init__(self, participants: List[Participant]| None = None):
        self.participants = participants or list()
        self.started = False

    def add_participant(self, name, age):
        self.participants.append((name, age))

    def current_state(self):
        state_description = self._status_description() + '\n'
        state_description += 'Participants:\n'
        if len(self.participants) == 0:
            state_description += 'No participants'
        else:
            state_description += self._participants_description()
        
        return state_description
    
    def start(self):
        self.started = True

    def _status_description(self):
        return 'Status: In progress' if self.started else 'Status: Not started'

    def _participants_description(self):
        return '\n'.join([f'{participant})' for participant in self.participants])