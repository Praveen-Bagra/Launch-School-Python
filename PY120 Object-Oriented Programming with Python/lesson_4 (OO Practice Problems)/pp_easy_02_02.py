class Game:
    count = 0

    def __init__(self, game_name):
        self._game_name = game_name
        Game.count += 1

    def play(self):
        return f'Start the {self._game_name} game!'

class Bingo(Game):
    def __init__(self, game_name, player_name):
        super().__init__(game_name)
        self._player_name = player_name

    @property
    def player_name(self):
        return self._player_name

class Scrabble(Game):
    def __init__(self, game_name, player_name1, player_name2):
        super().__init__(game_name)
        self._player_name1 = player_name1
        self._player_name2 = player_name2
    
    @property
    def player_name1(self):
        return self._player_name1

    @property    
    def player_name2(self):
        return self._player_name2

bingo = Bingo('Bingo', 'Bill')
print(Game.count)                       # 1
print(bingo.play())                     # Start the Bingo game!
print(bingo.player_name)                # Bill

scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
print(Game.count)                       # 2
print(scrabble.play())                  # Start the Scrabble game!
print(scrabble.player_name1)            # Jill
print(scrabble.player_name2)            # Sill
print(scrabble.player_name)
# AttributeError: 'Scrabble' object has no attribute 'player_name'k