from transport import Transport
from typing import List


def list_transports(transports_list: List[Transport]):
    print("List of transports \n")
    if len(transports_list) == 0:
        print("No transports available.")
    for transport in transports_list:
        print(transport)
    input("Press enter to continue...")