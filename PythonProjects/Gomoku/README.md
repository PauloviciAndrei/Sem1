# Gomoku Game with AI Bot

## 📌 Overview
This is a **Gomoku (Five in a Row) game** implemented in **Python**. The game allows a human player to compete against an AI bot. The bot evaluates the board and makes strategic moves to either attack or defend, aiming to win the game. The game follows the standard **15x15 Gomoku board rules**.

## 🎮 Features
- **15x15 board** following Gomoku rules.
- **Human vs. AI Bot** gameplay.
- **Validations** for player moves (ensures valid positions and prevents overriding existing pieces).
- **AI Bot Strategies**:
  - Identifies the best move using line, column, and diagonal evaluations.
  - Can block opponent's winning moves.
  - Attempts to create five in a row to win the game.

## 🎯 How to Play
- You will be prompted to **enter your move** in the format `row column` (e.g., `7 8`).
- The AI bot will **automatically make a move** after yours.
- The game continues until:
  - **You or the bot wins** by forming a line of 5 pieces.
  - The **board is full** (draw situation).

## 🤖 AI Bot Strategy
The AI evaluates the board to:
1. **Find the longest consecutive pieces in a row, column, or diagonal.**
2. **Defend against the player** if they are close to winning.
3. **Attack strategically** by extending its own sequences.
4. **Move towards the center** if no immediate attack or defense is required.

## 🚀 Example Gameplay
```
Your move: 7 8
AI moves: 6 8
Your move: 8 8
AI moves: 9 8
...
You won!
Play again?
1. Yes
2. No
```

