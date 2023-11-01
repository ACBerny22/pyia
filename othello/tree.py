import random
import copy

class Node: 
    def __init__(self, score, move, after_board):
        self.score = score
        self.move = move
        self.root_board = None
        self.after_board = after_board
        self.children = []

root = Node(0, [0,0], None)

# Function to check if a move is valid
def is_valid_move(board, row, col, player):
    if board[row][col] != ' ':
        return False
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    opponent = 'O' if player == 'X' else 'X'
    
    for dr, dc in directions:
        r, c = row, col
        r += dr
        c += dc
        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
                r += dr
                c += dc
            if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == player:
                return True
    return False

def get_all_valid_moves(board, player):
    print("Evaluated for player:", player)
    moves = []
    for i in range(8):
        for j in range(8):
            if is_valid_move(board, i, j, player):
                moves.append([i, j])
    return moves


def update_chips(board):
    xs = 0
    os = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'X':
                xs = xs + 1
            if board[i][j] == 'O':
                os = os + 1
    return xs, os


# Function to make a move
def make_move(board, row, col, player):
    if not is_valid_move(board, row, col, player):
        xs, os = update_chips(board)
        #print("Fichas X: ", xs)
        #print("Fichas O: ", os)
        return False, xs, os
    
    board[row][col] = player
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    opponent = 'O' if player == 'X' else 'X'
    
    for dr, dc in directions:
        r, c = row, col
        r += dr
        c += dc
        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
                r += dr
                c += dc
            if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == player:
                r -= dr
                c -= dc
                while r != row or c != col:
                    board[r][c] = player
                    r -= dr
                    c -= dc


    xs, os = update_chips(board)
    #print("Fichas X: ", xs)
    #print("Fichas O: ", os)
    return True, xs, os


def evaluate_move(board, row, col, player):
    # Create a copy of the board to validate moves without affecting the playing board
    board_copy = copy.deepcopy(board)
    sike, xs, os = make_move(board_copy, row, col, player)
    return xs, os, board_copy


def evaluate_moves(moves, board, player, container):
    for move in moves:
        xs, os, returned_board = evaluate_move(board, move[0], move[1], player)
        score = os - xs
        container.append(Node(score, move, returned_board))

def print_tree(node, indent=0):
    print("  " * indent + f"Score: {node.score}, Move: {node.move}")
    for child in node.children:
        print_tree(child, indent + 1)

def minmax(board, player):

    moves = get_all_valid_moves(board, player)
    evaluate_moves(moves, board, player, root.children)

    opponent = 'O' if player == 'X' else 'X'

    for child in root.children:
        #print('\n', child.score, child.move)
        moves = get_all_valid_moves(child.after_board, opponent)
        evaluate_moves(moves, child.after_board, opponent, child.children)

    print_tree(root)
    root.children = []


"""
for i in range(5):
    root.children.append(Node(random.randint(1,10), [1,5]))

for node in root.children:
    for i in range(2):
        node.children.append(Node(random.randint(1,10), [2,6]))


for node in root.children:
    print(node.score)
    for node_2 in node.children:
        print("\t", node_2.score)
        """