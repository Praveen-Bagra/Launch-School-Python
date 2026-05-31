# Tic Tac Toe is a 2-player game played on a 3x3 grid called the board.
# Each player takes a turn and marks a square on the board. The first
# player to get 3 squares in a row -- horizontally, vertically, or 
# diagonally -- wins. If all 9 squares are filled and neither player has
# 3 in a row, the game ends in a tie.

#  1. Display the initial empty 3x3 board.
#  2. Ask the user to make a square.
#  3. Computer makes a square.
#  4. Display the updated board state.
#  5. If it's a winning board, display the winner.
#  6. If the board is full, display tie.
#  7. If neither player won and the board is not full, go to # 2
#  8. Play again?
#  9. If yes, go to #1
# 10. Goodbye! 

import random
import pdb

def display_board(choices):
    empty_line = '   |   |   '
    dotted_line = '-----------'
    print(empty_line)
    print(f' {choices[0]} | {choices[1]} | {choices[2]} ')
    print(empty_line)
    print(dotted_line)
    print(empty_line)
    print(f' {choices[3]} | {choices[4]} | {choices[5]} ')
    print(empty_line)
    print(dotted_line)
    print(empty_line)
    print(f' {choices[6]} | {choices[7]} | {choices[8]} ')
    print(empty_line)

def return_winner_or_tie(choices):
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                        [1, 4 , 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    for winning_combination in winning_combinations:
        if all([choices[element] == 'X' for element in winning_combination]):
            return 'You'
        elif all([choices[element] == 'O' for element in winning_combination]):
            return 'Computer'

    if ' ' not in choices:
        return 'Tie'

def display_winner_or_tie(choices):
    if return_winner_or_tie(choices) == 'You':
        display_board(choices)
        print('You win!!')
    elif return_winner_or_tie(choices) == 'Computer':
        display_board(choices)
        print('Computer wins!!')
    elif return_winner_or_tie(choices) == 'Tie':
        display_board(choices)
        print("It's Tie.")

print()
print('-'* 24)
print('Welcome to Tictaetoe!!!')
print('-'* 24)
print()

while True:
    choices = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    valid_choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    while True:

        if all([element == ' ' for element in choices]):
            print('Please make a choice from 1 to 9 as suggested below:')
            display_board(valid_choices)
        else:
            print(f'Please make a choice from {', '.join(valid_choices)}')

        while True:
            choice = input()
            if choice in valid_choices:
                choices[int(choice) - 1] = 'X'
                break
            else:
                print("Not a valid choice. Please try again.")
                print(f'Valid choice should be from {', '.join(valid_choices)}')

        display_winner_or_tie(choices)
        if return_winner_or_tie(choices):
            break

        valid_choices.remove(choice)
        computer_choice = random.choice(valid_choices) 
        choices[int(computer_choice) - 1] = 'O'
        valid_choices.remove(computer_choice)

        print(f'You choose {choice}. Computer choose {computer_choice}')

        display_winner_or_tie(choices)
        if return_winner_or_tie(choices):
            break

        display_board(choices)

    print('Do you want to play again? y/n')
    answer = input()
    if answer.lower().startswith('n'):
        break

print("Thank you playing TicTacToe. Hope you enjoyed it!!!")


