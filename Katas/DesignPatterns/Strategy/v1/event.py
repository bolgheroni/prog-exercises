from typing import List
from participant import Participant


class Event:
    def __init__(self, name, event_strategy, max_ticks=1000, participants: List[Participant] = []):
        self.name = name
        self.current_tick = 0
        self.max_ticks = max_ticks
        self.event_strategy = event_strategy
        self.is_finished = False
        self.participants = participants

    def finish(self):
        self.is_finished = True

    def run(self):
        self.event_strategy.start(self)
        while not self.is_finished and self.current_tick < self.max_ticks:
            self.event_strategy.do_tick(self)
            self.current_tick += 1
