class Anagram:
    def __init__(self, word):
        self._word = word

    def match(self, words_lst):
        char_counts = self.case_insensitive_char_counts(self._word)

        anagrams = []
        for word in words_lst:
            current_char_counts = self.case_insensitive_char_counts(word)

            if (char_counts == current_char_counts and 
              word.lower() != self._word.lower()):
                anagrams.append(word)

        return anagrams 
    
    @staticmethod
    def case_insensitive_char_counts(word):
        word = word.lower()
        char_counts = {}

        for char in word:
            char_counts.setdefault(char, 0)
            char_counts[char] += 1
        
        return char_counts

