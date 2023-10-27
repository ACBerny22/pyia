from tree import *

# Initialize the board
board = [[' ' for _ in range(8)] for _ in range(8)]
board[3][3] = board[4][4] = 'X'
board[3][4] = board[4][3] = 'O'

xs = 0
os = 0

# Function to print the board
def print_board(board):
    print("  0 1 2 3 4 5 6 7")
    for i in range(8):
        print(i, end=' ')
        for j in range(8):
            print(board[i][j], end=' ')
        print()


# Sike Loop.
current_player = 'X'
while True:
    if current_player == 'X':
            print("====================== TURNO DEL JUGADOR 1 ======================")
            print_board(board)
            print("Player", current_player + "'s turn")
            try:
                minmax(board, current_player)
                row, col = map(int, input("Enter your move (row and column): ").split())
            except ValueError:
                print("Invalid input. Please enter numbers separated by a space.")
                continue

            if 0 <= row < 8 and 0 <= col < 8:
                is_valid, xs, os = make_move(board, row, col, current_player)
                if is_valid:
                    current_player = 'O'
                else:
                    print("Invalid move. Try again.")
            else:
                print("Invalid move. Row and column must be between 0 and 7.")

    if current_player == 'O':
            print("====================== TURNO DEL JUGADOR 2 ======================")
            print_board(board)
            print("Player", current_player + "'s turn")
            try:
                # Aquí el otro jugador hace su movida, pero en realidad, aquí se sacará del 
                # algoritmo minimax
                minmax(board, current_player)
                row, col = map(int, input("Enter your move (row and column): ").split())
            except ValueError:
                print("Invalid input. Please enter numbers separated by a space.")
                continue

            if 0 <= row < 8 and 0 <= col < 8:
                is_valid, xs, os = make_move(board, row, col, current_player)
                if is_valid:        
                    current_player = 'X'
                else:
                    print("Invalid move. Try again.")
            else:
                print("Invalid move. Row and column must be between 0 and 7.")
    pass


# Main game loop
"""
current_player = 'X'
while True:
    print_board(board)
    print("Player", current_player + "'s turn")
    try:
        row, col = map(int, input("Enter your move (row and column): ").split())
    except ValueError:
        print("Invalid input. Please enter numbers separated by a space.")
        continue

    if 0 <= row < 8 and 0 <= col < 8:
        is_valid, xs, os = make_move(board, row, col, current_player)
        if is_valid:
            if current_player == 'X':
                # Turno del jugador.
                current_player = 'O'
            else:
                # Turno de la computadora.
                current_player = 'X'
        else:
            print("Invalid move. Try again.")
    else:
        print("Invalid move. Row and column must be between 0 and 7.")

    #xs, os = update_chips(board)

"""

