from abc import ABC, abstractmethod
from participant import Participant


class ActionStrategy(ABC):
    @abstractmethod
    def do_action(self, participant: Participant):
        pass

    @abstractmethod
    def is_competing(self, participant: Participant) -> bool:
        pass
