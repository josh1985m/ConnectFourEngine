import numpy as np
import pygame
import sys
def create_board():
    board = np.zeros((ROW_COUNT, COL_COUNT))
    return board

ROW_COUNT = 6
COL_COUNT = 7

game_over = False
row = 0
turn = 0
turn_count = 1
board = create_board()

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT + 1):
        if board[r][col] == 0:
            return r

def show_board(board):
    print(np.flip(board, 0))
    #print(board)

def check_down():
    if board[row][col] == board[row - 1][col] == board[row - 2][col] == board[row - 3][col]:
        return True
    else:
        return False

def right_main():
    if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3]:
        return True
    else:
        return False
def right_sub_1():
    if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col - 1]:
        return True
    else:
        return False

def right_sub_2():
    if board[row][col] == board[row][col - 1] == board[row][col - 2] == board[row][col + 1]:
        return True
    else:
        return False

def left_main():
    if board[row][col] == board[row][col - 1] == board[row][col - 2] == board[row][col - 3]:
        return True
    else:
        return False

def left_sub_1():
    if board[row][col] == board[row][col - 1] == board[row][col - 2] == board[row][col + 1]:
        return True
    else:
        return False

def left_sub_2():
    if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col - 1]:
        return True
    else:
        return False

def back_diag_main():
    if board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2] == board[row + 3][col - 3]:
        return True
    else:
        return False

def back_diag_main_2():
    if board[row][col] == board[row - 1][col +1] == board[row - 2][col + 2] == board[row - 3][col + 3]:
        return True
    else:
        return False

def back_diag_sub_1():
    if board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2] == board[row - 1][col + 1]:
        return True
    else:
        return False

def back_diag_sub_2():
    if board[row][col] == board[row + 1][col - 1] == board[row - 1][col + 1] == board[row - 2][col + 2]:
        return True
    else:
        return False

def forw_diag_main():
    if board[row][col] == board[row + 1][col +1] == board[row + 2][col + 2] == board[row + 3][col + 3]:
        return True
    else:
        return False

def forw_diag_main_2():
    if board[row][col] == board[row - 1][col - 1] == board[row - 2][col - 2] == board[row - 3][col - 3]:
        return True
    else:
        return False

def forw_diag_sub_1():
    if board[row][col] == board[row - 1][col - 1] == board[row - 2][col - 2] == board[row + 1][col + 1]:
        return True
    else:
        return False

def forw_diag_sub_2():
    if board[row][col] == board[row - 1][col - 1] == board[row + 1][col + 1] == board[row + 2][col + 2]:
        return True
    else:
        return False

def check_mains():
    try:
        if check_down():
            return True
        elif back_diag_main():
            return True
        elif back_diag_main_2():
            return True
        elif forw_diag_main():
            return True
        elif forw_diag_main_2():
            return True
    except IndexError:
        return False

def check_subs():
    try:
        if right_sub_1():
            return True
        elif right_sub_2():
            return True
        elif left_sub_1():
            return True
        elif left_sub_2():
            return True
        elif forw_diag_sub_1():
            return True
        elif forw_diag_sub_2():
            return True
        elif back_diag_sub_1():
            return True
        elif back_diag_sub_2():
            return True
    except IndexError:
        return False

def check_left():
    try:
        if left_main():
            return True
    except IndexError:
        return False

def check_right():
    try:
        if right_main():
            return True
    except IndexError:
        return False

def winning_move():
    if turn_count >= 7:
        if check_subs():
            return True
        elif check_mains():
            return True
        elif check_down():
            return True
        elif check_right():
            return True
        elif check_left():
            return True
        else:
            return False
def

pygame.init()
SQUARESIZE = 100
width = COL_COUNT * SQUARESIZE
height = ROW_COUNT * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn == 0:
                col = int(input("Player 1 make your selection (0-6): "))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
                    show_board(board)
                    if winning_move():
                        print("You win! Player 1!")
                        print("Would you like to play again?")
                        new_game = input(print("y for yes : n to quit"))
                        if new_game == 'y':
                            game_over == False
                            board = create_board()
                            turn == 0
                            continue
                        else:
                            break

            else:
                player = 2
                col = int(input("Player 2 make your selection (0-6): "))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)
                    show_board(board)
                    if winning_move():
                        print("You win Player 2!")
                        print("Would you like to play again?")
                        new_game = input(print("y for yes : n to quit"))
                        if new_game == 'y':
                            print("Player 2 goes first this round")
                            game_over == False
                            board = create_board()
                            turn == 0
                            continue
                        else:
                            break

            turn += 1
            turn = turn % 2
            turn_count = turn_count + 1
        exit()
