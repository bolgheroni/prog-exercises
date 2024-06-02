from action_strategy import ActionStrategy
from participant import Participant
import random

class MarathonCompetitorStrategy(ActionStrategy):
    def do_action(self, participant: Participant):
        participant.current_state.position += participant.current_state.speed
        if participant.current_state.position >= 42:
            participant.current_state.speed = 1
        else:
            random_number = random.randint(2, 3)
            participant.current_state.speed = random_number

    def is_competing(self, participant: Participant) -> bool:
        return True
    