"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[X, EMPTY, X],
            [O, O, EMPTY],
            [X, O, O]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_x = 0
    num_o = 0

    for row in board:
        for col in row:
            if col == X:
                num_x += 1
            elif col == O:
                num_o += 1

    return O if num_o < num_x else X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == EMPTY:
                actions.append((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board[action[0]][action[1]] = player(board)
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2]:
        return board[2][0]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) != None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return 1 if winner(board) == X else -1 if winner(board) == O else 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

#  print(player(initial_state()))
#  print(actions(initial_state()))
#  print(result(initial_state(), (0,0)))
print(winner(initial_state()))
print(terminal(initial_state()))
print(utility(initial_state()))
