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
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # if 0 then X if 1 then  O
    current_guy = 0
    for row in board:
        for element in row:
            if element==X:
                current_guy= current_guy+1
            elif element==O:
                current_guy = current_guy-1
    if current_guy==0:
        return X
    else:
        return O

    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return_list = []
    for i,row in enumerate(board):
        for j,element in enumerate(row):
            if element==EMPTY:
                return_list.append((i,j))
    return return_list


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    current_player = player(board)
    i = action[0]
    j = action[1]
    if board[i][j]!= EMPTY:
        raise ValueError
    else:
        second_board = [[],[],[]]
        for ik,row in enumerate(board):
            for element in row:
                second_board[ik].append(element)
        second_board[i][j] = current_player
        return second_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check the rows first
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][0]==board[i][2]:
            return board[i][0]
    # check columns
    for j in range(3):
        if board[0][j]==board[1][j] and board[0][j]==board[2][j]:
            return board[0][j]
    #check diagonals
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]
    if board[1][1] == board[2][0] and board[1][1] == board[0][2]:
        return board[1][1]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #check if someone won
    if winner(board)== X or winner(board)==O:
        return True
    else:
        #check if any elememt is None
        for row in board:
            for element in row:
                if element==EMPTY:
                    return False    
        return True
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #basically winner
    check = winner(board)
    if check==X:
        return 1
    elif check==O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        cur_player = player(board)
        possible_moves = actions(board)
        move_chosen = (0,0)
        final = 0
        if cur_player == X:
            final = -2
        else:
            final = 2
        for move in possible_moves:
            res = result(board,move)
            check = final_result(res)
            if cur_player == X:
                if check > final:
                    move_chosen = move
                    final = check
                    if check==1:
                        break
            elif cur_player == O:
                if check<final:
                    move_chosen = move
                    final = check
                    if check==-1:
                        break
        return move_chosen


#takes a board, adn tells 1 if X wins, -1 if O wins, and 0 if draw
def final_result(board):
    if terminal(board):
        return utility(board)
    else:
        move = minimax(board)
        return final_result(result(board,move))