from v2.src.transport import Transport

class TruckTransport(Transport):
    def __init__(self, type: str, id: int, distance: int):
        super().__init__(type, id)
        self.distance = distance

    def __str__(self):
        base_description = super().__str__()
        distance_text = f"Distance: {self.distance}." 
        return f"{base_description}. {distance_text}"