# 1. Initialize deck
# 2. Deal cards to player and dealer
# 3. Player turn: hit or stay
#       - repeat until bust or stay
# 4. If player bust, dealer wins.
# 5. Dealer turn: hit or stay
#       - repeat until total >= 17
# 6. If dealer busts, player wins.
# 7. Compare cards and declare winner.

import random
import os

def initialize_deck():
    deck ={}
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    ranks = ['2', '3','4', '5', '6', '7', '8', '9', '10', 'Jack',
             'Queen', 'King', 'Ace']

    for suit in suits:
        for rank in ranks:
            card_description = f'{rank} of {suit}'

            if rank == 'Ace':
                deck[card_description] = 11
            elif rank in ['Jack', 'Queen', 'King']:
                deck[card_description] = 10
            else:
                deck[card_description] = int(rank)

    return deck

DECK = initialize_deck()

def deal_cards(deck, number_of_cards):
    cards = []

    for _ in range(number_of_cards):
        card = random.choice(list(deck))
        cards.append(card)
        del deck[card]

    return cards

def prompt(message):
    print(f'==> {message}')

def join_or(lst, delimiter1=', ', delimiter2='and'):
    if len(lst) == 0:
        return ''
    if len(lst) == 1:
        return f'{lst[0]}'
    if len(lst) == 2:
        return f'{lst[0]} {delimiter2} {lst[1]}'
    if len(lst) > 2:
        new_string = ''
        for element in lst[:-1]:
            new_string += str(element) + delimiter1
        return f'{new_string}{delimiter2} {lst[-1]}'

    return None

def total(cards):

    cards_values = [DECK[card] for card in cards]
    total_sum = sum(cards_values)
    ace_count = cards_values.count(11)

    while total_sum > 21 and ace_count > 0:
        total_sum -= 10
        ace_count -= 1

    return total_sum

def busted(total_sum):
    return total_sum > 21

def dealer_hit(dealer_cards, deck):
    while total(dealer_cards) < 17:
        dealer_cards += deal_cards(deck, 1)

def display_winner(player_total, dealer_total):
    if player_total > dealer_total:
        prompt("Player won.")
    elif player_total < dealer_total:
        prompt("Dealer won.")
    else:
        prompt("It's a tie.")


def twenty_one():
    while True:
        os.system('clear')
        deck = DECK.copy()
        player_cards = deal_cards(deck, 2)
        dealer_cards = deal_cards(deck, 2)
        prompt(f'Dealer has: {dealer_cards[0]} and unknown card.')

        while True:
            prompt(f'You have: {join_or(player_cards)}.')

            while True:
                prompt("Do you want to stay or hit? "
                    "Press 'h' for hit and 's' for stay")
                choice = input().strip().lower()
                if choice in ['h', 's', 'hit', 'stay']:
                    break
                prompt("Invalid choice.")

            player_busted = False
            if choice in ['h', 'hit']:
                player_cards += deal_cards(deck, 1)
                player_total = total(player_cards)
                if busted(player_total):
                    prompt("You are busted. Dealer won.")
                    prompt(f'You have: {join_or(player_cards)}.')
                    prompt(f'Dealer has: {join_or(dealer_cards)}')
                    player_busted = True
                    break
            elif choice in ['s', 'stay']:
                break

        if player_busted is False:
            dealer_hit(dealer_cards, deck)
            dealer_total = total(dealer_cards)

            if busted(dealer_total):
                prompt(f"Dealer has: {join_or(dealer_cards)}")
                prompt("Dealer busted. You won.")
            else:
                prompt(f"Dealer has: {join_or(dealer_cards)}")
                player_total = total(player_cards)
                display_winner(player_total, dealer_total)

        while True:
            prompt("Play another match? (y or n)")
            answer = input().strip().lower()

            if answer and answer[0] in ['y', 'n']:
                break

            prompt("Invalid choice.")

        if answer.startswith('n'):
            break

    prompt("Thanks for playing Twenety-One!!")

twenty_one()
