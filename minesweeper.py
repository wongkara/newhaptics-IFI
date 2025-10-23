import random

# Function returns a 2D array containing M for a mine or the number of adjacent mines
# Size and mine count depends on difficulty
# Initial x and y are passed in to ensure the first tile clicked is a 0
def generate_board(difficulty, initial_x, initial_y):
    
    # Set difficulties
    if difficulty == "easy":
        width, height, mines = 32, 4, 20
    elif difficulty == "medium":
        width, height, mines = 32, 8, 40
    elif difficulty == "hard":
        width, height, mines = 32, 12, 75
    else:
        raise ValueError("Invalid input")
    
    # Generate a 2D bool array that indicates location of mines
    mine_board = [[False for _ in range(width)] for _ in range(height)]
    
    # Create a safe zone around the initial x and y so mines cannot generate there
    safe_zone = set()
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            new_x = initial_x + dx
            new_y = initial_y + dy
            if 0 <= new_x < width and 0 <= new_y < height:
                safe_zone.add((new_x, new_y))
    
    # Generate mines from remaining avaiable positions
    available_positions = [(x, y) for y in range(height) for x in range(width) if (x, y) not in safe_zone]
    mine_positions = random.sample(available_positions, mines)
    for x, y in mine_positions:
        mine_board[y][x] = True
    
    # Generate 2D array that will display minesweeper board
    board = [["0" for _ in range(width)] for _ in range(height)]
    
    # Loop through mine_board and count number of adjacent mines for each tile
    for y in range(height):
        for x in range(width):
            if mine_board[y][x]:
                board[y][x] = "M"
            else:
                count = 0
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        new_x = x + dx
                        new_y = y + dy
                        if (0 <= new_x < width and 0 <= new_y < height and mine_board[new_y][new_x]):
                            count += 1
                board[y][x] = str(count)
    
    # Return minesweeper board
    return board

# Display the menu and rules
# None of the input() calls or invalid inputs should be present on codex
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
                play("easy")
                continue
            elif choice == "2":
                play("medium")
                continue
            elif choice == "3":
                play("hard")
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

if __name__ == "__main__":
    menu()
