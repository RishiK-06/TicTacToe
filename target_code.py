# Tic-Tac-Toe: Human (X) vs Computer AI (O) — Minimax

# Score tracking dictionary
score = {
    "human_wins": 0,
    "computer_wins": 0,
    "draws": 0
}

# board is a list from [0-9]

def get_empty_positions(board):
    """Return list of indices that are still empty (numbers 1-9)."""
    return [i for i in range(9) if isinstance(board[i], int)]


def check_win(board, player_symbol):
    """Check if player_symbol has won."""
    win_lines = [
        [0, 1, 2],  # top row
        [3, 4, 5],  # middle row
        [6, 7, 8],  # bottom row
        [0, 3, 6],  # left col
        [1, 4, 7],  # center col
        [2, 5, 8],  # right col
        [0, 4, 8],  # diagonal
        [2, 4, 6],  # anti-diagonal
    ]
    for line in win_lines:
        if all(board[i] == player_symbol for i in line):
            return True
    return False


def print_board(board):
    """Display the 3x3 board."""
    for row in range(3):
        # Extract the three cells for this row
        line_cells = board[row * 3:(row + 1) * 3]
        print(" | ".join(str(cell) for cell in line_cells))
        if row < 2:
            print("--+--+--")

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