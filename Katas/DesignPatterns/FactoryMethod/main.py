from transport import Transport
from add_transport import add_transport
from list_transports import list_transports
from deploy_transport import deploy_transport
from typing import List

def main():
    action = ""
    transports_list: List[Transport] = []
    print("Factory Method Pattern \n")
    print("----------------------\n")
    
    while action != "4":
        print("\n----------------------\n")
        
        action = get_action_input()

        if action == "1":
            list_transports(transports_list)
        
        if action == "2":
            add_transport(transports_list)
        
        if action == "3":
            deploy_transport(transports_list)
        
def get_action_input() -> str:
    print("Actions: \n")
    print("1. List ongoing transports")
    print("2. Add new transport")
    print("3. Deploy transport")
    print("4. Exit")
    print("----------------------\n")
    return input("Choose an action: ")


if __name__ == "__main__":
    main()