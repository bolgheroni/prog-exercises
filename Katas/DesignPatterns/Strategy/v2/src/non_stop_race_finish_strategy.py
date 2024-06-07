from src.event import Event

class NonStopRaceFinishStrategy:
    def check_finish(self, event: Event):
        return event.get_winners() != None