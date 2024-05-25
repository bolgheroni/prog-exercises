from transport import Transport
from typing import List
from transport_factory import create_transport

def add_transport(transports_list: List[Transport]):
    print("Add new transport \n")
    print("Select a transport type: \n")
    print("1. Truck")
    print("2. Ship")
    transport_code = input("Choose a transport type: ")
    
    createdTransport = create_transport(
        transport_code=int(transport_code),
        id=len(transports_list) + 1
    )
    transports_list.append(createdTransport)
