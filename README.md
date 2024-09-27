# tic-tac-toe

# Tic-Tac-Toe Game (Command Line Version)

This is a command-line version of the classic Tic-Tac-Toe game built in Python. The game allows two players to take turns marking the spaces in a 3x3 grid with their chosen symbols ('X' or 'O'). The goal is to be the first player to get three of their symbols in a row, column, or diagonal. The game automatically checks for win conditions after every move, and declares the game a draw if all spaces are filled without a winner.

## Features:
- **Two-player mode:** Player 1 chooses either 'X' or 'O', and Player 2 gets the remaining symbol.
- **Dynamic UI:** A 3x3 grid is displayed after each move, showing the current state of the game.
- **Input validation:** Prevents players from selecting a space that is already taken.
- **Win detection:** Automatically checks for winning combinations (rows, columns, diagonals) after each move.
- **Draw detection:** Ends the game when all spaces are filled and there’s no winner.
  
## How to Play:
1. Player 1 selects either 'X' or 'O' to begin.
2. Players take turns inputting the number of the grid cell where they want to place their symbol.
3. The game checks for a winner after each turn.
4. The game ends when there is a winner or when all grid spaces are filled, resulting in a draw.
