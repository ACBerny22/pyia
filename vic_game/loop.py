from logic import *

tablero = [[0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0]]

jugador = 1
puntaje = 0
ganador = False

while(True):
    if jugador == 1:
        imprimirTablero(tablero)
        #print("Movimientos posibles:" , movPosibles(tablero))
        columna = int(input("Jugador ingrese columna"))-1
        if columna in movPosibles(tablero):
            fila = gravedad(columna, tablero,jugador)
            print("\n")
            ganador = gana(fila, columna, tablero,jugador) 
            if ganador:
                print("JUGADOR GANA!!")
                imprimirTablero(tablero)

                break
            jugador = 2
        else:
            print("Movimiento no valido")        
    else:
        imprimirTablero(tablero)
        #print("Movimientos posibles:" , movPosibles(tablero))
        tree = construirArbol(tablero, jugador, 6)
        #print_tree(tree)
        best_play_node, _ = find_best_play(tree)
        print("Best move for the AI:", best_play_node.movimiento, "Score:", best_play_node.puntaje)
        columna = best_play_node.movimiento
        if columna in movPosibles(tablero):
            fila = gravedad(columna, tablero,jugador)
            
            print("\n")
            ganador = gana(fila, columna, tablero,jugador) 
            if ganador:
                print("IA GANA!!")
                imprimirTablero(tablero)
                break
            jugador = 1
        else:
            print("Movimiento no valido")