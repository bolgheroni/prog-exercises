class ParticipantState:
    def __init__(self, position: int, speed: float, last_state=None):
        self.position = position
        self.speed = speed
        self.last_state = last_state

   