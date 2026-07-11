import random
import os

def clear_screen():
    os.system('clear')

def join_and(lst, delimiter=', ', last_delimiter='and'):
    if len(lst) > 2:
        return (delimiter.join(str(obj) for obj in lst[:-1]) + 
            f'{delimiter}{last_delimiter} {lst[-1]}')

    return f' {last_delimiter} '.join([str(obj) for obj in lst])

class Card:
    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    def __str__(self):
        return f"{self._value} of {self._suit}"

    @property
    def value(self):
        return self._value

    def is_ace(self):
        return self.value == 'Ace'

class Deck:
    def __init__(self):
        self.reset()

    def reset(self):
        self._cards = self._initialize_deck()
    
    @staticmethod
    def _initialize_deck():
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

        values = ([str(num) for num in range(2, 11)] + 
                 ['Jack', 'Queen', 'King', 'Ace'])

        deck = [Card(suit, value)
                for suit in suits
                for value in values]

        random.shuffle(deck)
        return deck

    def get_a_card(self):
        return self._cards.pop()

class Participant:
    def __init__(self):
        self.reset()

    def reset(self):
        self._cards = []

    def deal_a_card(self, card):
        self._cards.append(card)

    @property
    def cards(self):
        return self._cards

class Player(Participant):
    def __init__(self):
        super().__init__()

class Dealer(Participant):
    def __init__(self):
        super().__init__()

    def get_first_card(self):
        if self._cards:
            return self._cards[0]

        return None

class TwentyOneGame:
    def __init__(self):
        self._player = Player()
        self._dealer = Dealer()
        self._deck = Deck()

    def play(self):
        clear_screen()
        self._display_welcome_msg()
    
        while True:
            clear_screen()
            self._deal_two_cards(self._player)
            self._deal_two_cards(self._dealer)
            self._display_player_cards()
            self._display_dealer_first_card()
            self._player_chooses()
            if not self._is_busted(self._player):
                self._dealer_chooses()

            self._display_results()

            if not self._play_again():
                break

            self._reset_game()
        
        self._display_goodbye_msg()

    @staticmethod
    def _display_welcome_msg():
        print("Welcome to Twenty-One Game. The goal of Twenty-One is to \n"
              "try to get as close to 21 as possible without going over. \n"
              "If you go over 21, it's a bust, and you lose.")
        print("Are you ready to play?")
        input("Press any key to continue...")

    def _deal_a_card(self, dealer_or_player): 
        card = self._deck.get_a_card()
        dealer_or_player.deal_a_card(card)

    def _deal_two_cards(self, dealer_or_player):
        for _ in range(2):
            self._deal_a_card(dealer_or_player)

    def _display_player_cards(self):
        print(f'You have {join_and(self._player.cards)} with '
              f'a total of {self._total_cards_value(self._player)}.')

    def _display_dealer_first_card(self):
        print(f'Dealer has {self._dealer.get_first_card()} and '
              f'an unknown card.')

    def _display_dealer_cards(self):
        print(f'Dealer has {join_and(self._dealer.cards)} with '
              f'a total of {self._total_cards_value(self._dealer)}.')

    @staticmethod
    def _get_choice():
        print()
        prompt = "Do you want to hit(h) or stay(s)? "
        while True:
            answer = input(prompt).lower()
            if answer in ['h', 's']:
                break
            print()
            print("Invalid choice. Please enter 'h' or 's'.")

        print()
        return answer

    def _player_chooses(self):
        while True: 
            player_choice = self._get_choice()
            if player_choice == 'h':
                self._deal_a_card(self._player)
                if self._is_busted(self._player):
                    return
                
                clear_screen()
                print("You choose to hit.")
                self._display_player_cards()
                continue

            print("You choose to stay.")
            print()
            return

    def _dealer_chooses(self):
        print("Dealer turn...")
        print()
        while self._total_cards_value(self._dealer) < 17:
            print("Dealer hits.")
            self._deal_a_card(self._dealer)
            self._display_dealer_cards()
            print()

        if not self._is_busted(self._dealer):
            if len(self._dealer.cards) == 2:
                self._display_dealer_cards()
            print("Dealer choose to stay.")
            print()

    def _is_busted(self, player_or_dealer):
        return self._total_cards_value(player_or_dealer) > 21

    @staticmethod
    def _total_cards_value(player_or_dealer):
        total = 0
        for card in player_or_dealer.cards:
            if card.value == 'Ace':
                total += 11
            elif card.value in ['Jack', 'Queen', 'King']:
                total += 10
            else:
                total += int(card.value)

        ace_count = sum([1 for card in player_or_dealer.cards 
                            if card.is_ace()])

        while ace_count > 0 and total > 21:
            total -= 10
            ace_count -= 1

        return total

    def _display_results(self):
        player_total = self._total_cards_value(self._player)
        dealer_total = self._total_cards_value(self._dealer)
    
        self._display_player_cards()
        self._display_dealer_cards()
        print()

        if self._is_busted(self._player):
            print("You are busted!!! You lost!!!")
        elif self._is_busted(self._dealer):
            print("Dealer busted!!! You won!!!")
        elif player_total > dealer_total:
            print("You won!!!")
        elif dealer_total > player_total:
            print("Dealer won!!!")
        else:
            print("It's a tie.")

    @staticmethod
    def _display_goodbye_msg():
        print()
        print("Thanks for playing Twenty-One game. Goodbye!!!")

    @staticmethod
    def _play_again():
        prompt = "Do you want to play again? 'y' or 'n' "
        while True:
            print()
            answer = input(prompt).lower()
            if answer in ['y', 'n']:
                break
            print("Invalid choice. Please enter 'y' or 'n'.")
        
        return answer == 'y'
        
    def _reset_game(self):
        self._deck.reset()
        self._player.reset()
        self._dealer.reset()

game = TwentyOneGame()
game.play()
