from typing import List
from src.participant import Participant
from src.event import Event
from src.event_strategies.non_stop_race_finish_strategy import NonStopRaceFinishStrategy
from src.event_strategies.race_start_strategy import RaceStartStrategy
from src.event_strategies.race_winners_strategy import RaceWinnersStrategy

def make_sprint_game(participants: List[Participant], distance: int):
    return Event(
        participants=participants,
        finish_strategy=NonStopRaceFinishStrategy(),
        start_strategy=RaceStartStrategy(),
        winner_strategy=RaceWinnersStrategy(distance)
    )