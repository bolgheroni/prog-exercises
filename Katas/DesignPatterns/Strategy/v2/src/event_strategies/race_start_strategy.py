from src.event import Event
from src.states.participant_state import ParticipantState


class RaceStartStrategy:
    def start(self, event: Event):
        for participant in event.participants:
            participant.set_state(ParticipantState(0))
        event.started = True
