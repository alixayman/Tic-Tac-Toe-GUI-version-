import sys
from PyQt5.QtWidgets import (QApplication,QLabel, QWidget,
                             QVBoxLayout, QGridLayout, QPushButton)
from PyQt5.QtCore import Qt
from TicTacToe import TicTacToe


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.game = TicTacToe()
        self.mode = None
        self.difficulty = None
        self.turn_flag = True
        self.vbox = QVBoxLayout()
        self.gbox = QGridLayout()
        self.multiplayer_button = QPushButton('Multiplayer',self)
        self.singleplayer_button = QPushButton('Singleplayer',self)
        self.easy_button = QPushButton('Easy',self)
        self.medium_button = QPushButton('Medium',self)
        self.hard_button = QPushButton('Hard',self)
        self.modes_buttons = [self.singleplayer_button,self.multiplayer_button]
        self.difficulty_buttons = [self.easy_button,self.medium_button,self.hard_button]
        self.modes_functions = [self.singleplayer,self.multiplayer]
        self.difficulty_functions = [self.easy,self.medium,self.hard]
        for index in range(2):
            self.modes_buttons[index].hide()
            self.modes_buttons[index].clicked.connect(self.modes_functions[index])
        for index in range(3):
            self.difficulty_buttons[index].hide()
            self.difficulty_buttons[index].clicked.connect(self.difficulty_functions[index])
        self.buttons = []
        for index in range(9):
            btn = QPushButton()
            btn.clicked.connect(self.handle_click)
            btn.hide()
            self.buttons.append(btn)
        index = 0
        for row in range(3):
            for col in range(3):
                self.gbox.addWidget(self.buttons[index], row, col)
                index += 1
        self.play_again_button = QPushButton("Play Again", self)
        self.play_again_button.hide()
        self.play_again_button.clicked.connect(self.reset_game)
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.hide()
        self.exit_button.clicked.connect(self.close)
        self.label = QLabel(self)
        self.label.hide()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Tic Tac Toe')
        self.label.show()
        self.singleplayer_button.show()
        self.multiplayer_button.show()
        self.label.setText("Choose your mode")
        self.label.setAlignment(Qt.AlignCenter)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.singleplayer_button)
        self.vbox.addWidget(self.multiplayer_button)
        self.vbox.addWidget(self.play_again_button)
        self.vbox.addWidget(self.exit_button)
        self.vbox.addLayout(self.gbox)
        self.setLayout(self.vbox)
        self.setStyleSheet("""
                    QLabel,QPushButton {
                        padding: 15px;
                        margin: 10px;
                        font-weight: bold;
                    }
                    QPushButton{
                        background-color: hsl(350, 79%, 41%);
                        font-size: 40px;
                        border: 1px solid;
                        border-radius: 10px;   
                    }
                    QPushButton:hover {
                        background-color: hsl(350, 79%, 81%);
                    }
                    QLabel{
                        background-color: hsl(192, 100%, 50%);
                        border-radius: 10px;
                        font-size: 60px;
                    }
                """)



    def singleplayer(self):
        self.disable_modes_buttons()
        self.label.setText("Choose your difficulty")
        self.easy_button.show()
        self.medium_button.show()
        self.hard_button.show()
        self.vbox.addWidget(self.easy_button)
        self.vbox.addWidget(self.medium_button)
        self.vbox.addWidget(self.hard_button)
        self.mode = "singleplayer"


    def multiplayer(self):
        self.disable_modes_buttons()
        self.label.hide()
        self.show_grid_buttons()
        self.mode = "multiplayer"


    def easy(self):
        self.disable_difficulty_buttons()
        self.label.hide()
        self.show_grid_buttons()
        self.difficulty = "easy"

    def medium(self):
        self.disable_difficulty_buttons()
        self.label.hide()
        self.show_grid_buttons()
        self.difficulty = "medium"

    def hard(self):
        self.disable_difficulty_buttons()
        self.label.hide()
        self.show_grid_buttons()
        self.difficulty = "hard"

    def handle_click(self):
        btn = self.sender()
        position = self.buttons.index(btn)
        if self.mode == "singleplayer":
            self.handle_singleplayer(position)
        else:
            self.handle_multiplayer(position)
    def handle_singleplayer(self,position):
        self.buttons[position].setText("X")
        self.buttons[position].setEnabled(False)
        self.game.make_move(position, "X")
        result = self.game.winner()
        if result == "X":
            combo = self.game.winner_line()
            if combo:
                self.highlight_winning_line(combo)
            self.label.setText("You Won!")
            self.label.show()
            self.disable_grid_buttons()
            self.play_again_button.show()
            self.exit_button.show()
        elif self.game.tie():
            self.label.setText("It's a tie!")
            self.label.show()
            self.disable_grid_buttons()
            self.play_again_button.show()
            self.exit_button.show()
        else:
            if self.difficulty == "easy":
                ai_pos = self.game.computer_turn_easy()

            elif self.difficulty == "medium":
                ai_pos = self.game.computer_turn_medium("X","O")
            else:
                ai_pos = self.game.computer_turn_hard("X","O")

            self.game.make_move(ai_pos, "O")
            self.buttons[ai_pos].setEnabled(False)
            self.buttons[ai_pos].setText("O")

            result = self.game.winner()
            if result == "O":
                combo = self.game.winner_line()
                if combo:
                    self.highlight_winning_line(combo)
                self.label.setText("You Lost!")
                self.label.show()
                self.disable_grid_buttons()
                self.play_again_button.show()
                self.exit_button.show()
            elif self.game.tie():
                self.label.setText("It's a tie!")
                self.label.show()
                self.disable_grid_buttons()
                self.play_again_button.show()
                self.exit_button.show()
    def handle_multiplayer(self,position):
        self.buttons[position].setText("X" if self.turn_flag else "O")
        self.buttons[position].setEnabled(False)
        self.game.make_move(position, "X" if self.turn_flag else "O")
        result = self.game.winner()
        if result == "X" or result== "O":
            combo = self.game.winner_line()
            if combo:
                self.highlight_winning_line(combo)
            self.label.setText("Player1 Won!" if self.turn_flag else "Player2 Won!")
            self.label.show()
            self.disable_grid_buttons()
            self.play_again_button.show()
            self.exit_button.show()
        elif self.game.tie():
            self.label.setText("It's a tie")
            self.label.show()
            self.disable_grid_buttons()
            self.play_again_button.show()
            self.exit_button.show()
        self.turn_flag = not self.turn_flag

    def show_grid_buttons(self):
        for btn in self.buttons:
            btn.setEnabled(True)
            btn.show()

    def disable_grid_buttons(self):
        for btn in self.buttons:
            btn.setEnabled(False)

    def reset_grid_buttons(self):
        for btn in self.buttons:
            btn.setText("")
            btn.hide()
            self.reset_buttons_style_sheet(btn)

    def reset_buttons_style_sheet(self,btn):
        btn.setStyleSheet("""
            QPushButton{
                    background-color: hsl(350, 79%, 41%);
                    font-size: 40px;
                    border: 1px solid;
                    border-radius: 10px;   
            }
            QPushButton:hover {
                    background-color: hsl(350, 79%, 81%);
            }""")
    def disable_modes_buttons(self):
        self.singleplayer_button.hide()
        self.multiplayer_button.hide()
        self.singleplayer_button.setDisabled(True)
        self.multiplayer_button.setDisabled(True)

    def disable_difficulty_buttons(self):
        self.easy_button.hide()
        self.medium_button.hide()
        self.hard_button.hide()
        self.easy_button.setDisabled(True)
        self.medium_button.setDisabled(True)
        self.hard_button.setDisabled(True)

    def reset_game(self):
        self.game.reset_board()
        self.turn_flag = True
        self.mode = None
        self.difficulty = None
        self.reset_grid_buttons()
        for btn in self.difficulty_buttons:
            btn.hide()
            btn.setEnabled(True)
        for btn in self.modes_buttons:
            btn.show()
            btn.setEnabled(True)
        self.label.setText("Choose your mode")
        self.label.show()
        self.play_again_button.hide()
        self.exit_button.hide()

    def highlight_winning_line(self, combo):
        for index in combo:
            self.buttons[index].setStyleSheet("background-color: hsl(120, 79%, 50%);")


def main():
    app = QApplication(sys.argv)
    the_gui = GUI()
    the_gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
