from src.event import Event


class RaceWinnersStrategy:
    def __init__(self, race_distance: int):
        self.race_distance = race_distance

    def get_winners(self, event: Event):
        winners = [
            participant for participant in event.participants if participant.state.position >= self.race_distance]
        return winners if len(winners) > 0 else None