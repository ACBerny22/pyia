import random
import time as t

#IA Statistics
plays = []
misses = []
hits = []

#IA Statis
SEEKING = 0
DESTROYNG = 1
bot_state = SEEKING


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


def take_one(prob_board):
    row = 0
    column = 0

    # Si no hay naves pendientes por destruir o a la vista
    # el estado sera "seeking" o buscando.
    if bot_state == SEEKING:
        row = random.randint(0,9)
        column = random.randint(0,9)

        #Comprobar que la coordenada no se haya dado ya.
        pass



    # Si hubo un hit el bot empezara a buscar el resto de
    # la nave hasta destruirla, para luego pasar a "SEEKING"
    # otra vez
    if bot_state == DESTROYNG:
        print("No more!")


    return((row, column))


def update_prob(board, row, column):

    symbol = board_player_show[row][column]

    if symbol == '◌':
        board[row][column] = 0
        misses.append((row, column))

    
    for row in board:
        print(row)


def singleplayer_loop(is_my_turn, ships_player, ships_ia):
    coord = []
    
    while(True):
        if is_my_turn:
            print("====================== TURNO DEL JUGADOR 1 ======================")
            
            
            print("Player 1 Status:")
            print_board(board_player_show)
            print("_______________________________________\n")
            print("Computer Status:")
            print_board(board_IA_show)

            # El jugador ingresa sus coordenadas
            for i in range(2):
                entry = input("Fila: ")
                coord.append(int(entry))

            print(coord)

            # Se comprueba que la coordenada elegida contenga una nave
            if ships_player[coord[0]][coord[1]] == '■':
                print("Hit!!")
                # Si si, se actualiza el tablero con el hit.
                board_IA_show[coord[0]][coord[1]] = '◉'
            else:
                print("Miss!!")
                # Si no, se actualiza el tablero con el miss.
                board_IA_show[coord[0]][coord[1]] = '◌'
                
            coord = []

            t.sleep(2)
        
        else:
            print("====================== TURNO DEL BOT ======================")

            print("Player 1 Status:")
            print_board(board_player_show)
            print("_______________________________________\n")
            print("Computer Status:")
            print_board(board_IA_show)

            # La maquina hace la eleccion de la jugada que hara
            coord = take_one(prob_board)

            print(coord)
            plays.append(coord)

            # Se comprueba que la coordenada elegida contenga una nave
            if ships_player[coord[0]][coord[1]] == '■':
                print("Hit!!")
                 # Si si, se actualiza el tablero con el hit.
                board_player_show[coord[0]][coord[1]] = '◉'
                # Se inicia el modo destructor del bot.
                bot_state = DESTROYNG
            else:
                print("Miss!!")
                # Si no, se actualiza el tablero con el miss.
                board_player_show[coord[0]][coord[1]] = '◌'
                
            coord = []

        print(plays)
        is_my_turn = not is_my_turn




def multiplayer_loop(is_my_turn, board_1, board_2):
    coord = []
    while(True):
        if is_my_turn:
            print("====================== TURNO DEL JUGADOR 1 ======================")
            
            
            print("Player 1 Status:")
            print_board(board_player_show)
            print("_______________________________________\n")
            print("Player 2 Status:")
            print_board(board_IA_show)

            for i in range(2):
                entry = input("Fila: ")
                coord.append(int(entry))

            print(coord)

            if board_2[coord[0]][coord[1]] == '■':
                print("Hit!!")
                board_IA_show[coord[0]][coord[1]] = '◉'
            else:
                print("Miss!!")
                board_IA_show[coord[0]][coord[1]] = '◌'
                
            coord = []

        else:
            print("====================== TURNO DEL JUGADOR 2 ======================")

            print("Player 1 Status:")
            print_board(board_player_show)
            print("_______________________________________\n")
            print("Player 2 Status:")
            print_board(board_IA_show)


            for i in range(2):
                entry = input("Fila: ")
                coord.append(int(entry))

            print(coord)

            if board_1[coord[0]][coord[1]] == '■':
                print("Hit!!")
                board_player_show[coord[0]][coord[1]] = '◉'
            else:
                print("Miss!!")
                board_player_show[coord[0]][coord[1]] = '◌'
                
            coord = []

        is_my_turn = not is_my_turn
            
