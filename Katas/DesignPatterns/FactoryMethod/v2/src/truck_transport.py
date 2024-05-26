from v2.src.transport import Transport

class TruckTransport(Transport):
    def __init__(self, id: int, distance_km: int):
        super().__init__(type="TRUCK", id=id)
        self.distance_km = distance_km

    def __str__(self):
        base_description = super().__str__()
        distance_km_text = f"Distance (km): {self.distance_km}." 
        return f"{base_description}. {distance_km_text}"