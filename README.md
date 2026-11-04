# Python Tic-Tac-Toe

A small terminal game where you play **X** against a computer **O**. It tracks your score across rounds and keeps going until you quit with **Q**.

---

## What it does

- **You vs. Computer** — Human is X, AI is O
- **Hard AI** — Uses the Minimax algorithm
- **Score tracking** — Wins, losses, and draws persist across rounds
- **Play forever** — Enter `Q` at the prompt to exit

---

## How the Minimax works

it simulates every possible future move from the current board status:

1. **Look at all empty squares**
2. **Try each one** — temporarily place an **O** there
3. **Recurse** — gives the turn to users and thinks user will play his best option
4. **Keep going** until the game ends (win, loss, or draw)
5. **Score the outcome**  
   - Computer wins → `+1`  
   - You win → `-1`  
   - Draw → `0`
6. **Backtrack** — the computer picks the move that leads to the highest score (assuming you also play your best moves to minimize its score)

Because the game tree for tic-tac-toe is tiny, this runs instantly. The result: the AI never looses.

---

## How to play

Run it:
```bash
python main.py
```

![Demo video](demoGif.gif)

---
### Methods used
1. `get_empty_positions`
2. `check_win`
3. `print_board`
4. `computer_move` (minimax)
5. Main loop with score tracking and Q-quit
