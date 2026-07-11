import random
import os

def clear_screen():
    os.system('clear')

def join_or(lst, delimiter=', ', last_delimiter='or'):
    if len(lst) > 2:
        return (delimiter.join(str(obj) for obj in lst[:-1]) + 
            f'{delimiter}{last_delimiter} {lst[-1]}')

    return f' {last_delimiter} '.join([str(obj) for obj in lst])

class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    def __str__(self):
        return self.marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

class Board:
    def __init__(self):
        self.reset()

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |"
              f"  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |"
              f"  {self.squares[5]}  |"
              f"  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |"
              f"  {self.squares[9]}")
        print("     |     |")
        print()

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def unused_squares(self):
        return [key
                for key, square in self.squares.items()
                if square.is_unused()]

    def is_full(self):
        return len(self.unused_squares()) == 0

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)

    def reset(self):
        self.squares = {key: Square() for key in range(1, 10)}

    def get_unused_square(self, seq):
        for key in seq:
            if self.squares[key].is_unused():
                return key

        return None

class Player:
    def __init__(self, marker):
        self.marker = marker
        self.reset()

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

    def reset(self):
        self.wins = 0

    def increment_wins(self):
        self.wins += 1

    @property
    def wins(self):
        return self._wins

    @wins.setter
    def wins(self, wins):
        self._wins = wins


class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    )

    GAMES_TO_WIN_MATCH = 3

    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
        self.human_first = True

    def play(self):
        clear_screen()
        self._display_welcome_message()
        input("Press any key to continue...")

        while True:
            self._play_match()
            if not self._play_again():
                break

        self._display_goodbye_message()

    def _play_match(self):
        self._reset_player_wins()

        while True:
            self._play_one_game()
            self._update_scores()
            self._display_board_with_clear()
            self._display_results()
            self.human_first = not self.human_first

            if self._someone_won_the_match():
                break

            self._display_scores()
            input('Ready for the next game. Press any key to continue...')

        self._display_match_results()

    def _play_one_game(self):
        self.board.reset()
        current_player = self.human if self.human_first else self.computer
        self._display_board_with_clear()

        if not self.human_first:
            print("==> Computer goes first this game.")
            input("==> Press any key to continue...")

        while True:
            self._player_moves(current_player)
            if self._is_game_over():
                return
            self._display_board_with_clear()
            current_player = self._toggle_player(current_player)

    def _display_welcome_message(self):
        print(f"Welcome to Tic Tac Toe! The match consist of multiple "
              f"games. Whosoever wins {TTTGame.GAMES_TO_WIN_MATCH} games "
              f"first, will win the match.")

    def _display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe! Goodbye!")

    def _display_results(self):
        if self._is_winner(self.human):
            print("You won! Congratulations!")
        elif self._is_winner(self.computer):
            print("I won! I won! Take that, human!")
        else:
            print("A tie game. How boring.")

    def _is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self._three_in_a_row(player, row):
                return True

        return False

    def _human_moves(self):
        valid_choices = self.board.unused_squares()
        choices_str = join_or(valid_choices)

        while True:
            prompt = f"Choose a square ({choices_str}): "
            choice = input(prompt)

            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("Sorry, that's not a valid choice.")
            print()

        self.board.mark_square_at(choice, self.human.marker)

    def _computer_moves(self):
        valid_choices = self.board.unused_squares()

        choice = (self._get_attacking_square() or
                  self._get_defending_square() or
                  (5 if 5 in valid_choices else None) or
                  random.choice(valid_choices))

        self.board.mark_square_at(choice, self.computer.marker)

    def _is_game_over(self):
        return self.board.is_full() or self._someone_won()

    def _three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def _someone_won(self):
        return (self._is_winner(self.human) or
                self._is_winner(self.computer))

    def _play_again(self):
        prompt = "Do you want to play again? (y/n) "

        while True:
            answer = input(prompt).lower()
            if answer in ['y', 'n']:
                break
            print("Please enter 'y' or 'n'.")

        if answer == 'y':
            clear_screen()
            print()
        return answer == 'y'

    def _get_defending_square(self):
        return self._critical_square(self.human)

    def _get_attacking_square(self):
        return self._critical_square(self.computer)

    def _critical_square(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.board.count_markers_for(player, row) == 2:
                key = self.board.get_unused_square(row)
                if key:
                    return key
        return None

    def _reset_player_wins(self):
        self.human.reset()
        self.computer.reset()

    def _update_scores(self):
        if self._is_winner(self.human):
            self.human.increment_wins()

        if self._is_winner(self.computer):
            self.computer.increment_wins()

    def _display_scores(self):
        print(f"You won: {self.human.wins}, "
              f"Computer won: {self.computer.wins}")

    def _someone_won_the_match(self):
        return (self.human.wins == TTTGame.GAMES_TO_WIN_MATCH or
            self.computer.wins == TTTGame.GAMES_TO_WIN_MATCH)

    def _display_match_results(self):
        if self.human.wins == TTTGame.GAMES_TO_WIN_MATCH:
            print("Yahoo!!! You won the match.")
        elif self.computer.wins == TTTGame.GAMES_TO_WIN_MATCH:
            print("Computer won the match!!! You lost!!")

    def _display_board_with_clear(self):
        clear_screen()
        self._display_scores()
        self.board.display()

    def _player_moves(self, player):
        if player == self.human:
            self._human_moves()
        else:
            self._computer_moves()

    def _toggle_player(self, player):
        return self.computer if player == self.human else self.human


game = TTTGame()
game.play()