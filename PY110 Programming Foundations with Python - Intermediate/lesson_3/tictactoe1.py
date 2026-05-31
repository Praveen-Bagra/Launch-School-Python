import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
GAMES_TO_WIN_MATCH = 5
WINNING_LINES = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9], # columns
    [1, 5, 9], [3, 5, 7]             # diagonals
]

def display_board(board, computer_wins, player_wins):
    os.system('clear')

    prompt(f'You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.')
    prompt(f'Current Score:- Player: {player_wins}, '
           f'Computer: {computer_wins}')
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}')
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def prompt(message):
    print(f'==> {message}')

def empty_squares(board):
    return [key for key, value in board.items() 
                if value == INITIAL_MARKER]

def player_chooses_square(board):

    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f'Choose a square ({join_or(valid_choices)}):')
        square = input().strip()
        if square in valid_choices:
            break
        
        prompt("Sorry, that's not a valid choice.")
            
    board[int(square)] = HUMAN_MARKER

def find_threat_or_opportunity(board, marker):
    for winning_line in WINNING_LINES:
        line_markers = [board[sq] for sq in winning_line]
        if ((line_markers.count(marker) == 2) and
              (line_markers.count(INITIAL_MARKER) == 1)):
            return [sq for sq in winning_line 
                       if board[sq] == INITIAL_MARKER][0] 
    return None


def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return

    square = None
    
    square = find_threat_or_opportunity(board, COMPUTER_MARKER) 
    # attack first

    if square is None:
        square = find_threat_or_opportunity(board, HUMAN_MARKER) 
        # then defend

    if square is None and 5 in empty_squares(board):
        square = 5 # Choose 5 if available

    if square is None:        
        square = random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
            return 'Computer'
    
    return None

def join_or(lst, delimiter1=', ', delimiter2='or'):
    if len(lst) == 0:
        return ''
    elif len(lst) == 1:
        return f'{lst[0]}' 
    elif len(lst) == 2:
        return f'{lst[0]} {delimiter2} {lst[1]}'
    else:
        new_string = ''
        for element in lst[:-1]:
            new_string += str(element) + delimiter1
        return f'{new_string}{delimiter2} {lst[-1]}'

def choose_square(board, current_player):
    if current_player == 'Player':
        player_chooses_square(board)
    elif current_player == 'Computer':
        computer_chooses_square(board)

def alternate_player(current_player):
    if current_player == 'Computer':
        return 'Player'
    elif current_player == 'Player':
        return 'Computer'


def play_tic_tac_toe():

    while True:
        player_wins = 0
        computer_wins = 0

        prompt(f"We are playing a match to win {GAMES_TO_WIN_MATCH} "
               f"games. Whosoever wins {GAMES_TO_WIN_MATCH} games first, "
               f"wins. If game results in a tie, it won't be counted.")
        prompt("Are you ready for a match? Press any key to continue.")
        input()
           
        while True:
            prompt("Who do you want to go first? "
                   "Enter 'p' for player and 'c' for computer.")
            current_player = input().strip().lower()
            if current_player in ['p', 'c', 'player', 'computer']:
                break
            else:
                prompt("Not a valid choice.")

        if current_player in ['p', 'player']:
            current_player = 'Player'
        elif current_player in ['c', 'computer']:
            current_player = 'Computer'

        while True:
            board = initialize_board()

            while True:
                display_board(board, computer_wins, player_wins)
                choose_square(board, current_player)
                current_player = alternate_player(current_player)
                if someone_won(board) or board_full(board):
                    break

            display_board(board, computer_wins, player_wins)

            winner = detect_winner(board)

            if someone_won(board):
                prompt(f'{winner} won the game!')
                if winner == 'Player':
                    player_wins += 1
                else:
                    computer_wins += 1
            else:
                prompt("It's a tie!")

            prompt(f'Current Score:- Player: {player_wins}, '
                   f'Computer: {computer_wins}')

            if player_wins == GAMES_TO_WIN_MATCH:
                prompt("Player won the match!!")
                break 
            elif computer_wins == GAMES_TO_WIN_MATCH:
                prompt("Computer won the match!!")
                break    

            prompt("Ready for another game? Press any key to continue")
            input()

        while True:
            prompt('Play another match? (y or n)')
            answer = input().strip().lower()

            if answer and answer[0] in 'yn':
                break
            else:
                prompt('Not a valid choice.')

        if answer[0] == 'n':
            break

    prompt('Thanks for playing Tic Tac Toe')

play_tic_tac_toe()