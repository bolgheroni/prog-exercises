from abc import ABC, abstractmethod
from event import Event
from participant import Participant
from participant_state import ParticipantState

class EventStrategy(ABC):
    def start(self, event: Event):
        for participant in event.participants:
            participant.set_initial_state(
                self.get_participant_initial_state(participant)
            )

    def do_tick(self, event: Event):
        print(f'Tick {event.current_tick} of {event.name}')
        for participant in event.participants:
            participant.do_action()
        
        event_ended = self.check_end(event)
        if event_ended:
            event.finish()
            self.display_final_results(event)
        else:
            self.display_current_state(event)
            print('')

    @abstractmethod
    def check_end(self, event: Event) -> bool:
        pass

    @abstractmethod
    def get_participant_initial_state(self, participant: Participant) -> ParticipantState:
        pass

    @abstractmethod
    def display_current_state(self, event: Event):
        pass

    @abstractmethod
    def display_final_results(self, event: Event):
        pass

    