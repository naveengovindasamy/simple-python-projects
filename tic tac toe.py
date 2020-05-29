#Implementation of two player Tic-Tac-Toe game in Python

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' '}
board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

#main

def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("it's your turn," + turn + ".Move to which place?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("that place is already filled.\nMove to which place?")
            continue

        #checking player X or O has won,for every move after 5 moves.

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': #across the top
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break

            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': #across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break

            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': #across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break

            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': #down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break

            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': #down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break

            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': #down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break

            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': #diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break

            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': #diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break

            # if neither X nor O wins and the board is full,we'll declare the result as ;tie'

        if count == 9:
                print("\nGame Over.\n")
                print("it's a Tie!!!")

            #now we have to change the player after every move.

        if turn =='X':
                turn = 'O'
        else:
                turn = 'X'

            #want to restart or not

    restart = input("do you want to play agin?(y/n)")
    if restart == "y" or restart == "y":
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()












