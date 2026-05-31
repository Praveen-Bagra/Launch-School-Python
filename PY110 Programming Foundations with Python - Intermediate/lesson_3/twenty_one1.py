import random
import os

SUITS = ('H', 'D', 'S', 'C')
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10',
          'J', 'Q', 'K', 'A')
BUST_LIMIT = 21
DEALER_HIT_THRESHOLD = 17
GAMES_PER_MATCH = 5

def prompt(message):
    print(f'==> {message}')

def initialize_deck():
    new_deck = [f"{value}{suit}" for value in VALUES for suit in SUITS]
    random.shuffle(new_deck)
    return new_deck

def total(cards):
    sum_val = 0

    for card in cards:
        value = card[:-1]

        if value == 'A':
            sum_val += 11
        elif value in ['J', 'Q', 'K']:
            sum_val += 10
        else:
            sum_val += int(value)

    # Correct for Aces
    for card in cards:
        value = card[:-1]
        if sum_val <= BUST_LIMIT:
            break
        if value == 'A':
            sum_val -= 10

    return sum_val

def busted(hand_total):
    return hand_total > BUST_LIMIT

def detect_result(dealer_total, player_total):

    if player_total > BUST_LIMIT:
        return 'PLAYER_BUSTED'
    if dealer_total > BUST_LIMIT:
        return 'DEALER_BUSTED'
    if dealer_total < player_total:
        return 'PLAYER'
    if dealer_total > player_total:
        return 'DEALER'

    return 'TIE'

def display_end_of_game(dealer_cards_total, player_cards_total,
                            dealer_cards_, player_cards):

    print('==============')
    prompt(f"Dealer has {hand(dealer_cards)}, "
           f"for a total of: {dealer_cards_total}")
    prompt(f"Player has {hand(player_cards)}, "
           f"for a total of: {player_cards_total}")
    print('==============')

    result = detect_result(dealer_cards_total, player_cards_total)

    match result:
        case 'PLAYER_BUSTED':
            prompt('You busted! Dealer wins!')
        case 'DEALER_BUSTED':
            prompt('Dealer busted! You win!')
        case 'PLAYER':
            prompt('You win!')
        case 'DEALER':
            prompt('Dealer wins!')
        case _:
            prompt("It's a tie!")

def play_again():
    print("-------------")
    while True:
        prompt('Do you want to play again? (y or n) ')
        answer = input().strip().lower()

        if answer and answer[0] in ['y', 'n']:
            break
        prompt("Not a valid choice.")

    return answer[0] == 'y'

def pop_two_from_deck(hand_deck):
    return [hand_deck.pop(), hand_deck.pop()]

def hand(cards):
    return ', '.join(cards)

def display_game_rules():
    prompt('''
    1. It starts with a standard 52-card deck consisting of the 4 suits 
    (Hearts, Diamonds, Clubs, and Spades), and 13 values (2, 3, 4, 5, 
    6, 7, 8, 9, 10, Jack, Queen, King, Ace))

    2. The goal of Twenty-One is to try to get as close to 21 as 
    possible without going over. If you go over 21, it's a bust, 
    and you lose.

    3. The game consists of a dealer and a player. Both participants are 
    initially dealt a hand of two cards. The player can see their two 
    cards, but can only see one of the dealer's cards.

    4. All of the card values are pretty straightforward, except for the 
    Ace. The cards with numbers 2 through 10 are worth their face value. 
    The Jack, Queen, and King are each worth 10. The Ace can be worth 1 
    or 11 depending on circumstances. Its value is determined each time 
    a new card is drawn from the deck. For example, if the hand contains
    a 2, an Ace, and a 5, then the total value of the hand is 18. In 
    this case, the Ace is worth 11 because the sum of the hand 
    (2 + 11 + 5) doesn't exceed 21. 

    5. The player always goes first, and can decide to either hit or 
    stay. A hit means the player wants to be dealt another card. 
    Remember, if his total exceeds 21, he will bust and lose the game. 
    The decision to hit or stay depends on the player's cards and what 
    the player thinks the dealer has. For example, if the dealer is 
    showing a "10" (the other card is hidden), and the player has a "2" 
    and a "4", then the obvious choice is for the player to hit. 
    The player can continue to hit as many times as they want. The turn 
    is over when the player either busts or stays. If the player busts, 
    the game is over, and the dealer won.

    6. When the player stays, it's the dealer's turn. If the dealer 
    busts, then the player wins.

    7. When both the player and the dealer stay, it's time to compare 
    the total value of the cards and see who has the highest value.
    ''')

    continue_prompt()

