
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
        print(" | ".join(str(cell) for cell in board[row*3:(row+1) *3]))

        # Print separator between rows
        if row < 2:
            print("--+---+--")


# Easy Mode: Random computer move
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


# Main game
def main():

    print("===== TIC TAC TOE =====")
    print("Player: X")
    print("Computer: O")

    # Difficulty selection
    while True:
        print("\nSelect Difficulty:")
        print("1. Easy")
        print("2. Hard")

        choice = input("Enter your choice (1/2): ")

        if choice in ["1", "2"]:
            break

        print("Invalid choice. Please select 1 or 2.")

    if choice == "1":
        print("\nEasy Mode Selected!")
    else:
        print("\nHard Mode Selected!")

    # Replay loop
    while True:

        board = list(range(1, 10))

        # Game loop
        while True:

            print_board(board)

            # Human turn
            try:
                human_input = int(input("Choose a position (1-9): "))
            except ValueError:
                print("Please enter a number.")
                continue

            human_index = human_input - 1

            if human_index not in get_empty_positions(board):
                print("Invalid position. Try again.")
                continue

            board[human_index] = "X"

            if check_win(board, "X"):
                print_board(board)
                print("Congratulations! You win!")
                score["human_wins"] += 1
                break

            if not get_empty_positions(board):
                print_board(board)
                print("It's a Draw!")
                score["draws"] += 1
                break

            # Computer turn
            if choice == "1":
                computer_index = easy_computer_move(board)
            else:
                computer_index = hard_computer_move(board)

            board[computer_index] = "O"

            print("\nComputer played:")
            
            if check_win(board, "O"):
                print_board(board)
                print("Computer Wins!")
                score["computer_wins"] += 1
                break

            if not get_empty_positions(board):
                print_board(board)
                print("It's a Draw!")
                score["draws"] += 1
                break

        # Display score
        print("\n===== SCOREBOARD =====")
        print("Your Wins:", score["human_wins"])
        print("Computer Wins:", score["computer_wins"])
        print("Draws:", score["draws"])

        again = input("\nPlay Again? (Y/N): ").strip().lower()

        if again != "y":
            print("Thanks for playing!")
            break


# Program execution
if __name__ == "__main__":
    main()


