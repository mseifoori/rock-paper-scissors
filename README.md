## ✊📄✂ Rock Paper Scissors Game

Welcome to the Rock Paper Scissors Game!
This is a classic implementation of the popular game, built entirely in Python.

## 🧩 Features

- Interactive Gameplay: Play multiple rounds against the computer.
- Rules On Demand: View the rules any time.
- Randomized Computer Choice: The computer makes a fair random choice every round.
- Input Validation: Ensures you only enter valid moves.

## 📁 Project Structure

```
Rock_Paper_Scissors
│
├── src/
│    ├── main.py
│
└── README.md
```

## 🚀 How To Run

```Bash
python main.py
```

## 🧠 How It Works

The project is structured into:

welcome_user() → Greets the player, takes their action choice (play, rules, quit).

see_rules() → Displays the official game rules.

RockPaperScissors class:

getting_computer_choice() → Picks a random choice for the computer.

getting_user_choice() → Asks for and validates the user’s move.

user_choice_validation() → Ensures the input is valid, otherwise prompts again.

game_logic() → Determines the winner based on standard rules:

Rock beats Scissors

Scissors beats Paper

Paper beats Rock

play() → Runs the game loop and asks if the user wants to continue.

## 📝 Notes

This game runs entirely in the terminal/command line.

Python 3.6+ is required to run the game.

## 📃 License

This project is open-source and available under the MIT License.

## 💬 Contributing

Feel free to fork, modify, and submit a pull request!
