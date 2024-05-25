from transport import TruckTransport, ShipTransport
from abc import ABC, abstractmethod
import constants

class TrasportFactory(ABC):
    @abstractmethod
    def create_transport(self, id: int):
        pass


class TruckTransportFactory(TrasportFactory):
    def create_transport(self, id: int):
        distance_km = int(input("Enter the distance in km: "))
        return TruckTransport(
            distance_km=distance_km,
            id=id
        )
    

class ShipTransportFactory(TrasportFactory):
    def create_transport(self, id: int):
        distance_km = int(input("Enter the distance in km: "))
        crew_amount = int(input("Enter the number of crew members: "))
        return ShipTransport(
            distance_km=distance_km,
            id=id,
            crew_amount=crew_amount
        )

def create_transport(transport_code: int, id: int):
    if transport_code == constants.TRUCK_CODE:
        return TruckTransportFactory().create_transport(id)
    if transport_code == constants.SHIP_CODE:
        return ShipTransportFactory().create_transport(id)
    raise ValueError("Invalid transport code.")
        