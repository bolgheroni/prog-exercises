from typing import List
from src.participant import Participant
from src.event_state import EventState


class Event():
    def __init__(self,
            start_strategy,
            finish_strategy,
            winner_strategy,
            participants: List[Participant] | None = None,
        ):
        self.participants = participants or list()
        self.started = False
        self.ticks = 0
        self.finished = False
        self.start_strategy = start_strategy
        self.finish_strategy = finish_strategy
        self.winner_strategy = winner_strategy

    def add_participant(self, name, age):
        self.participants.append((name, age))

    def current_state(self) -> EventState:
        return EventState(
            participants=self._participants_description(),
            status=self._status_description(),
            ticks=self.ticks,
            winners=self.get_winners()
        )

    def tick(self):
        if self.finished:
            raise Exception('Cannot tick a finished event')

        if not self.started:
            raise Exception('Cannot tick a non-started event')

        for participant in self.participants:
            participant.act()

        self.ticks += 1

        if self.check_finish():
            self._finish()

    def _finish(self):
        self.started = False
        self.finished = True

    def _participants_description(self):
        if len(self.participants) == 0:
            return 'No participants'
        return '\n'.join([f'{participant})' for participant in self.participants])

    def _status_description(self):
        if self.finished:
            return 'Finished'

        if self.started:
            return 'In progress'

        return 'Not started'

    def check_finish(self):
        return self.finish_strategy.check_finish(self)

    def get_winners(self):
        return self.winner_strategy.get_winners(self)

    def start(self):
        self.start_strategy.start(self)
