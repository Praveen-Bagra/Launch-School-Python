# Tic Tac Toe is a game where each player makes its marker once.
# Whenever there is a winning combination for any player, that player
# wins.

# Nouns
# Game
# Human
# Computer
# Board
import os
import random

class Board:
    WINNING_LINES = [[1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
                     [1, 4, 7], [2, 5, 8], [3, 6, 9], # columns
                     [1, 5, 9], [3, 5, 7]] # diagonals

    def __init__(self):
        self._state = None
        self._winner_marker = None
        self.reset()

    def display(self):
        self._space_line()
        print(f'  {self._state[1]}  |  {self._state[2]}  |  {self._state[3]}')
        self._space_line()
        self._dash_line()
        self._space_line()
        print(f'  {self._state[4]}  |  {self._state[5]}  |  {self._state[6]}')
        self._space_line()
        self._dash_line()
        self._space_line()
        print(f'  {self._state[7]}  |  {self._state[8]}  |  {self._state[9]}')
        self._space_line()

    def _space_line(self):
        print(f'{' ' * 5}|{' ' * 5}|')

    def _dash_line(self):
        print('-' * 17)

    def reset(self):
        self._state = {}
        for num in range(1, 10):
            self._state[num] = ' '
        self._winner_marker = None

    def anyone_win(self):
        for line in self.WINNING_LINES:
            sq1, sq2, sq3 = line
            if ((self._state[sq1] == self._state[sq2] == self._state[sq3]) and
                    self._state[sq1] != ' '):
                return True

        return False

    def update_winner_marker(self):
        for line in self.WINNING_LINES:
            sq1, sq2, sq3 = line
            if ((self._state[sq1] == self._state[sq2] == self._state[sq3]) and
                    self._state[sq1] != ' '):
                self._winner_marker = self._state[sq1]

    def full(self):
        return len([num for num, value in self._state.items()
                        if value == ' ']) == 0

    def get_unused_spaces(self):
        return [str(num) for num, value in self._state.items()
                    if value == ' ']

    def mark_square(self, position, marker):
        self._state[position] = marker

    @property
    def winner_marker(self):
        return self._winner_marker

class Player:
    def __init__(self, marker):
        self._marker = marker

    @property
    def marker(self):
        return self._marker

class Human(Player):
    def mark(self, board):
        unused_spaces = board.get_unused_spaces()
        while True:
            print(f"Please choose from {', '.join(unused_spaces)}.")
            choice = input()
            if choice in unused_spaces:
                break
            print("Not a valid choice.")

        board.mark_square(int(choice), self.marker)

class Computer(Player):
    def mark(self, board):
        unused_spaces = board.get_unused_spaces()
        choice = random.choice(unused_spaces)
        board.mark_square(int(choice), self.marker)

class TicTacToeGame:
    def __init__(self):
        self._human = Human('X')
        self._computer = Computer('O')
        self._board = Board()

    def play(self):
        while True:
            self._board.reset()
            self._clear_screen()
            self._display_welcome_msg()
            self._board.display()

            while True:
                self._human.mark(self._board)
                if self._board.anyone_win() or self._board.full():
                    break

                self._computer.mark(self._board)
                if self._board.anyone_win() or self._board.full():
                    break

                self._clear_screen()
                print()
                self._board.display()

            self._clear_screen()
            print()
            self._board.display()

            if self._board.anyone_win():
                self._board.update_winner_marker()
                self._diplay_winner_msg()
            else:
                print("It's a tie.")

            if not self._play_again():
                break

        self._display_end_msg()

    def _clear_screen(self):
        os.system('clear')

    def _display_welcome_msg(self):
        print("Welcome to Tic Tac Toe!!")

    def _ready_prompt(self):
        input("Press any key to continue...")

    def _diplay_winner_msg(self):
        if self._board.winner_marker == self._human.marker:
            print("You win!!!")
        elif self._board.winner_marker == self._computer.marker:
            print("Computer wins!!!")

    def _play_again(self):
        prompt = "Do you want to play again (y/n)? "
        while True:
            answer = input(prompt).lower()
            if answer and answer[0] in ['y', 'n']:
                break
            print("Invalid choice.", end=' ')

        return answer[0] == 'y'

    def _display_end_msg(self):
        print("Thanks for playing Tic Tac Toe!!!")

TicTacToeGame().play()