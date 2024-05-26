from src.truck_transport import TruckTransport
from src.ship_transport import ShipTransport

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
        distance_km = self.input_collector.collect_distance()
        return TruckTransport(
            id=id,
            distance_km=distance_km
        )
    
    def _create_ship(self, id: int):
        crew_amount = self.input_collector.collect_crew_amount()
        distance_km = self.input_collector.collect_distance()
        return ShipTransport(
            id=id,
            crew_amount=crew_amount,
            distance_km=distance_km
        )