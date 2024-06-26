from src.transport import Transport
from src.eta import ETA
import math

class TruckTransport(Transport):
    _SPEED_KM_H = 50.0
    def __init__(self, id: int, distance_km: int):
        super().__init__(type="TRUCK", id=id, distance_km=distance_km)
    
    def eta(self):        
        travel_time_mins = 60 * self._distance_km / self._SPEED_KM_H
        return ETA(
            hours=math.floor(travel_time_mins // 60),
            minutes=math.floor(travel_time_mins % 60)
        )

    def __str__(self):
        base_description = super().__str__()
        return f"{base_description}."