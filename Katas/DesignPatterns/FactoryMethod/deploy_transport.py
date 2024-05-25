from transport import Transport
from list_transports import list_transports
from typing import List

def deploy_transport(transports_list: List[Transport]): 
    transport = None
    while transport == None:
        list_transports(transports_list)
        selected_transport_id = int(input("Enter transport id to deploy: "))
        transport = next((t for t in transports_list if t.id == selected_transport_id), None)
        if transport == None:
            print("Invalid transport id. Try again.")

    transport.deploy()