from transport import Transport

def add_transport(transports_list: list):
    print("     Add new transport \n")
    distance_km = float(input("     Enter distance in km: "))
    print("     Select a transport type: \n")
    print("     1. Truck")
    # print("     2. Ship")

    transport_type = input("     Choose a transport type: ")
    createdTransport = Transport(
        type=transport_type,
        capacity=50,
        speed_km_h=100,
        distance_km=distance_km
    )
    transports_list.append(createdTransport)
