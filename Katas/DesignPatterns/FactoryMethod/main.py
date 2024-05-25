from transport import Transport
from add_transport import add_transport
from list_transports import list_transports
from deploy_transport import deploy_transport
from typing import List
import constants

def main():
    action = ""
    transports_list: List[Transport] = []
    print("Factory Method Pattern \n")

    while action != constants.EXIT_ACTION:
        print("----------------------")
        
        action = get_action_input()

        if action == constants.LIST_TRANSPORTS_ACTION:
            list_transports(transports_list)
        
        if action == constants.ADD_TRANSPORT_ACTION:
            add_transport(transports_list)
        
        if action == constants.DEPLOY_TRANSPORT_ACTION:
            deploy_transport(transports_list)
        
def get_action_input() -> str:
    actions = {
        constants.LIST_TRANSPORTS_ACTION: "List transports",
        constants.ADD_TRANSPORT_ACTION: "Add transport",
        constants.DEPLOY_TRANSPORT_ACTION: "Deploy transport",
        constants.EXIT_ACTION: "Exit"
    }
    print("Actions:")
    sorted_actions = sorted(actions.items())
    for action in sorted_actions:
        print(f"{action[0]}. {action[1]}")
    
    print("----------------------")
    return input("Choose an action: ")


if __name__ == "__main__":
    main()