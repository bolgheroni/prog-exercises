from v2.src.truck_transport import TruckTransport
from v2.src.ship_transport import ShipTransport

class TransportFactory:
    def __init__(self, input_collector):
        self.input_collector = input_collector

    def create_transport(self, id: int, type: str):
        if type == "TRUCK":
            return self._create_truck(id)
        if type == "SHIP":
            return self._create_ship(id)
        
        raise ValueError("Invalid transport type.")
    
    def _create_truck(self, id: int):
        distance = self.input_collector.collect_distance()
        return TruckTransport(
            type="TRUCK",
            id=id,
            distance=distance
        )
    
    def _create_ship(self, id: int):
        crew_amount = self.input_collector.collect_crew_amount()
        return ShipTransport(
            type="SHIP",
            id=id,
            crew_amount=crew_amount
        )