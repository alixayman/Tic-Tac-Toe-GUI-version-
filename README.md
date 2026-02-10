# Tic Tac Toe (Python + PyQt5)

A fully interactive **Tic Tac Toe game** built in Python using **PyQt5**, featuring **singleplayer and multiplayer modes**, multiple AI difficulty levels, and a clean graphical user interface.

---

## Features

### 🎮 Game Modes

* **Singleplayer**

  * Play against the computer
  * Three difficulty levels:

    * Easy (random moves)
    * Medium (basic strategy + blocking)
    * Hard (advanced strategy with optimal moves)
* **Multiplayer**

  * Two players play on the same device
  * Alternating turns (X / O)

---

### 🧠 Game Logic

* Win detection for all possible winning combinations
* Tie detection
* Highlighting of the winning line
* Turn management
* Board reset and replay functionality

---

### 🖥️ Graphical User Interface

* Built using **PyQt5**
* Responsive layout using `QVBoxLayout` and `QGridLayout`
* Dynamic UI flow:

  * Mode selection
  * Difficulty selection
  * Game board display
* Visual feedback for:

  * Winning moves
  * Disabled buttons
* Styled using Qt stylesheets (CSS-like styling)

---
## Technologies Used

* **Python 3**
* **PyQt5**
* Object-Oriented Programming (OOP)
* Event-driven programming

---

## How to Run

1. Make sure Python is installed (Python 3.9+ recommended)
2. Install PyQt5:

   ```bash
   pip install PyQt5
   ```
3. Run the GUI file:

   ```bash
   python gui.py
   ```

---

## Controls

* Click on a grid cell to place your mark
* Buttons guide you through:

  * Mode selection
  * Difficulty selection
* Use **Play Again** to restart
* Use **Exit** to close the game

---


