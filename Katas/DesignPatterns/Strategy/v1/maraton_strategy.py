from participant import Participant
from participant_state import ParticipantState
from event import Event
from event_strategy import EventStrategy

class MarathonStrategy(EventStrategy):
    def __init__(self, distance: int):
        self.distance = distance
        
    def check_end(self, event: Event) -> bool:
        for participant in event.participants:
            if participant.is_competing() and participant.current_state.position >= self.distance:
                return True
        
        return False
    
    def get_participant_initial_state(self, participant: Participant) -> ParticipantState:
        if participant.is_competing():
            return ParticipantState(
                position=0,
                speed=1,
                last_state=None
            )
        else:
            return ParticipantState(
                position=10,
                speed=0,
                last_state=None
            )
        
    def display_current_state(self, event: Event):
        sorted_participants = sorted(event.participants, key=lambda x: x.current_state.position, reverse=True)
        for participant in sorted_participants:
            print(f'{participant.name} is at position {participant.current_state.position}')

    def display_final_results(self, event: Event):
        winners = []
        for participant in event.participants:
            if participant.is_competing() and  participant.current_state.position >= self.distance:
                winners.append(participant)
        
        if len(winners) == 0:
            print('No one finished the marathon')
        
        if len(winners) == 1:
            print(f'{winners[0].name} won the marathon')

        if len(winners) > 1:
            print('We have a tie!')
            for winner in winners:
                print(f'{winner.name} tied for first place')