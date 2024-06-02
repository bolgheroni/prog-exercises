from participant_state import ParticipantState


class Participant:
    def __init__(self, name, action_strategy):
        self.name = name
        self.action_strategy = action_strategy
        self.current_state = ParticipantState(0, 0)

    def __str__(self):
        return f'{self.name} at state: {str(self.current_state)}'

    def set_initial_state(self, initial_state: ParticipantState):
        self.current_state = initial_state

    def do_action(self):
        return self.action_strategy.do_action(self)

    def is_competing(self) -> bool:
        return self.action_strategy.is_competing(self)
