# Tic-tac-toe game
# By: Angel Gabriel Quintana
# Started: April 13 2020
# Last edited: April 15 2020    

# This program provides a text-based game of Tic Tac Toe
# One can play against someone or else or choose between computer players of 3 different difficulties
# When playing against the computer, the computer will play as X i.e. the computer will always go first
# The easy and medium CPUs could be repurposed to possibly play second or even on bigger boards,
# however, the hard CPU is coded in a very fixed way so it cannot play second. 

from random import randint
from time import sleep



# here is our board info: x starts
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
moves = []
turn = "X"

######################################################################################################################
# useful functions

# prints the current board
def print_board():
    print("%s|%s|%s" % (board[0], board[1], board[2]))
    print("-+-+-")
    print("%s|%s|%s" % (board[3], board[4], board[5]))
    print("-+-+-")
    print("%s|%s|%s" % (board[6], board[7], board[8]))

# prints the instructions on how to play
def print_instructions():
    print("Here is how to play the game:")
    sleep(2)
    print("\tYou'll be asked to input a number from 1 to 9 when it's your turn.")
    print("\tThese numbers are associated to the grid like so:\n")
    sleep(3)
    print("\t1|2|3")
    print("\t-+-+-")
    print("\t4|5|6")
    print("\t-+-+-")
    print("\t7|8|9\n")
    sleep(3)
    


# changes move to match chosen move (position goes from 0-8)
#   if move is invalid, board is unchanged and returns warning
def make_move(position):
    global turn
    if (position > 8 or position < 0):
        print("Hey! That's not in range! Try again.\n")
        return False
    elif board[position] != " ":
        print("Hey! That square is already taken! Try again.\n")
        return False
    else:
        if turn == "X":
            board[position] = "X"
            turn = "O"
        else:
            board[position] = "O"
            turn = "X"
        moves.append(position)
        return True


# checks if board is full
def is_board_full():
    if len(moves) == 9:
        return True
    return False

# checks for win on board
def is_there_a_win():
    # loop through rows
    for row in range(0,3):
        row *= 3
        if (board[row] == board[row + 1] == board[row + 2]) and (board[row] != " "):
            return True
    # loop through columns
    for col in range(0,3):
        if (board[col] == board[col + 3] == board[col + 6]) and (board[col] != " "):
            return True
    # check diagonals
    if ((board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6])) and (board[4] != " "):
        return True
    return False



######################################################################################################################
# here are the different CPUs


# returns a random move, thus it can play as "O" or "X"
# does NOT actually make the move
#   requires: board is not full, no one has won yet
def easy_ai():
    blank_spaces = []
    blank_count = 0
    index = 0
    for space in board:
        if space == " ":
            blank_count += 1
            blank_spaces.append(index)
        index += 1
    move_index = randint(0, blank_count - 1)
    return blank_spaces[move_index]

# returns a move that would complete a line on the board for the given player or -1 if there is no such move
# does NOT actually make the move
#   requires: board is not full, no one has won yet
def search_for_line(player):
    if board[0] == player:
        if board[1] == player and board[2] == " ":
            return 2
        elif board[2] == player and board[1] == " ":
            return 1
        elif board[4] == player and board[8] == " ":
            return 8
        elif board[8] == player and board[4] == " ":
            return 4
        elif board[3] == player and board[6] == " ":
            return 6
        elif board[6] == player and board[3] == " ":
            return 3
    if board[1] == player:
        if board[2] == player and board[0] == " ":
            return 0
        elif board[4] == player and board[7] == " ":
            return 7
        elif board[7] == player and board[4] == " ":
            return 4
    if board[2] == player:
        if board[4] == player and board[6] == " ":
            return 6
        elif board[6] == player and board[4] == " ":
            return 4
        elif board[5] == player and board[8] == " ":
            return 8
        elif board[8] == player and board[5] == " ":
            return 5
    if board[3] == player:
        if board[6] == player and board[0] == " ":
            return 0
        elif board[4] == player and board[5] == " ":
            return 5
        elif board[5] == player and board[4] == " ":
            return 4
    if board[4] == player:
        if board[5] == player and board[3] == " ":
            return 3
        elif board[6] == player and board[2] == " ":
            return 2
        elif board[7] == player and board[1] == " ":
            return 1
        elif board[8] == player and board[0] == " ":
            return 0
    if board[5] == player and board[8] == player and board[2] == " ":
        return 2
    if board[6] == player:
        if board[7] == player and board[8] == " ":
            return 8
        elif board[8] == player and board[7] == " ":
            return 7
    if board[7] == player and board[8] == player and board[6] == " ":
        return 6
    return -1

# returns an ok move (will look for wins and to block opponent, but otherwise random), can play as "O" or "X"
# does NOT actually make the move
#   requires: board is not full, no one has won yet
def medium_ai():
    if turn == "X":
        search_for_win = search_for_line("X")
        if search_for_win != -1:
            return search_for_win
        search_to_block = search_for_line("O")
        if search_to_block != -1:
            return search_to_block
    else: # it's O's turn
        search_for_win = search_for_line("O")
        if search_for_win != -1:
            return search_for_win
        search_to_block = search_for_line("X")
        if search_to_block != -1:
            return search_to_block
    return easy_ai()

