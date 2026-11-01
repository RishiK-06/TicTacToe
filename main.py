
import random

# Score tracking
score = {
    "human_wins": 0,
    "computer_wins": 0,
    "draws": 0
}

# Get all empty positions available on the board
def get_empty_positions(board):

    # Check each cell and collect the indexes of empty positions
    return [i for i in range(9) if isinstance(board[i], int)]

# Check whether the given player has won the game
def check_win(board, symbol):

    # Store all possible winning combinations (rows, columns and diagonals)
    win_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    # Check whether all three positions in any combination contain the same symbol
    for line in win_lines:
        if all(board[i] == symbol for i in line):
            return True  # Player has won
    return False  # No winning combination found

# Display the Tic-Tac-Toe board in a 3x3 format
def print_board(board):

    # Loop through each row of the board
    for row in range(3):

        # Display three cells in the current row
        print(" | ".join(str(cell) for cell in board[row*3:(row+1)*3]))

        # Print separator between rows
        if row < 2:
            print("--+---+--")

# Easy difficulty
def easy_computer_move(board):
    empty_positions = get_empty_positions(board)
    return random.choice(empty_positions)


# Hard Mode: Minimax AI
def hard_computer_move(board):

    def minimax(is_computer_turn):

        if check_win(board, "O"):
            return 1

        if check_win(board, "X"):
            return -1

        if not get_empty_positions(board):
            return 0

        if is_computer_turn:
            best_score = -999
        else:
            best_score = 999

        for position in get_empty_positions(board):

            if is_computer_turn:
                board[position] = "O"
            else:
                board[position] = "X"

            result = minimax(not is_computer_turn)

            board[position] = position + 1

            if is_computer_turn:
                best_score = max(best_score, result)
            else:
                best_score = min(best_score, result)
        return best_score

    best_move = None
    best_value = -999

    for position in get_empty_positions(board):

        board[position] = "O"

        value = minimax(False)

        board[position] = position + 1

        if value > best_value:
            best_value = value
            best_move = position
    return best_move