def continue_prompt():
    prompt("Press enter to continue.")
    input()

def display_initial_messages():
        os.system('clear')
        prompt('Welcome to Twenty-One!')
        prompt(f"This match will consist of a series of {GAMES_PER_MATCH} "
               f"games. Tied games are replayed and don't count toward the " 
               f"{GAMES_PER_MATCH} game total. The player who wins " 
               f"the most games, will be declared the overall winner. ")

        while True:
            prompt("Do you want to see the game rules? "
                   "Press y or n.")
            answer = input().strip().lower()

            if answer and answer[0] in ['y', 'n']:
                break
            prompt("Not a valid choice.")

        if answer[0] == 'y':
            display_game_rules()
            

def display_score_line(total_games_played, total_player_wins, 
                        total_dealer_wins):
    prompt(f'Games played: {total_games_played}, ' 
           f'Player wins: {total_player_wins}, '
           f'Dealer wins: {total_dealer_wins}')
           
def play_game_and_return_winner(games_played, player_wins,
                                    dealer_wins):
    deck = initialize_deck()
    player_cards = pop_two_from_deck(deck)
    dealer_cards = pop_two_from_deck(deck)
    player_total = total(player_cards)
    dealer_total = total(dealer_cards)

    os.system('clear')
    display_score_line(games_played, player_wins, dealer_wins)
    prompt(f"Dealer had {dealer_cards[0]} and ?")
    prompt(f"You have: {player_cards[0]} and {player_cards[1]}, "
           f"for a total of {player_total}.")

    while True:
        prompt("Would you like to (h)it or (s)tay?")
        player_choice = input().strip().lower()
        if player_choice not in ['h', 's', 'hit', 'stay']:
            prompt("Sorry, must enter 'h' or 's'.")
            continue

        if player_choice in ['h', 'hit']:
            player_cards.append(deck.pop())
            player_total = total(player_cards)
            prompt('You chose to hit!')
            prompt(f'Your cards are now: {hand(player_cards)}')
            prompt(f'Your total is now: {player_total}')

        if player_choice in ['s', 'stay'] or busted(player_total):
                    break
        
    if busted(player_total):
        display_end_of_game(dealer_total, player_total, dealer_cards,
                            player_cards)
        return detect_result(dealer_total, player_total)

    prompt(f"You stayed at {player_total}")

    # dealer turn
    prompt("Dealer's turn...")

    while dealer_total < DEALER_HIT_THRESHOLD:
        prompt("Dealer hits!")
        dealer_cards.append(deck.pop())
        dealer_total = total(dealer_cards)
        prompt(f"Dealer's cards are now: {hand(dealer_cards)}"
               f", for a total of {dealer_total}.")

    if busted(dealer_total):
        prompt("Dealer busted!")
    else:
        prompt("Dealer stays!")

    # both player and dealer finished - compare cards!
    display_end_of_game(dealer_total, player_total, dealer_cards,
                            player_cards)
    
    return detect_result(dealer_total, player_total)

def twenty_one():
    while True:
        display_initial_messages()

        games_played = 0
        player_wins = 0
        dealer_wins = 0

        while games_played < GAMES_PER_MATCH:
            game_winner = play_game_and_return_winner(games_played,
                            player_wins, dealer_wins)

            if game_winner in ['PLAYER_BUSTED', 'DEALER']: 
                dealer_wins += 1
                games_played += 1
            elif game_winner in ['DEALER_BUSTED', 'PLAYER']:
                player_wins += 1
                games_played += 1

            if games_played != GAMES_PER_MATCH:
                continue_prompt()

        print()
        print('***********************************************************')
        prompt(f'Games played: {games_played}, Player wins: {player_wins}, '
            f'Dealer wins: {dealer_wins}')
        if player_wins > dealer_wins:
            prompt("You win the match!! Congratulations!!")
        else:
            prompt("Dealer wins the match!!")        
        print('***********************************************************')
        print()

        if not play_again():
            break

    prompt("Thank you for playing Twenty-One!!!")

twenty_one()