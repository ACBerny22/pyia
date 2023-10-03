import random

board_player_show = [['⬞' for _ in range(10)] for _ in range(10)]
board_IA_show = [['⬞' for _ in range(10)] for _ in range(10)]


prob_board = [[(1/100) for _ in range(10)] for _ in range(10)]


def colocar_nave(tablero, longitud, fila, columna):
    direccion = random.choice(['horizontal', 'vertical'])

    if direccion == 'horizontal':
        if columna + longitud > len(tablero[0]):
            return False  # No se puede colocar horizontalmente en esta posición
        for i in range(longitud):
            if tablero[fila][columna + i] != '⬞':
                print("Pues nel carnal")
                return False  # La posición está ocupada
        for i in range(longitud):
            tablero[fila][columna + i] = '■'
    else:  # Dirección vertical
        if fila + longitud > len(tablero):
            return False  # No se puede colocar verticalmente en esta posición
        for i in range(longitud):
            if tablero[fila + i][columna] != '⬞':
                return False  # La posición está ocupada
        for i in range(longitud):
            tablero[fila + i][columna] = '■'
    
    return True

def print_board(board):
    i = 0
    print("   ", "0 1 2 3 4 5 6 7 8 9")
    for row in board:
        print(i ,  " ", ' '.join(row))
        i += 1



def get_prob():
    for row in prob_board:
        print(row)




def multiplayer_loop(is_my_turn, board_1, board_2):
    coord = []
    while(True):
        if is_my_turn:
            print("----------------------TURNO DEL JUGADOR 1 ----------------------")
            for i in range(2):
                entry = input("Fila: ")
                coord.append(int(entry))

            print(coord)

            if board_2[coord[0]][coord[1]] == '■':
                print("Hit!!")
                board_player_show[coord[0]][coord[1]] = '◉'
            else:
                print("Miss!!")
                board_player_show[coord[0]][coord[1]] = '◌'
                
            coord = []
            print_board(board_player_show)

        else:
            print("----------------------TURNO DEL JUGADOR 2 ----------------------")
            for i in range(2):
                entry = input("Fila: ")
                coord.append(int(entry))

            print(coord)

            if board_1[coord[0]][coord[1]] == '■':
                print("Hit!!")
                board_IA_show[coord[0]][coord[1]] = '◉'
            else:
                print("Miss!!")
                board_IA_show[coord[0]][coord[1]] = '◌'
                
            coord = []
            print_board(board_IA_show)

        is_my_turn = not is_my_turn
            
