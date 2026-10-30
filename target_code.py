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


def computer_move(board):
    def minimax_score(is_computer_turn):
        """Recursively score board states."""
        if check_win(board, "O"):   # Computer win
            return 1
        if check_win(board, "X"):   # Human win
            return -1
        if not get_empty_positions(board):  # No moves left
            return 0

        if is_computer_turn:
            best_score = -999
        else:
            best_score = 999
        for position in get_empty_positions(board):
            # Simulate placing symbol
            if is_computer_turn:
                board[position] = "O"
            else:
                board[position] = "X"
            score_value = minimax_score(not is_computer_turn)
            # Undo simulation (restore number)
            board[position] = position + 1
            # Computer wants max; human wants min
            if is_computer_turn:
                best_score = max(best_score, score_value)
            else:
                best_score = min(best_score, score_value)
        return best_score

    best_move = None
    best_value = -999
    for position in get_empty_positions(board):
        board[position] = "O"
        value = minimax_score(False)  # Next turn is human
        board[position] = position + 1
        if value > best_value:
            best_value = value
            best_move = position
    return best_move


# Main game loop: play forever until user quits with Q
while True:
    # Fresh board for each match
    board = list(range(1, 10))

    # Inner loop: one full game until win/draw
    while True:
        print_board(board)

        # Human turn
        try:
            human_input = int(input("You are X. Pick 1-9: "))
        except Exception:
            continue
        human_index = human_input - 1

        # Validate
        if human_index not in get_empty_positions(board):
            print("Invalid move. Try again.")
            continue

        # Apply X
        board[human_index] = "X"
        if check_win(board, "X"):
            print_board(board)
            print("You win!")
            score["human_wins"] += 1
            break
        if not get_empty_positions(board):
            print_board(board)
            print("Draw!")
            score["draws"] += 1
            break

        # Computer turn (Hard/Minimax)
        computer_index = computer_move(board)
        board[computer_index] = "O"
        if check_win(board, "O"):
            print_board(board)
            print("Computer wins!")
            score["computer_wins"] += 1
            break
        if not get_empty_positions(board):
            print_board(board)
            print("Draw!")
            score["draws"] += 1
            break

    # Score and replay
    print("\n=== SCORE ===")
    print(f"You (X): {score['human_wins']}")
    print(f"Computer (O): {score['computer_wins']}")
    print(f"Draws: {score['draws']}")
    print()
    again = input("Play again? (Q to quit): ").strip().lower()
    if again == "q" or again == "quit":
        print("Goodbye.")
        break