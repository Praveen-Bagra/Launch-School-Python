# input: string word containing capital letters
# output: integer
# rules:
#   Explicit:
#       - Compute the scrabble score i.e. sum the values of all
#         the tiles used in each word. Tile means letter and each letter
#         has a specific point
#   Implicit:
#       - Empty stirng will return 0 scrabble score.
# Data Structure and Algorithm:
#   - Initialize TILES to nested dictionary
#       - {('D', 'G'): 2, ('B', 'C', 'M', 'P'): 3....}
#   - Initialize the score to 0.
#   - Iterate over each letter
#       - Iterate over each key in TILES
#           - If letter is in key
#               - increase score by its associated value
#               - break
#   - Retrun score

class Scrabble:
    TILES = {('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'): 1,
             ('D', 'G'): 2,
             ('B', 'C', 'M', 'P'): 3,
             ('F', 'H', 'V', 'W', 'Y'): 4,
             ('K'): 5,
             ('J', 'X'): 8,
             ('Q', 'Z'): 10
    }

    def __init__(self, word):
        self._word = word

    def score(self):
        if not isinstance(self._word, str):
            return 0        

        scrabble_score = 0
        for letter in self._word.upper():
            for key, value in Scrabble.TILES.items():
                if letter in key:
                    scrabble_score += value
                    break

        return scrabble_score

    @classmethod
    def calculate_score(cls, word):
        return cls(word).score()