# returns an UNBEATABLE move (based off Randall Munroe's Tic Tac Toe Comic)
# plays as "X", i.e. the first player
# does NOT actually make the move
#   requires: board is not full, no one has won yet
def hard_ai_x():
    not_blank = 0
    for space in board:
        if space != " ":
            not_blank += 1

    if not_blank == 0:
        return 0
    elif not_blank == 2:
        if moves[1] % 2 == 1:
            return 4
        elif moves[1] == 6 or moves[1] == 8:
            return 2
        elif moves[1] == 2:
            return 6
        else:
            return 8
    elif not_blank == 4:
        if moves[2] == 4:
            if moves[3] != 8:
                return 8
            elif moves[1] == 1 or moves[1] == 7:
                return 6
            else:
                return 2
        elif moves[2] == 2:
            if moves[3] != 1:
                return 1
            elif moves[1] == 6:
                return 8
            else:
                return 6
        elif moves[2] == 6:
            if moves[3] != 3:
                return 3
            else:
                return 8
        else:
            return 8 - moves[3]
    elif not_blank == 6:
        if moves[1] == 1:
            if moves[5] != 3:
                return 3
            else:
                return 2
        elif moves[1] == 2:
            if moves[5] != 7:
                return 7
            else:
                return 4
        elif moves[1] == 3:
            if moves[5] != 1:
                return 1
            else:
                return 6
        elif moves[1] == 5:
            if moves[5] != 1:
                return 1
            else:
                return 6
        elif moves[1] == 6:
            if moves[5] != 5:
                return 5
            else:
                return 4
        elif moves[1] == 7:
            if moves[5] != 3:
                return 3
            else:
                return 2
        elif moves[1] == 8:
            if moves[5] != 3:
                return 3
            else:
                return 4
        else:
            if moves[3] == 1 or moves[3] == 5:
                if moves[5] != 6:
                    return 6
                else:
                    return 2
            elif moves[3] == 2:
                if moves[5] != 3:
                    return 3
                else:
                    return 7
            elif moves[3] == 3 or moves[3] == 7:
                if moves[5] != 2:
                    return 2
                else:
                    return 6
            else:
                if moves[5] != 1:
                    return 1
                else:
                    return 5
    else:
        return 8 - moves[7]


######################################################################################################################


# resets the game
def reset():
    global board
    global moves
    global turn
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    moves = []
    turn = "X"
    

#############################################################################################################################
# main game 

print("Hi there! Welcome to Tic Tac Toe.\n")
print_instructions()

while True:
    print("\nYou are at the main menu.")
    print("\nNote: You may return to this menu from within a game by typing \"menu\".\n")
    print("Please select an option by pressing the corresponding number:")
    print("\t1. Instructions.")
    print("\t2. Play against a friend.")
    print("\t3. Play against the computer(easy).")
    print("\t4. Play against the computer(medium).")
    print("\t5. Play against the computer(hard).")
    print("Note: The Computer always goes first.")
    print("\t6. Quit.\n\n")

    player2 = "nothing"
    
    menu_choice = input()
    if menu_choice == "1":
        print_instructions()
        continue
    elif menu_choice == "2":
        player2 = "human"
    elif menu_choice == "3":
        player2 = "easy"
    elif menu_choice == "4":
        player2 = "medium"
    elif menu_choice == "5":
        player2 = "hard"
    elif menu_choice == "6":
        break
    else:
        print("Not a valid option!")
        continue

    reset()
    while True:
        print_board()
        print("It is %s's turn.\n" % turn)
        if turn == "O":
            x = input("Please select a number from 1 to 9.\n")
            if x == "menu":
                break
            try:
                x = int(x) 
                move_val = make_move(x - 1)
            except ValueError:
                print("Hey! That's not a number! Try again.\n")
                continue
            if move_val == False:
                continue
        else:
            if player2 == "human":
                x = input("Please select a number from 1 to 9.\n")
                if x == "menu":
                    break
                try:
                    x = int(x) 
                    move_val = make_move(x - 1)
                except ValueError:
                    print("Hey! That's not a number! Try again.\n")
                    continue
                if move_val == False:
                    continue
            else:
                print("Thinking...\n")
                sleep(1)
                if player2 == "easy":
                    make_move(easy_ai())
                elif player2 == "medium":
                    make_move(medium_ai())
                else:
                    make_move(hard_ai_x())
        if is_there_a_win() == True:
            if turn == "X":
                print_board()
                if player2 == "human":
                    print("Congrats! O wins!\n")
                elif player2 == "easy" or player2 == "medium":
                    print("Congrats! You win!\n")
                else:
                    print("Impossible! The Hard CPU has no weaknesses!!!\n")
            else:
                print_board()
                if player2 == "human":
                    print("Congrats! X wins!\n")
                elif player2 == "easy":
                    print("Congrats! You lost to the easy computer!\n")
                elif player2 == "medium":
                    print("Oh no, you lost. Better luck next time!\n")
                else:
                    print("Oh no, you lost. It's ok, it was the hard difficulty after all.\n")
            break
        elif is_board_full() == True:
            print_board()
            print("It's a Tie!\n")
            break
    print("\nBack to the menu...\n")
    sleep(3)

print("Thanks for playing my game! <3 <3")
