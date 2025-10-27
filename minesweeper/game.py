"""
Minesweeper Game Logic
Handles the main loop, turns, input, and win/loss conditions.
"""

import random
from board import generate_board

class Game:
    def __init__(self, difficulty="easy"):
        self.difficulty = difficulty
        self.board = None
        self.player_board = None
        self.width = 0
        self.height = 0
        self.started = False
        self.game_over = False
        self.win = False
        self.remaining_safe = 0
        self.moves = 0

    def start(self, x, y):
        """Generate board and start game with first reveal."""
        self.board = generate_board(self.difficulty, x, y)
        self.height = len(self.board)
        self.width = len(self.board[0])
        self.player_board = [["#" for _ in range(self.width)] for _ in range(self.height)]
        self.remaining_safe = sum(1 for row in self.board for v in row if v != "M")
        self.started = True
        return self.reveal(x, y)

    def toggle_flag(self, x, y):
        """Place or remove a flag on hidden tile."""
        if self.game_over:
            return
        if not self.in_bounds(x, y):
            print(f"Invalid coordinates ({x}, {y}). Valid range: x=0-{self.width-1}, y=0-{self.height-1}")
            return
        if self.player_board[y][x] not in ("#", "F"):
            return
        if self.player_board[y][x] == "#":
            self.player_board[y][x] = "F"
        elif self.player_board[y][x] == "F":
            self.player_board[y][x] = "#"

    def reveal(self, x, y):
        """Reveal a tile; handles flood-fill for zeros."""
        if self.game_over:
            return
        if not self.in_bounds(x, y):
            print(f"Invalid coordinates ({x}, {y}). Valid range: x=0-{self.width-1}, y=0-{self.height-1}")
            return
        if self.player_board[y][x] in ("F", str(self.board[y][x])):
            return

        val = self.board[y][x]
        self.moves += 1

        # --- Case 1: Mine ---
        if val == "M":
            self.player_board[y][x] = "M"
            self.game_over = True
            self.win = False
            self.reveal_all_mines()
            print("Game Over! You hit a mine.")
            return

        # --- Case 2: Number > 0 ---
        if val != "0":
            self.player_board[y][x] = str(val)
            self.remaining_safe -= 1

        # --- Case 3: 0 (empty) — flood fill ---
        else:
            self._flood_fill(x, y)

        # --- Check win condition ---
        if self.remaining_safe == 0:
            self.game_over = True
            self.win = True
            print("You Win!")
            self.reveal_all_mines()

    def _flood_fill(self, x, y):
        """Recursive reveal of empty (0) tiles."""
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if not self.in_bounds(cx, cy):
                continue
            if self.player_board[cy][cx] != "#":
                continue
            val = self.board[cy][cx]
            self.player_board[cy][cx] = " " if val == "0" else str(val)
            if val == "0":
                for nx in range(cx - 1, cx + 2):
                    for ny in range(cy - 1, cy + 2):
                        if (nx, ny) != (cx, cy) and self.in_bounds(nx, ny):
                            if self.player_board[ny][nx] == "#":
                                stack.append((nx, ny))
            self.remaining_safe -= 1

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def reveal_all_mines(self):
        """Reveal all mines at the end of the game."""
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == "M":
                    self.player_board[y][x] = "M"

    def print_board(self):
        """Print the current player board (CLI visualization)."""
        # Print column numbers header - add space after each number
        header = "   "
        for x in range(min(self.width, 20)):
            header += f"{x:>2} "
        print(header.rstrip())
        
        for y in range(self.height):
            row_str = f"{y}  "
            for x in range(min(self.width, 20)):
                row_str += f"{self.player_board[y][x]:>2} "
            print(row_str.rstrip())
        print()

    def status(self):
        """Return current game status."""
        if self.win:
            return "win"
        elif self.game_over:
            return "loss"
        else:
            return "ongoing"


# --- Test code ---
if __name__ == "__main__":
    game = Game("easy")
    print("Welcome to Minesweeper! (coordinates: x y)")
    x, y = map(int, input("Enter starting tile: ").split())
    game.start(x, y)
    game.print_board()

    while not game.game_over:
        action = input("Enter 'r x y' to reveal or 'f x y' to flag: ").split()
        if not action:
            continue
        if action[0] == "r":
            game.reveal(int(action[1]), int(action[2]))
        elif action[0] == "f":
            game.toggle_flag(int(action[1]), int(action[2]))
        else:
            print("Invalid input.")
        game.print_board()

    print(f"Game ended: {game.status()} in {game.moves} moves.")
