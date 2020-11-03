from termcolor import colored
import numpy as np

board = np.zeros((20, 10))


def init_board(enter_board):
    global board
    board = enter_board

def print_current_board():
    print_board(board)


def print_board(game_board, start=0):
    print("BOARD=============")
    # print(game_board)
    for row in range(start, 20):
        for col in range(10):
            number = game_board[row][col]
            if number == 0:
                print(colored(0, 'grey'), end='')
            if number == 1:
                print(colored(0, 'white'), end='')
            if number == 2:
                print(colored(0, 'red'), end='')
        print('')

