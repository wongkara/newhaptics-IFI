from game import game_start

# Display the menu and rules
# None of the input() calls or invalid inputs should be present on Codex
def menu():
    
    while True:
        print("\n1. Start")
        print("2. Rules")
        print("3. Quit")
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == "1":
            print("\n1. Easy")
            print("2. Medium")
            print("3. Hard")
            print("4. Back")
            choice = input("Enter choice (1-4): ").strip()
            
            if choice == "1":
                game_start("easy")
                continue
            elif choice == "2":
                game_start("medium")
                continue
            elif choice == "3":
                game_start("hard")
                continue
            elif choice == "4":
                continue
            else:
                print("\nInvalid input")
                continue
        
        elif choice == "2":
            print("\nTriple tap to start the board")
            print("Double tap to place a flag")
            print("Triple tap to reveal a tile")
            print("Numbers show mines in adjacent 8")
            input("Press enter to return to the menu")
            
        elif choice == "3":
            break
        
        else:
            print("\nInvalid input")
            continue