import random
from functions import *

turno = False

board_player = [['⬞' for _ in range(10)] for _ in range(10)]
board_IA = [['⬞' for _ in range(10)] for _ in range(10)]


board_player_show = [['⬞' for _ in range(10)] for _ in range(10)]
board_IA_show = [['⬞' for _ in range(10)] for _ in range(10)]

colocar_nave(board_player, 3, 5, 5)
colocar_nave(board_player, 3, 2, 1)

colocar_nave(board_IA, 3, 0, 0)
colocar_nave(board_IA, 2, 3, 1)



print_board(board_player)
print("\n-----------------\n")
print_board(board_IA)

multiplayer_loop(True, board_player, board_IA)