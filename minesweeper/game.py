from board import generate_board

# Handles starting a new game
# Displays an empty board and allows only one reveal
def game_start(difficulty):
    if difficulty == "easy":
        height = 4
    elif difficulty == "medium":
        height = 8
    elif difficulty == "hard":
        height = 12
    
    # Create and display empty board
    player_board = [["#" for _ in range(32)] for _ in range(height)]
    print_board(player_board)

    # Ask for initial reveal coordinates (shouldn't be present on Codex)
    x, y = map(int, input("Enter starting tile: ").split())

    # Generate board and reveal initial tile
    board = generate_board(difficulty, x, y)
    reveal(player_board, board, x, y)

    # Start game loop
    game_loop(player_board, board)

# Handles the main game loop and what happens after game over
def game_loop(player_board, board):

    # Loop until game over
    while game_over(player_board, board) is False:

        # Display board and ask for action (shouldn't be present on Codex)
        print_board(player_board)
        action = input("Enter 'r x y' to reveal or 'f x y' to flag: ").split()

        # Process actions
        if action[0] == "r":
            x, y = int(action[1]), int(action[2])
            reveal(player_board, board, x, y)
        elif action[0] == "f":
            x, y = int(action[1]), int(action[2])

            # Switch flag on or off (ignore other tiles)
            if (player_board[y][x] == "#"):
                player_board[y][x] = "F"
            elif (player_board[y][x] == "F"):
                player_board[y][x] = "#"
    
    # Game ended so reveal all mines and display board
    reveal_all_mines(player_board, board)
    print_board(player_board)
    
    # Check if player won or lost (print statements will be different on Codex)
    if check_win(player_board, board):
        print("You Win!")
    else:
        print("Game Over! You hit a mine.")
    
    # Should not be present on Codex
    input("Press enter to return to the menu")

# Simple function to loop through the player board and reveal all mines
def reveal_all_mines(player_board, board):
    height = len(board)
    width = len(board[0])
    for y in range(height):
        for x in range(width):
            if board[y][x] == "M":
                player_board[y][x] = "M"

# Function to check if player won (all safe tiles revealed)
def check_win(player_board, board):
    height = len(board)
    width = len(board[0])
    for y in range(height):
        for x in range(width):

            # If there's a non-mine tile that's still hidden, game not won
            if board[y][x] != "M" and player_board[y][x] == "#":
                return False
    return True

# TODO: Implement the print_board function
# Function to print the current state of the board to the player
# Include row and column numbers for reference (will be removed for Codex)
def print_board(player_board):
    pass

# TODO: Implement the reveal function
# Update the board to reveal the tile at (x, y)
# Recursively reveal adjacent tiles if the revealed tile is a 0
def reveal(player_board, board, x, y):
    pass

# TODO: Implement the game_over function
# Checks to see if a mine was revealed or all safe tiles revealed
def game_over(player_board, board):
    pass