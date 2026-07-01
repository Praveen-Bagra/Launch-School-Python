# Rock Paper Scissors is a two-player game where each player chooses
# one of three possible moves: rock, paper, or scissors. The chosen moves
# will then be compared to see who wins, according to the following
# rules:

# - rock beats scissors (rock crushes scissors)
# - scissors beats paper (scissors but paper)
# - paper beats rock (paper wraps rock)

# If the player choose the same move, then it's a tie.

# Nouns: player, move(rock, paper, scissor), rule
# Verbs: choose, compare

# Player
#   - choose
# Move
# Rule

# - compare

import random
import os

class StringJoiningMixin:
    def join_with_or(self, seq):
        length = len(seq)
        match length:
            case 0:
                return ""
            case 1:
                return str(seq[0])
            case 2:
                return f'{seq[0]} or {seq[1]}'
            case _:
                new_seq = seq[:len(seq) - 1]
                return (', '.join([str(obj) for obj in new_seq]) +
                        f', or {seq[-1]}')

    def capitalize_join_with_space(self, seq):
        return ' '.join([str(obj).capitalize() for obj in seq])

class Score:
    def __init__(self):
        self._score = 0

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError("Only integers addition are allowed")

        obj = Score()
        obj._score = self._score + other
        return obj 

    def __iadd__(self, other):
        if not isinstance(other, int):
            raise TypeError("Only integers addition are allowed.")

        self._score += other
        return self

    def __eq__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        return self._score == other

    def __str__(self):
        return str(self._score)


class Move:
    def __str__(self):
        return self.__class__.__name__.lower()

class Rock(Move):
    def __gt__(self, other):
        if isinstance(other, Move):
            return isinstance(other, Scissors) or isinstance(other, Lizard)
        
        return NotImplemented

class Paper(Move):
    def __gt__(self, other):
        if isinstance(other, Move):
            return isinstance(other, Rock) or isinstance(other, Spock)
        
        return NotImplemented

class Scissors(Move):
    def __gt__(self, other):
        if isinstance(other, Move):
            return isinstance(other, Paper) or isinstance(other, Lizard)
        
        return NotImplemented

class Lizard(Move):
    def __gt__(self, other):
        if isinstance(other, Move):
            return isinstance(other, Paper) or isinstance(other, Spock)
        
        return NotImplemented

class Spock(Move):
    def __gt__(self, other):
        if isinstance(other, Move):
            return isinstance(other, Rock) or isinstance(other, Scissors)
        
        return NotImplemented

class Player:
    CHOICES = ('rock', 'paper', 'scissors', 'lizard', 'spock')
    MOVES_CLASS_REGISTRY = {
        'rock': Rock,
        'paper': Paper,
        'scissors': Scissors,
        'lizard': Lizard,
        'spock': Spock,
        }

    def __init__(self):
        self.move = None
        self.reset_score()

    def create_move(self, name):
        return Player.MOVES_CLASS_REGISTRY[name]()

    def reset_score(self):
        self.score = Score()

class Computer(Player):
    def choose(self):
        self.move = self.create_move(random.choice(Player.CHOICES))

class Human(StringJoiningMixin, Player):
    def choose(self):
        prompt = f'Please choose {self.join_with_or(Player.CHOICES)}: '

        while True:
            choice = input(prompt).lower()
            if choice.lower() in Player.CHOICES:
                break

            print(f'Sorry, {choice} is not valid')

        self.move = self.create_move(choice) 

class RPSGame(StringJoiningMixin):
    GAMES_TO_WIN_MATCH = 5

    def __init__(self):
        self._human = Human()
        self._computer = Computer()
        self._result = None
        self._reset_match()

    def _display_welcome_message(self):
        print(f'Welcome to {self.capitalize_join_with_space(Player.CHOICES)}!')
        print(f'The game is played to {RPSGame.GAMES_TO_WIN_MATCH} points. '
              f'Whosoever wins {RPSGame.GAMES_TO_WIN_MATCH} games first, '
              f'will win the match.')

    def _display_goodbye_message(self):
        print(f'Thanks for playing {self.capitalize_join_with_space(Player.CHOICES)}. Goodbye!')

    def _update_score(self):
        if self._human_wins():
            self._result = 'You win!'
            self._human.score += 1
        elif self._computer_wins():
            self._result = 'Computer wins!'
            self._computer.score += 1
        else:
            self._result = "It's a tie!" 
        

    def _display_winner_and_score(self):
        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        print(self._result)
        print(f"Current Score: You: {self._human.score}, "
              f"Computer: {self._computer.score}")
    
    def _human_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return human_move > computer_move

    def _computer_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return computer_move > human_move

    def _update_history(self):
        self._game_count += 1
        self._moves_history[f'Game {self._game_count:02d}'] = (
        {
            'You': str(self._human.move),
            'Computer': str(self._computer.move),
            'Result': self._result
        })

    def _print_history(self):
        for game, details in self._moves_history.items():
            print()
            print(game, end=' ==> ')
            for particulars, description in details.items():
                print(f'{particulars}: {description}', end='. ') 
        print()

    def _reset_match(self):        
        self._human.reset_score()
        self._computer.reset_score()
        self._game_count = 0
        self._moves_history = {}

    def _ready(self):
        input("Press any key to continue...")

    def _clear_screen(self):
        os.system('clear')

    def play(self):
        self._display_welcome_message()
        self._ready()
        self._clear_screen()

        while True:
            self._reset_match()

            while True:
                self._clear_screen()
                self._human.choose()
                self._computer.choose()
                self._update_score()
                self._display_winner_and_score()
                self._update_history()

                if self._human.score == RPSGame.GAMES_TO_WIN_MATCH:
                    print("You won the match!!!")
                    if self._history_show():
                        self._print_history()
                    break 
                elif self._computer.score == RPSGame.GAMES_TO_WIN_MATCH:
                    print("Computer won the match!!!")
                    if self._history_show():
                        self._print_history()
                    break 

                self._ready()

            if not self._play_again():
                break

        self._display_goodbye_message()

    def _history_show(self):
        prompt = "Would you like to see game-wise history of the match? (y/n) "
        return self._validate_answer(prompt)

    def _play_again(self):
        self._ready()
        self._clear_screen()
        prompt = "Would you like to play again? (y/n) "
        return self._validate_answer(prompt)

    def _validate_answer(self, prompt):
        while True:
            answer = input(prompt).lower()
            if answer.startswith('y') or answer.startswith('n'):
                break 
            print("Invalid choice.", prompt)

        return answer.lower().startswith('y')

RPSGame().play()