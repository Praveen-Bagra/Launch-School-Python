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

    def is_face_card(self):
        return self.value in ['Jack', 'Queen', 'King']

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

class Hand:
    def __init__(self):
        self._cards = []

    def add_a_card(self, card):
        self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def get_first_card(self):
        if not self.is_empty():
            return self._cards[0]

        return None
        
    def is_empty(self):
        return len(self._cards) == 0

    def value(self):
        total = 0
        for card in self.cards:
            if card.is_ace():
                total += 11
            elif card.is_face_card():
                total += 10
            else:
                total += int(card.value)

        ace_count = sum([1 for card in self.cards
                            if card.is_ace()])

        while ace_count > 0 and total > 21:
            total -= 10
            ace_count -= 1

        return total

    def is_busted(self):
        return self.value() > 21

class Participant:
    def __init__(self):
        self.reset_hand()

    def reset_hand(self):
        self._hand = Hand()

    def hand(self):
        return list(self._hand.cards)

    def hand_value(self):
        return self._hand.value()

    def is_busted(self):
        return self._hand.is_busted()
    
    def hand_summary(self):
        return (f'{join_and(self.hand())} with '
              f'a total of {self.hand_value()}.')

    def deal_a_card(self, deck): 
        card = deck.get_a_card()
        self._hand.add_a_card(card)

    def deal_two_cards(self, deck):
        for _ in range(2):
            self.deal_a_card(deck)

class Player(Participant):
    INITIAL_AMOUNT = 5
    BROKE_AMOUNT = 0
    RICH_AMOUNT = 10

    def __init__(self):
        self.reset_purse()
        super().__init__()

    def display_cards(self):
        print(f'You have {self.hand_summary()}')

    def take_turn(self, deck):
        while True: 
            player_choice = self._get_choice()
            if player_choice.startswith('h'):
                self.deal_a_card(deck)
                if self.is_busted():
                    return
                
                clear_screen()
                print("You choose to hit.")
                self.display_cards()
                continue

            print("You choose to stay.")
            print()
            return

    def reset_purse(self):
        self._purse = Player.INITIAL_AMOUNT 

    def is_broke(self):
        return self._purse <= Player.BROKE_AMOUNT

    def is_rich(self):
        return self._purse >= Player.RICH_AMOUNT

    @staticmethod
    def _get_choice():
        print()
        prompt = "Do you want to hit(h) or stay(s)? "
        while True:
            answer = input(prompt).lower()
            if answer in ['h', 's', 'hit', 'stay']:
                break
            print()
            print("Invalid choice. Please enter 'h' or 's'.")

        print()
        return answer

    def display_purse(self):
        print(f"You currently have ${self._purse}.")

    def increment_purse(self):
        self._purse += 1

    def decrement_purse(self):
        self._purse -= 1

class Dealer(Participant):
    def get_first_card(self):
        return self._hand.get_first_card()

    def display_cards(self):
        print(f'Dealer has {self.hand_summary()}') 

    def take_turn(self, deck):
        clear_screen()
        print("Dealer turn...")
        print()
        while self.hand_value() < 17:
            print("Dealer hits.")
            self.deal_a_card(deck)
            self.display_cards()
            print()

        if not self.is_busted():
            print("Dealer chose to stay.")
            print()

class TwentyOneGame:
    def __init__(self):
        self._player = Player()
        self._dealer = Dealer()
        self._deck = Deck()

    def play(self):
        clear_screen()
        self._display_welcome_msg()
    
        while True:
            self._play_match()    

            if not self._play_again():
                break
        
        self._display_goodbye_msg()

    def _play_match(self):
        while True:
            self._play_one_game()

            if self._player.is_broke() or self._player.is_rich():
                break

        self._display_match_results()
        self._reset_match()

    def _play_one_game(self):
        clear_screen()

        self._player.deal_two_cards(self._deck)
        self._dealer.deal_two_cards(self._deck)

        self._player.display_cards()
        self._display_dealer_first_card()

        self._player.take_turn(self._deck)

        if not self._player.is_busted():
            self._dealer.take_turn(self._deck)
            
        self._display_game_results()

        winner = self._determine_winner()
        self._update_player_purse(winner)
        self._player.display_purse() 

        self._reset_game()
        if not self._player.is_broke() and not self._player.is_rich():
            input("Ready for the next game. Press any key to continue...")

    @staticmethod
    def _display_welcome_msg():
        print("Welcome to Twenty-One Game. The goal of Twenty-One is to \n"
              "try to get as close to 21 as possible without going over. \n"
              "If you go over 21, it's a bust, and you lose.")
        print("Are you ready to play?")
        input("Press any key to continue...")

    def _display_dealer_first_card(self):
        print(f'Dealer has {self._dealer.get_first_card()} and '
              f'an unknown card.')

    def _display_game_results(self):
        player_total = self._player.hand_value()
        dealer_total = self._dealer.hand_value()
    
        self._player.display_cards()
        self._dealer.display_cards()
        print()

        if self._player.is_busted():
            print("You are busted!!! You lost!!!")
        elif self._dealer.is_busted():
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
        self._player.reset_hand()
        self._dealer.reset_hand()

    def _reset_match(self):
        self._player.reset_purse()

    def _display_match_results(self):
        print()
        if self._player.is_broke():
            print("You have become broke. You lost everything.")
        else:
            print("Congratulations!!! You have become rich.")

    def _update_player_purse(self, winner):
        if winner == 'player':
            self._player.increment_purse()
        elif winner == 'dealer':
            self._player.decrement_purse()

    def _determine_winner(self):
        player_total = self._player.hand_value()
        dealer_total = self._dealer.hand_value()

        if self._player.is_busted():
            return 'dealer'

        if self._dealer.is_busted():
            return 'player'  

        if player_total > dealer_total:
            return 'player'

        if dealer_total > player_total:
            return 'dealer'

        return None

game = TwentyOneGame()
game.play()