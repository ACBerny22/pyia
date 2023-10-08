import random
from functions import *

class Ship:
  def __init__(self, large, dots):
    self.range = large
    self.dots = dots


board_player = [['⬞' for _ in range(10)] for _ in range(10)]
board_IA = [['⬞' for _ in range(10)] for _ in range(10)]

board_player_show = [['⬞' for _ in range(10)] for _ in range(10)]
board_IA_show = [['⬞' for _ in range(10)] for _ in range(10)]


colocar_nave(board_player, 3, 5, 5)
colocar_nave(board_player, 3, 2, 1)

colocar_nave(board_IA, 3, 0, 0)
colocar_nave(board_IA, 2, 3, 1)


print("Player 1 Ships:")
print_board(board_player)
print("\n-----------------\n")
print("Player 2 Ships:")
print_board(board_IA)

singleplayer_loop(True, board_player, board_IA)

#print(take_one(prob_board))