import random 

class GuessingGame:
    def __init__(self):
        self._winning_number = None
        self._remaining_guesses = None
        self._guess = None

    def play(self):
        self._winning_number = random.randint(1, 100)
        self._remaining_guesses = 7

        while self._remaining_guesses > 0:
            self._display_remaining_guesses_prompt()
            self._guess = int(input("Enter a number between 1 and 100: "))
            self._validate_guess()
            self._display_guess_msg()

            if self._guess == self._winning_number:
                return

            self._remaining_guesses -= 1

        print("You have no more guesses. You lost!")
        print()

    def _display_remaining_guesses_prompt(self):
        if self._remaining_guesses > 1:
            print(f"You have {self._remaining_guesses} guesses remaining.")
        else:
            print(f"You have {self._remaining_guesses} guess remaining.")

    def _validate_guess(self):
        while True:
            if self._guess in range(1, 101):
                break
            self._guess = int(input("Invalid guess. Enter a number between " 
                            "1 and 100: "))

    def _display_guess_msg(self):
        if self._guess < self._winning_number:
            print("Your guess is too low.")
            print()
        elif self._guess > self._winning_number:
            print("Your guess is too high.")
            print()
        else:
            print("That's the number!")
            print()
            print("You won!")
            print()

game = GuessingGame()
game.play()