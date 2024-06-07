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

    def add_participant(self, name, age):
        self.participants.append((name, age))

    def current_state(self) -> EventState:
        return EventState(
            participants=self._participants_description(),
            status=self._status_description(),
            ticks=self.ticks,
            winners=self._get_winners()
        )
    
    def start(self):
        for participant in self.participants:
            participant.set_state(ParticipantState(0))
        self.started = True

    def tick(self):
        self.ticks += 1
        for participant in self.participants:
            participant.act()

        if self._check_finish():
            self._finish()

    def _check_finish(self):
        return self._get_winners() != None
    
    def _finish(self):
        self.started = False
        self.finished = True

    def _get_winners(self):
        winners = [participant for participant in self.participants if participant.state.position >= self.distance]

        if len(winners) == 0:
            return None
        
        return winners

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