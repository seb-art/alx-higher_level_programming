#!/usr/bin/python3
'''Challenge of placing N non-attacking queens on an NxN chessboard'''
import sys


def nqueens(n):
    '''class: a program that solves the N queens problem'''

    # n must be type int
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    # n must be an integer greater or equal to 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # game schemas
    chess_board = [-1] * n
    moves = []

    def move_queen(row, col):
        '''game schemas, place queen on board'''

        for i in range(row):
            if chess_board[i] == col or \
               chess_board[i] - i == col - row or \
               chess_board[i] + i == col + row:
                return False
        return True

    def backtrack(row):
        '''
        game schemas, arrangements of questions
        and valid solution using bactracking
        '''

        if row == n:
            moves.append(list(enumerate(chess_board)))
        else:
            for col in range(n):
                if move_queen(row, col):
                    chess_board[row] = col
                    backtrack(row+1)

    backtrack(0)
    return moves


# execute plays and commandline
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    moves = nqueens(n)
    for m in moves:
        print([list(i) for i in m])
