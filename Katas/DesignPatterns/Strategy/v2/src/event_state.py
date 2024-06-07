class EventState:
    def __init__(self, participants, status, ticks, winners=None):
        self.participants = participants
        self.status = status
        self.ticks = ticks
        self.winners = winners