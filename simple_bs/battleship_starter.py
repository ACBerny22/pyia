import random

# Create the game board
board = [['O' for _ in range(10)] for _ in range(10)]

# Place ships (for simplicity, we'll place a single ship of size 3)
ship_row = random.randint(0, 9)
ship_col = random.randint(0, 7)
for i in range(3):
    board[ship_row][ship_col + i] = 'S'

# Display the board
def print_board(board):
    for row in board:
        print(' '.join(row))
        
print_board(board)

# Game loop
turns = 0
while True:
    # Player's turn
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    # Check if the guess hits a ship
    if board[guess_row][guess_col] == 'S':
        print("Congratulations! You sank the battleship!")
        break
    else:
        print("You missed!")
        board[guess_row][guess_col] = 'X'

    # Display the updated board
    print_board(board)
    turns += 1

# Game over
print(f"Game over! You took {turns} turns to sink the battleship.")
