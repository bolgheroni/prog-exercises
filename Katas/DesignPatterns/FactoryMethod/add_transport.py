from transport import Transport
from typing import List

def add_transport(transports_list: List[Transport]):
    print("Add new transport \n")
    distance_km = float(input("Enter distance in km: "))
    print("Select a transport type: \n")
    print("1. Truck")
    # print("     2. Ship")

    transport_type = input("Choose a transport type: ")
    createdTransport = Transport(
        type="Truck",
        capacity=50,
        speed_km_h=100,
        distance_km=distance_km,
        id=len(transports_list) + 1
    )
    transports_list.append(createdTransport)
