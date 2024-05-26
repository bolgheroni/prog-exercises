import math
from v2.src.transport import Transport 
from v2.src.eta import ETA
class ShipTransport(Transport):
    def __init__(self, id: int, distance_km: int, crew_amount: int):
        super().__init__(type="SHIP", id=id)
        self.crew_amount = crew_amount
        self.distance_km = distance_km

    def eta(self):
        _SPEED_KM_H = 27.0
        travel_time_mins = 60 * self.distance_km / _SPEED_KM_H
        return ETA(
            hours=math.floor(travel_time_mins // 60),
            minutes=math.floor(travel_time_mins % 60)
        )

    def __str__(self):
        base_description = super().__str__()
        crew_amount_text = f"Crew amount: {self.crew_amount}." 
        distance_km_text = f"Distance (km): {self.distance_km}."
        return f"{base_description}. {crew_amount_text} {distance_km_text}"