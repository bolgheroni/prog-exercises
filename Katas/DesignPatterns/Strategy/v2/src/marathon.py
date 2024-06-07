from typing import List
from src.participant import Participant
from src.event_state import EventState

class Marathon:
    def __init__(self, participants: List[Participant]| None = None):
        self.participants = participants or list()
        self.started = False

    def add_participant(self, name, age):
        self.participants.append((name, age))

    def current_state(self) -> EventState:
        return EventState(
            participants=self._participants_description(),
            status=self._status_description()
        )
    
    def start(self):
        self.started = True

    def _status_description(self):
        return 'In progress' if self.started else 'Not started'

    def _participants_description(self):
        if len(self.participants) == 0:
            return 'No participants'
        return '\n'.join([f'{participant})' for participant in self.participants])