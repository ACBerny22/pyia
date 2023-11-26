import random
import copy

class Node: 
    def __init__(self, score, move, after_board):
        self.score = score # Quien tiene ventaja.
        self.move = move # Coordenadas.
        self.root_board = None # NO LE HAGAS CASO.
        self.after_board = after_board # Tablero DESPUES de haacer el mov.
        self.children = [] # Hijos.

root = Node(0, [0,0], None)

x_white_player = "⚪" #X
o_black_player = "⚫" #O

# Function to check if a move is valid
def is_valid_move(board, row, col, player):
    if board[row][col] != ' ':
        return False
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    opponent = o_black_player if player == x_white_player else x_white_player
    
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
    #print("Evaluated for player:", player)
    moves = []
    for i in range(8):
        for j in range(8):
            if is_valid_move(board, i, j, player):
                moves.append([i, j])
    
    #print(moves)
    return moves

# Función que define la cantidad de fichas para cada jugador.
def update_chips(board):
    xs = 0
    os = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == x_white_player:
                xs = xs + 1
            if board[i][j] == o_black_player:
                os = os + 1
    return xs, os


# Función para hacer un movimiento
def make_move(board, row, col, player):
    if not is_valid_move(board, row, col, player):
        xs, os = update_chips(board)
        #print("Fichas X: ", xs)
        #print("Fichas O: ", os)
        return False, xs, os
    
    board[row][col] = player
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    opponent = o_black_player if player == x_white_player else x_white_player
    
    for dr, dc in directions:
        r, c = row, col
        r += dr
        c += dc
        # Si estamos dentro de los limites del tablero y la celda a 
        # evaluar es del oponente comenzamos la exploración.
        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
                r += dr
                c += dc
            # Si estamos dentro de los limites, y la celda a 
            # evaluar es del jugador, encontramos el límite de cambio.
            if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == player:
                r -= dr
                c -= dc
                # Tomamos ambos puntos y empezamos a voltear las fichas
                # entre ambos puntos.
                while r != row or c != col:
                    board[r][c] = player
                    r -= dr
                    c -= dc


    xs, os = update_chips(board)
    #print("Fichas X: ", xs)
    #print("Fichas O: ", os)
    return True, xs, os


# Evalua un movimiento a partir de una copia del tablero, para no afectar el juego
# principal.
def evaluate_move(board, row, col, player):
    board_copy = copy.deepcopy(board)
    sike, xs, os = make_move(board_copy, row, col, player)
    return xs, os, board_copy


def sort_childs(container):
    
    pass


def evaluate_moves(moves, board, player, container):
    for move in moves:
        xs, os, returned_board = evaluate_move(board, move[0], move[1], player)
        score = os - xs
        container.append(Node(score, move, returned_board))
        if player == 'X':
            # Ordenar con los menores primero
            container.sort(key=lambda x: x.score, reverse=False)
        if player == 'O':
            # Ordenar con los mayores primero
            container.sort(key=lambda x: x.score, reverse=True)
        

def print_tree(node, indent=0):
    print("  " * indent + f"Score: {node.score}, Move: {node.move}")
    for child in node.children:
        print_tree(child, indent + 1)

"""def minmax(board, player):

    moves = get_all_valid_moves(board, player)
    evaluate_moves(moves, board, player, root.children)

    opponent = 'O' if player == 'X' else 'X'

    for child in root.children:
        #print('\n', child.score, child.move)
        moves = get_all_valid_moves(child.after_board, opponent)
        evaluate_moves(moves, child.after_board, opponent, child.children)

    print_tree(root)
    root.children = []"""

def minimax(root):
    print_tree(root)
    pass

def find_best_play(node, alpha=float('-inf'), beta=float('inf'), maximizing_player=True):
    if not node.children:
        return node, node.score  # If it's a leaf node, return itself and its score
    
    best_node = None
    if maximizing_player:
        max_score = float('-inf')
        for child in node.children:
            _, score = find_best_play(child, alpha, beta, False)
            if score > max_score:
                max_score = score
                best_node = child
            alpha = max(alpha, max_score)
            if beta <= alpha:
                break  # Beta cut-off
        return best_node, max_score
    else:
        min_score = float('inf')
        for child in node.children:
            _, score = find_best_play(child, alpha, beta, True)
            if score < min_score:
                min_score = score
                best_node = child
            beta = min(beta, min_score)
            if beta <= alpha:
                break  # Alpha cut-off
        return best_node, min_score

def create_tree(board, player, depth, node=None):
    if node is None:
        node = Node(None, "Root", board)
    
    if depth == 0:
        return  # Evaluate the leaf node
    
    moves = get_all_valid_moves(node.after_board, player)
    evaluate_moves(moves, node.after_board, player, node.children)
    
    opponent = o_black_player if player == x_white_player else x_white_player
    
    for child in node.children:
        create_tree(child.after_board, opponent, depth - 1, child)  # Recurse with reduced depth for children
        
    return node