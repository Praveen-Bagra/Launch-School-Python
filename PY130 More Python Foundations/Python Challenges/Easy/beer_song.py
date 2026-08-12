class BeerSong:
    def __init__(self, start_num, end_num=None):
        self._start_num = start_num
        self._end_num = end_num

    def details(self):
        if self._end_num is None:
            self._end_num = self._start_num - 1
        else:
            self._end_num -= 1

        song_verses = []
        for num in range(self._start_num, self._end_num, -1):
            verse = (f"{num} bottles of beer on the wall, "
                        f"{num} bottles of beer.\n"
                        f"Take one down and pass it around, "
                        f"{num - 1} bottles of beer on the wall.\n")

            if num == 2:
                verse = ("2 bottles of beer on the wall, 2 bottles of beer.\n"
                        "Take one down and pass it around, 1 bottle of beer on the wall.\n")

            if num == 1:
                verse = ("1 bottle of beer on the wall, 1 bottle of beer.\n"
                            "Take it down and pass it around, no more bottles of beer on the wall.\n")

            if num == 0:
                verse = ("No more bottles of beer on the wall, no more bottles of beer.\n"
                            "Go to the store and buy some more, 99 bottles of beer on the wall.\n")

            song_verses.append(verse)

        return '\n'.join(song_verses)

    @classmethod
    def verse(cls, num):
        return cls(num).details()

    @classmethod
    def verses(cls, start_num, end_num):
        return cls(start_num, end_num).details()
    
    @classmethod
    def lyrics(cls):
        return cls(99, 0).details()

