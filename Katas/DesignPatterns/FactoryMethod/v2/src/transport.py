from abc import ABC, abstractmethod
from v2.src.eta import ETA

class Transport(ABC):
    def __init__(self, type: str, id: int):
        self.type = type
        self.id = id
        self._is_deployed = False

    def deploy(self):
        self._is_deployed = True

    def is_deployed(self):
        return self._is_deployed
        
    def __str__(self):
        eta_text = self.eta()
        return f"{self.type} - {self.id}. ETA: {eta_text.hours}h{eta_text.minutes}m."
    
    @abstractmethod
    def eta(self)->ETA:
        pass
