from typing import List
from src.participant import Participant
from src.participant_state import ParticipantState
from src.event_state import EventState

class Marathon:
    def __init__(self, participants: List[Participant]| None = None):
        self.participants = participants or list()
        self.started = False
        self.ticks = 0
        self.distance = 40000
        self.finished = False
        self.winners = None

    def add_participant(self, name, age):
        self.participants.append((name, age))

    def current_state(self) -> EventState:
        return EventState(
            participants=self._participants_description(),
            status=self._status_description(),
            ticks=self.ticks,
            winners=self.winners
        )
    
    def start(self):
        for participant in self.participants:
            participant.set_state(ParticipantState(0))
        self.started = True

    def tick(self):
        self.ticks += 1
        for participant in self.participants:
            participant.act()

        if self.check_finish():
            self.finish()

    def check_finish(self):
        return all([participant.state.position >= self.distance for participant in self.participants])
    
    def finish(self):
        self.started = False
        self.finished = True
        self.winners = [participant for participant in self.participants if participant.state.position >= self.distance]

    def _status_description(self):
        if self.finished:
            return 'Finished'

        if self.started:
            return 'In progress'

        return 'Not started'        

    def _participants_description(self):
        if len(self.participants) == 0:
            return 'No participants'
        return '\n'.join([f'{participant})' for participant in self.participants])