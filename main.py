import time
import random

game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]

on = True

def display_game_board():
    print("\n")
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2] + "     1 | 2 | 3")
    print("---------")
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5] + "     4 | 5 | 6")
    print("---------")
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8] + "     7 | 8 | 9")
    print("\n")

def play_game():
    x()
    o()

def check_winner():
    if game_board[0] == game_board[1] == game_board[2] != '-':
        print(f'{game_board[0]} is the winner')
        return True
    if game_board[3] == game_board[4] == game_board[5] != '-':
        print(f'{game_board[3]} is the winner')
        return True
    if game_board[6] == game_board[7] == game_board[8] != '-':
        print(f'{game_board[6]} is the winner')
        return True
    if game_board[0] == game_board[3] == game_board[6] != '-':
        print(f'{game_board[0]} is the winner')
        return True
    if game_board[1] == game_board[4] == game_board[7] != '-':
        print(f'{game_board[1]} is the winner')
        return True
    if game_board[2] == game_board[5] == game_board[8] != '-':
        print(f'{game_board[6]} is the winner')
        return True
    if game_board[0] == game_board[4] == game_board[8] != '-':
        print(f'{game_board[0]} is the winner')
        return True
    if game_board[2] == game_board[4] == game_board[6] != '-':
        print(f'{game_board[2]} is the winner')
        return True
    if '-' not in game_board:
        print('Game Draw!')
        return True


def x():
    display_game_board()
    if check_winner():
        exit(0)
    print("X's Turn")
    a = input("Enter the position where you want to put your X:")
    if a not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Enter correct position")
        time.sleep(1.5)
        x()
    elif game_board[int(a)-1] != '-':
        print("Enter correct position")
        time.sleep(1.5)
        x()
    else:
        game_board[int(a) - 1] = "X"
        display_game_board()

def o():
    display_game_board()
    if check_winner():
        exit(0)
    b = random.randint(0, 9)
    if game_board[int(b)-1] != '-':
         time.sleep(1.5)
         o()
    else:
        game_board[int(b) - 1] = "0"
        display_game_board()

while on:
    play_game()






