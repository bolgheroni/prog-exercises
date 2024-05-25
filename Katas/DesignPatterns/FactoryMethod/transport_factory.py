from transport import TruckTransport, ShipTransport
import constants

def create_transport(transport_code: int, distance_km: float, id: int):
    if transport_code == constants.TRUCK_CODE:
        return TruckTransport(distance_km, id)
    if transport_code == constants.SHIP_CODE:
        return ShipTransport(distance_km, id)
    raise ValueError("Invalid transport code.")
        