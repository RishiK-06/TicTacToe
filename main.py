import random

def computer_move(board):
    def minimax_score(is_computer_turn):
        # recursively check scores
        if check_win(board, "O"): # win
            return 1
        if check_win(board, "X"): # loose
            return -1
        if not get_empty_positions(board): # draw
            return 0