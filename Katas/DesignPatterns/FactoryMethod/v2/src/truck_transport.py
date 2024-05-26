from v2.src.transport import Transport
from v2.src.eta import ETA

class TruckTransport(Transport):
    def __init__(self, id: int, distance_km: int):
        super().__init__(type="TRUCK", id=id)
        self._distance_km = distance_km
    
    def eta(self):
        return ETA(hours=2, minutes=12)

    def __str__(self):
        base_description = super().__str__()
        distance_km_text = f"Distance (km): {self._distance_km}." 
        eta = self.eta()
        eta_text = f"ETA: {eta.hours}h{eta.minutes}m."
        return f"{base_description}. {distance_km_text} {eta_text}"