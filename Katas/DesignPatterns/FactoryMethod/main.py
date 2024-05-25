from transport import Transport
from add_transport import add_transport
from list_transports import list_transports
from typing import List

def main():
    action = ""
    transports_list: List[Transport] = []
    print("Factory Method Pattern \n")
    print("----------------------\n")
    while action != "4":
        print("\n")
        print("----------------------\n")
        print("Actions: \n")
        print("1. List ongoing transports")
        print("2. Add new transport")
        print("3. Deploy transport")
        print("4. Exit")
        print("----------------------\n")
        action = input("Choose an action: ")

        if action == "1":
            list_transports(transports_list)
        
        if action == "2":
            add_transport(transports_list)
        



if __name__ == "__main__":
    main()