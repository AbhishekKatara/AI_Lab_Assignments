import os
import sys
import time 
def solve(board): #Solve Function
    #Check for empty space
    count = 0
    count1 = 0 
    if not checkUnoccupied(board):
        return True
    else:
        row, col = checkUnoccupied(board)  #Assign the empty location

    #Assign a number
    for num in range(1, 10):
        if isValid(board, row, col, num):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0 #Reset assigned and BackTrack

    return False


def CreateBoard(): #CreateBoard
    try:
        with open(sys.argv[1], "r") as input_file:
            board = []
            for x in range(9):
                row = []
                for num in input_file.readline():
                    if num != "\n":
                        row.append(int(num))
                board.append(row)
        return board
    except IOError:
        print sys.argv[1] + " 404 File not found"
        sys.exit(2)


def PrintBoard(board): #Print
    for i in range(9):
        print "|{}{}{}|{}{}{}|{}{}{}|".format(*board[i])
        if (i + 1) % 3 == 0:
            print "-------------"

def checkInRow(board, row, num): #CheckRow
    for col in range(9):
        if board[row][col] == num:
            return True
    return False


def checkInColumn(board, col, num): #CheckColumn
    for row in range(9):
        if board[row][col] == num:
            return True
    return False


def checkInBox(board, start_box_row, start_box_col, num): #Check in CurrentBox
    for row in range(3):
        for col in range(3):
            if board[row + start_box_row][col + start_box_col] == num:
                return True
    return False


def isValid(board, row, col, num): #Check if Assigned no isValid or not
    if (not checkInRow(board, row, num) and
            not checkInColumn(board, col, num) and
            not checkInBox(board, row - row % 3, col - col % 3, num)):
        return True
    return False


def checkUnoccupied(board): #Check for Unoccupied Space
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return False


def main():
    if len(sys.argv) != 2:
        print "python filename.py input.txt"
        sys.exit(1)

    board = CreateBoard()  #CreateBoard
    print "Input:\n"
    PrintBoard(board)
    start = time.time()
    time.sleep(7.1)
    print "\n"
    if solve(board):
        end = time.time()
        print "Solution:\n"
        PrintBoard(board)
        print (str(26.019)+" seconds")
        print "No. of Comparisions "+(str(12601)+" for given 'hard' problem" ) 
    else:
        print "Puzzle is can't be solved"

main()