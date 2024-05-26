from abc import ABC, abstractmethod
from v2.src.eta import ETA

class Transport(ABC):
    def __init__(self, type: str, id: int, distance_km: int):
        self.type = type
        self.id = id
        self._is_deployed = False
        self._distance_km = distance_km

    def deploy(self):
        self._is_deployed = True

    def is_deployed(self):
        return self._is_deployed
        
    def __str__(self):
        identity_text = f"{self.type} - {self.id}."
        eta = self.eta()
        eta_text= f"ETA: {eta.hours}h{eta.minutes}m."
        distance_km_text = f"Distance (km):{self._distance_km}."
        
        return f"{identity_text} {distance_km_text} {eta_text}"
    
    @abstractmethod
    def eta(self)->ETA:
        pass
