#IMPORTS

from IPython.display import clear_output



#METHOD DECLARATIONS

def clear_screen():

    for x in range(0,101):
        print('\n')
    clear_output()


def print_board(move_map):

    row0  = ('        |         |        ')
    row1  = ('        |         |        ')
    row2  = ('        |         |        ')
    row3  = ('--------|---------|--------')
    row4  = ('        |         |        ')
    row5  = ('        |         |        ')
    row6  = ('        |         |        ')
    row7  = ('--------|---------|--------')
    row8  = ('        |         |        ')
    row9  = ('        |         |        ')
    row10 = ('        |         |        ')

    board = [row0,row1,row2,row3,row4,row5,row6,row7,row8,row9,row10]

    board[1] = update_row(move_map[0:3], board[1])
    board[5] = update_row(move_map[3:6], board[5])
    board[9] = update_row(move_map[6:9], board[9])

    for row in board:
        print(row)


def update_row(move_map, board_row):

    board_row_listed = list(board_row)

    board_row_listed[3] = move_map[0]
    board_row_listed[13] = move_map[1]
    board_row_listed[23] = move_map[2]

    board_rejoined = ''.join(board_row_listed)

    return board_rejoined


def update_map(move_map, square, symbol):

    if move_map[square-1] == ' ':
        move_map[square-1] = symbol
    return(move_map)


def check_move_legality(move_map, square):

    for test_val in range(1,10):
        if square == str(test_val):
            if move_map[int(square)-1] == ' ':
                return True
            else:
                break

    return False


def check_win(move_map, symbol):

    if check_three(move_map, symbol):
        return True
    else:
        return False


def check_stalemate(mvoe_map):
    if ' ' not in move_map:
        print("It's a stalemate!")
        return True

    return False


def check_three(move_map, symbol):

    three = [False]*8

    three[0] = move_map[0] == move_map[1] == move_map[2] == symbol
    three[1] = move_map[3] == move_map[4] == move_map[5] == symbol
    three[2] = move_map[6] == move_map[7] == move_map[8] == symbol

    three[3] = move_map[0] == move_map[3] == move_map[6] == symbol
    three[4] = move_map[1] == move_map[4] == move_map[7] == symbol
    three[5] = move_map[2] == move_map[5] == move_map[8] == symbol

    three[6] = move_map[0] == move_map[4] == move_map[8] == symbol
    three[7] = move_map[2] == move_map[4] == move_map[6] == symbol

    for win in three:
        if win == True:
            return True

    return False



#INITIALISATION

move_map = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
game_on = True

user_input = ''



#EXECUTION

print('Tic Tac Toe')
print('Make your move by selecting the squares 1-9')
print('Left to right, top to bottom')

while user_input != 'y' and user_input != 'n':
    user_input = input('Ready to play? (y/n)')

if user_input == 'y':
    game_on = True
else:
    game_on = False

user_input = ''

while game_on == True:

    if game_on == True:

        clear_screen()
        print_board(move_map)
        move = input('Player 1 move')

        while check_move_legality(move_map, move) == False:
                move = input('Illegal move, enter another move')

        move = int(move)
        move_map = update_map(move_map, move, 'X')

        if check_win(move_map, 'X'):
            clear_screen()
            print_board(move_map)
            print('Player 1 has won!')
            game_on = False
        elif check_stalemate(move_map):
            clear_screen()
            print_board(move_map)
            print('Stalemate')
            game_on = False

    if game_on == True:

        clear_screen()
        print_board(move_map)
        move = input('Player 2 move')

        while check_move_legality(move_map, move) == False:
                move = input('Illegal move, enter another move')

        move = int(move)
        move_map = update_map(move_map, move, 'O')

        if check_win(move_map, 'O'):
            clear_screen()
            print_board(move_map)
            print('Player 2 has won!')
            game_on = False
        elif check_stalemate(move_map):
            clear_screen()
            print_board(move_map)
            print('Stalemate')
            game_on = False

    if game_on == False:

        while user_input != 'y' and user_input != 'n':
            user_input = input('Another game? (y/n)')

            if user_input == 'n':
                break
            elif user_input == 'y':
                game_on = True
                move_map = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
                print_board(move_map)
                clear_screen()

        user_input = ''
