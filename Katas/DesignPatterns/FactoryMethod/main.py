def main():
    action = ""
    while action != "3":
        print("\n")
        print("Factory Method Pattern \n")
        print("----------------------\n")
        print("Actions: \n")
        print("1. List ongoing transports")
        print("2. Add new transport")
        print("3. Exit")
        print("----------------------\n")
        action = input("Choose an action: ")

        if action == "1":
            print("List ongoing transports")
            input("Press enter to continue...")
        
        if action == "2":
            print("Add new transport")
            input("Press enter to continue...")
        



if __name__ == "__main__":
    main()