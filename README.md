# 🧮 Tic-Tac-Toe Math Challenge

A playful twist on the classic game!  
This Python-powered **Tic-Tac-Toe** isn’t just about strategy — you’ll need to flex your math muscles to win your turn. Can you outsmart the computer and ace the math problems?

---

## 📌 Table of Contents
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Installation](#-installation)
- [Code Structure](#-code-structure)
- [Future Improvements](#-future-improvements)

---

## 🎮 Features

- ✅ **Interactive Tic-Tac-Toe:** Play head-to-head with a computer.
- 🧠 **Math Challenges:** Solve simple addition problems to claim a square.
- 🤖 **Unpredictable AI:** The computer may sometimes skip its move.
- 🏆 **Win/Tie Detection:** Automatic detection of game outcomes.

---

## 🛠 How It Works

1. **Game Setup**
   - The board is displayed with squares numbered 1–9.
   - You play as `O`; the computer is `X`.

2. **Your Turn**
   - Select a square (1–9).
   - Solve an addition problem (e.g., `3 + 3`).  
   - Get it right? The spot is yours!

3. **Computer Turn**
   - Each round, the computer has a 50% chance to move (random empty spot) or skip its turn.

4. **Victory!**
   - First to align three marks wins.
   - If all squares fill up, it’s a tie.

---

## ⚙️ Installation

1. **Requirements:**  
   - Python 3.x

2. **Play the Game:**  
   ```bash
   python3 tic_tac_toe.py
   ```

---

## 📂 Code Structure

| Function            | Description                                    |
|---------------------|------------------------------------------------|
| `tic_tac_toe()`     | Prints the initial board layout.               |
| `move()`            | Updates & displays the board after each move.  |
| `computer_move()`   | Handles computer’s logic (move or skip).       |
| `win()`             | Checks for a win condition.                    |
| `tie()`             | Checks if the game is a draw.                  |
| `addition_equ()`    | Generates player’s math challenge.             |

**Key Variables:**
- `spaces_dict`: Tracks state of each square.
- `marked_spaces`: List of occupied squares.

---

## 🔮 Future Improvements

- **Difficulty Levels:** Tackle harder problems (like multiplication!).
- **GUI:** Add a graphical version with Pygame or Tkinter.
- **Smarter AI:** Make the computer actually try to win (minimax, anyone?).

---

## 🎉 Enjoy the Game!

Sharpen your mind as you play.  
Fork this repo, try it out, and make it your own!

---

## 👾 Demo

```
Welcome to Tic-Tac-Toe Land!
   |    |   
 1 |  2 |  3
   |    |   
--------------
   |    |   
 4 |  5 |  6
   |    |   
--------------
   |    |   
 7 |  8 |  9
   |    |   

Pick a square between 1 and 9: 5
3 + 3
What is the answer? 6
You are correct!
Now it's the computer's turn...
   |    |   
 1 |  2 |  3
   |    |   
--------------
   |    |   
 4 |  O |  6
   |    |   
--------------
   |    |   
 7 |  8 |  9
   |    |   
```

---

Created with ❤️ by [stefos41](https://github.com/stefos41)
