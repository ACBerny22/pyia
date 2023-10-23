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

# Function to make a move
def make_move(board, row, col, player):
    if not is_valid_move(board, row, col, player):
        return False
    
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


    #print("Fichas O: ", os)
    return True

# Main game loop
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
        if make_move(board, row, col, current_player):
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
        else:
            print("Invalid move. Try again.")
    else:
        print("Invalid move. Row and column must be between 0 and 7.")

    xs, os = update_chips(board)

    print("Fichas X: ", xs)
    print("Fichas O: ", os)

