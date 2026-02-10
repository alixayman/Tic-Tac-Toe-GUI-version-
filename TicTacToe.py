import random
winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]
class TicTacToe:
    def __init__(self):
        self._board = [" "," "," "," "," "," "," "," "," "]
    def reset_board(self):
        self._board = [" "," "," "," "," "," "," "," "," "]
    @property
    def board(self):
        return self._board
    def get_cell(self,i):
        return self._board[i]
    def winner(self):
        for combo in winning_combinations:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]
        return None

    def winner_line(self):
        for combo in winning_combinations:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return combo
        return None

    def make_move(self,position,player):
        self._board[position]=player
    def tie(self):
        return " " not in self._board
    def computer_turn_easy(self):
        while True:
            position = random.randint(0,8)
            if self._board[position]==" ":
                return position
    def computer_turn_medium(self,player,computer):
        position = 0
        while position < 9:
            if self._board[position] != ' ':
                position+=1
                continue
            self._board[position] = computer
            if self.winner() == computer:
                self._board[position] = ' '
                return position
            else:
                self._board[position] = " "
            position+=1
        position = 0
        while position < 9:
            if self._board[position] != ' ':
                position += 1
                continue
            self._board[position] = player
            if self.winner() == player:
                self._board[position] = ' '
                return position
            else:
                self._board[position] = " "
            position += 1
        return self.computer_turn_easy()

    def computer_turn_hard(self,player,computer):
        position = 0
        while position < 9:
            if self._board[position] != ' ':
                position += 1
                continue
            self._board[position] = computer
            if self.winner() == computer:
                self._board[position] = ' '
                return position
            else:
                self._board[position] = " "
            position += 1
        position = 0
        while position < 9:
            if self._board[position] != ' ':
                position += 1
                continue
            self._board[position] = player
            if self.winner() == player:
                self._board[position] = ' '
                return position
            else:
                self._board[position] = " "
            position += 1

        if self._board[4] == " ":
            return 4
        elif self._board[0] == " ":
            return 0
        elif self._board[2] == " ":
            return 2
        elif self._board[6] == " ":
            return 6
        elif self._board[8] == " ":
            return 8
        else:
            return self.computer_turn_easy()






