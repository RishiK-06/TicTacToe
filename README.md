## Python Tic-Tac-Toe (Hard AI - MiniMax)

### What it does
- 2-player terminal game: You play **X**, Computer plays **O**.
- AI uses **Minimax** (unbeatable).
- Tracks wins / losses / draws and loops until you press **Q**.

### System Diagram

![System Diagram](pngTicTacToe.excalidraw.png)

### Files
- `target_code.py` — main program
- `pngTicTacToe.excalidraw.png` — system diagram

### How to run
```bash
python target_code.py
```

### Method order (predecessor-wise)
1. `get_empty_positions`
2. `check_win`
3. `print_board`
4. `computer_move` (minimax)
5. Main loop with score tracking and Q-quit
