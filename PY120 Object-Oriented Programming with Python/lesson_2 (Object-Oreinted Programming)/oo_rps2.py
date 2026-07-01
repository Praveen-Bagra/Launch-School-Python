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

        return self

    def __iadd__(self, other):
        if not isinstance(other, int):
            raise TypeError("Only integers addition are allowed.")

        self._score += other
        return self._score

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
    def __init__(self):
        self._human = Human()
        self._computer = Computer()
        self._result = None
        self._moves_history = {}
        self._game_count = 0

    def _display_welcome_message(self):
        print(f'Welcome to {self.capitalize_join_with_space(Player.CHOICES)}!')

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
            self._result = "It's a tie" 
        

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

    def _update_and_print_moves_history(self):
        self._game_count += 1
        self._moves_history[f'Game {self._game_count:02d}'] = (
        {
            'You': str(self._human.move),
            'Computer': str(self._computer.move),
            'Result': self._result
        })

        for game, details in self._moves_history.items():
            print()
            print(game)
            for particulars, description in details.items():
                print(f'{particulars}: {description}') 

    def _score_reset(self):
        self._human.reset_score()
        self._computer.reset_score()

    def play(self):
        self._display_welcome_message()

        while True:
            self._score_reset()
            while True:
                self._human.choose()
                self._computer.choose()
                self._display_winner_and_score()
                self._update_and_print_moves_history()
                if self._human.score == 5 or self._computer.score == 5:
                    break

            if not self._play_again():
                break

        self._display_goodbye_message()

    def _play_again(self):
        answer = input("Would you like to play again? (y/n) ")
        return answer.lower().startswith('y')

RPSGame().play()