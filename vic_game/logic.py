import random
import copy
import numpy as np


class Nodo:
    def __init__(self, puntaje, movimiento, tablero):
        self.puntaje = puntaje
        self.movimiento = movimiento
        self.tablero = tablero
        self.hijos = []

#VERIFICA QUE LA FICHA CAIGA HASTA DONDE TOPE
def gravedad(columna, tablero, jugador):
    cont = 0

    #if tablero[0][columna] != 0:
     #   return 0, False

    while tablero[cont][columna] == 0: #Mientras la casilla sea 0 (está vacía)
        #print(cont)
        cont+=1
        if cont == 6:                  #Si llega al final del tablero se detiene
            break
        
    tablero[cont-1][columna] = jugador
    return cont-1


def ganaVertical(fila, columna, tablero, jugador):
    if fila < 3: #Se checa si hay fichas iguales abajo
        if tablero[fila][columna]== jugador and tablero[fila+1][columna]== jugador and tablero[fila+2][columna]== jugador and tablero[fila+3][columna]==jugador:
            #return(print("GANÓ JUGADOR",jugador, "VERTICALMENTE"))
            return True
        
def ganaHorizontal(fila, columna, tablero,jugador):
    #if fila > 3:
        #vecinos = [[fila+1, columna],[fila+2, columna],[fila+3, columna]]
    if columna < 3: 
        #Se checa si hay fichas iguales a la derecha
        if tablero[fila][columna+1]== jugador and tablero[fila][columna+2]== jugador and tablero[fila][columna+3]==jugador:
            return(True)
        #Se checa si la columna es 2 y hay una ficha igual a la izquierda y dos a la derecha
        elif columna == 2 and tablero[fila][columna-1]== jugador and tablero[fila][columna+1]== jugador and tablero[fila][columna+2]==jugador:
            return(True)
        #Se checa si la columna es 2 y hay dos fichas iguales a la izquierda y una a la derecha
        elif columna == 2 and tablero[fila][columna-2]== jugador and tablero[fila][columna-1]== jugador and tablero[fila][columna+1]==jugador:
            return(True)
        #Se checa si la columna es 1 y hay una ficha igual a la izquierda y dos a la derecha
        elif columna == 1 and tablero[fila][columna-1]== jugador and tablero[fila][columna+1]== jugador and tablero[fila][columna+2]==jugador:
            return(True)
        
        
    elif columna > 3:   
        #Se checa si hay fichas iguales a la izquierda
        if tablero[fila][columna-1]== jugador and tablero[fila][columna-2]== jugador and tablero[fila][columna-3]==jugador:
            return(True)
        #Se checa si la columna es 4 y hay dos fichas iguales a la izquierda y una a la derecha
        elif columna == 4 and tablero[fila][columna-2]== jugador and tablero[fila][columna-1]== jugador and tablero[fila][columna+1]==jugador:
            return(True)
        #Se checa si la columna es 4 y hay una ficha igual a la izquierda y dos a la derecha
        elif columna == 4 and tablero[fila][columna-1]== jugador and tablero[fila][columna+1]== jugador and tablero[fila][columna+2]==jugador:
            return(True)
        #Se checa si la columna es 5 y hay dos fichas a la izquierda y una a la derecha
        elif columna == 5 and tablero[fila][columna-2]== jugador and tablero[fila][columna-1]== jugador and tablero[fila][columna+1]==jugador:
            return(True)
        
        
    elif columna == 3:  
        #Se checa si la columna es 3 y hay fichas iguales a la derecha 
        if tablero[fila][columna+1]== jugador and tablero[fila][columna+2]== jugador and tablero[fila][columna+3]==jugador:
            return(True)
        #Se checa si la columna es 3 y hay fichas iguales a la izquierda 
        elif tablero[fila][columna-1]== jugador and tablero[fila][columna-2]== jugador and tablero[fila][columna-3]==jugador:
            return(True)
        #Se checa si la columna es 3 y hay dos fichas iguales a la izquierda y una a la derecha
        elif tablero[fila][columna-2]== jugador and tablero[fila][columna-1]== jugador and tablero[fila][columna+1]==jugador:
            return(True)
        #Se checa si la columna es 3 y hay una ficha igual a la izquierda y dos a la derecha
        elif tablero[fila][columna-1]== jugador and tablero[fila][columna+1]== jugador and tablero[fila][columna+2]==jugador:
            return(True)
        
def ganaDiagonal(fila, columna, tablero,jugador):
    if columna < 3: 
        
        if fila < 3:
            #Se checa si la fila es menor que 3 y hay fichas iguales en diagonal abajo a la derecha
            if tablero[fila+1][columna+1]== jugador and tablero[fila+2][columna+2]== jugador and tablero[fila+3][columna+3]==jugador:
                return(True)
            
            elif fila == 1:
                #Se checa si la columna es 1 y hay una arriba izquierda y dos abajo derecha
                if columna == 1 and tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]== jugador and tablero[fila+2][columna+2]==jugador:
                    return(True)
                #Se checa si la columna es 2 y hay una ficha igual en diagonal arriba izquierda y dos abajo derecha
                elif columna == 2 and tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]== jugador and tablero[fila+2][columna+2]==jugador:
                    return(True)
                #Se checa si la columna es 2 y hay dos fichas iguales en diagonal abajo a la izquierda y una arriba a la derecha
                elif columna == 2 and tablero[fila+2][columna-2]== jugador and tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]==jugador:
                    return(True)
                
            elif fila == 2:
                #Se checa si la columna es 1 y hay una ficha igual en diagonal arriba izquierda y dos abajo derecha
                if columna == 1 and tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]== jugador and tablero[fila+2][columna+2]==jugador:
                    return(True)
                #Se checa si la columna es 1 y hay una abajo izquierda y dos arriba derecha
                elif columna == 1 and tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]== jugador and tablero[fila-2][columna+2]==jugador:
                    return(True)
                #Se checa si la columna es 2 y hay dos arriba izquierda y una abajo derecha 
                elif columna == 2 and tablero[fila-2][columna-2]== jugador and tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]==jugador:
                    return(True)
                #Se checa si la columna es 2 y hay una arriba izquierda y dos abajo derecha 
                elif columna == 2 and tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]== jugador and tablero[fila+2][columna+2]==jugador:
                    return(True)
                #Se checa si la columna es 2 y hay dos abajo izquierda y una arriba derecha 
                elif columna == 2 and tablero[fila+2][columna-2]== jugador and tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]==jugador:
                    return(True)
                #Se checa si a columna es 2 y hay uno abajo izquierda y dos arriba derecha
                elif columna == 2 and tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]== jugador and tablero[fila-2][columna+2]==jugador:
                    return(True)
            
        elif fila > 2:  
            #Se checa si la fila es mayor que 2 y hay fichas iguales en diagonal arriba a la derecha
            if tablero[fila-1][columna+1]== jugador and tablero[fila-2][columna+2]== jugador and tablero[fila-3][columna+3]==jugador:
                return(True)
            
            elif fila == 3:
                #Se checa si la columna es 1 y hay una arriba izquierda y dos abajo derecha
                if columna == 1 and tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]== jugador and tablero[fila+2][columna+2]==jugador:
                    return(True)
                #Se checa si la columna es 1 hay una abajo izquierda y dos arriba derecha  
                if columna == 1 and tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]== jugador and tablero[fila-2][columna+2]==jugador:
                    return(True)
                #Se checa si la columna es 2 y hay dos arriba izquierda y una abajo derecha 
                elif columna == 2 and tablero[fila-2][columna-2]== jugador and tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]==jugador:
                    return(True)
                #Se checa si la columna es 2 y hay una arriba izquierda y dos abajo derecha 
                elif columna == 2 and tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]== jugador and tablero[fila+2][columna+2]==jugador:
                    return(True)
                #Se checa si la columna es 2 y hay dos abajo izquierda y una arriba derecha 
                elif columna == 2 and tablero[fila+2][columna-2]== jugador and tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]==jugador:
                    return(True)
                #Se checa si a columna es 2 y hay uno abajo izquierda y dos arriba derecha
                elif columna == 2 and tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]== jugador and tablero[fila-2][columna+2]==jugador:
                    return(True)
            elif fila == 4:
                #Se checa si la columna es 1 hay una abajo izquierda y dos arriba derecha 
                if columna == 1 and tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]== jugador and tablero[fila-2][columna+2]==jugador:
                    return(True)
                #Se checa si a columna es 2 y hay uno abajo izquierda y dos arriba derecha
                elif columna == 2 and tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]== jugador and tablero[fila-2][columna+2]==jugador:
                    return(True)
                #Se checa si la columna es 2 y hay dos arriba izquierda y una abajo derecha 
                elif columna == 2 and tablero[fila-2][columna-2]== jugador and tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]==jugador:
                    return(True)
                
    
    elif columna == 3:

        if fila < 3:

            #Se checa si hay fichas iguales en diagonal abajo a la izquierda
            if tablero[fila+1][columna-1]== jugador and tablero[fila+2][columna-2]== jugador and tablero[fila+3][columna-3]==jugador:
                return(True)
            #Se checa si hay fichas iguales en diagonal abajo a la derecha
            elif tablero[fila+1][columna+1]== jugador and tablero[fila+2][columna+2]== jugador and tablero[fila+3][columna+3]==jugador:
                return(True)
            
            elif fila == 1:
                #Se checa si hay una arriba izquierda y dos abajo derecha
                if tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]== jugador and tablero[fila+2][columna+2]==jugador:
                    return(True)
                #Se checa si hay dos abajo izquierda y una arriba derecha
                elif tablero[fila+2][columna-2]== jugador and tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]==jugador:
                    return(True)
                
            elif fila == 2:
                #Se checa si hay dos arriba izquierda y una abajo derecha 
                if tablero[fila-2][columna-2]== jugador and tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]==jugador:
                    return(True)
                #Se checa si hay una arriba izquierda y dos abajo derecha
                elif tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]== jugador and tablero[fila+2][columna+2]==jugador:
                    return(True) 
                #Se checa si hay dos abajo izquierda y uno arriba derecha
                elif tablero[fila+2][columna-2]== jugador and tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]==jugador:
                    return(True)
                #Se checa si hay uno abajo izquierda y dos arriba derecha
                elif tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]== jugador and tablero[fila-2][columna+2]==jugador:
                    return(True)
                

        elif fila > 2: 

            #Se checa si hay en diagonal arriba a la izquierda
            if tablero[fila-1][columna-1]== jugador and tablero[fila-2][columna-2]== jugador and tablero[fila-3][columna-3]==jugador:
                return(True)
            #Se checa si hay en diagonal arriba a la derecha 
            elif tablero[fila-1][columna+1]== jugador and tablero[fila-2][columna+2]== jugador and tablero[fila-3][columna+3]==jugador:
                return(True)
            
            elif fila == 3:
                #Se checa si hay dos arriba izquierda y una abajo derecha 
                if tablero[fila-2][columna-2]== jugador and tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]==jugador:
                    return(True)
                #Se checa si hay una arriba izquierda y dos abajo derecha 
                elif tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]== jugador and tablero[fila+2][columna+2]==jugador:
                    return(True)
                #Se checa si hay dos abajo izquierda y una arriba derecha 
                elif tablero[fila+2][columna-2]== jugador and tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]==jugador:
                    return(True)
                #Se checa si hay uno abajo izquierda y dos arriba derecha
                elif tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]== jugador and tablero[fila-2][columna+2]==jugador:
                    return(True)
            
            elif fila == 4:
                #Se checa si hay dos arriba izquierda y una abajo derecha 
                if tablero[fila-2][columna-2]== jugador and tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]==jugador:
                    return(True)
                #Se checa si hay uno abajo izquierda y dos arriba derecha
                elif tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]== jugador and tablero[fila-2][columna+2]==jugador:
                    return(True)

    elif columna > 3:

        if fila < 3:
            #Se checa si hay fichas iguales en diagonal abajo a la izquierda
            if tablero[fila+1][columna-1]== jugador and tablero[fila+2][columna-2]== jugador and tablero[fila+3][columna-3]==jugador:
                return(True)
            
            elif fila == 1:

                if columna == 4:
                    #Se checa si hay uno arriba izquierda y dos abajo derecha
                    if tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]== jugador and tablero[fila+2][columna+2]==jugador:
                        return(True)
                    #Se checa si hay dos abajo izquierda y uno arriba derecha
                    elif tablero[fila+2][columna-2]== jugador and tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]==jugador:
                        return(True)

                elif columna == 5:
                    #Se checa si hay dos abajo izquierda y una arriba derecha
                    if tablero[fila+2][columna-2]== jugador and tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]==jugador:
                        return(True)
                    

            elif fila == 2:
    
                if columna == 4:
                    #Se checa si hay dos arriba izquierda y una abajo derecha 
                    if tablero[fila-2][columna-2]== jugador and tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]==jugador:
                        return(True)
                    #Se checa si hay uno arriba izquierda y dos abajo derecha
                    elif tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]== jugador and tablero[fila+2][columna+2]==jugador:
                        return(True)
                    #Se checa si hay dos abajo izquierda y uno arriba derecha
                    elif tablero[fila+2][columna-2]== jugador and tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]==jugador:
                        return(True)
                    #Se checa si hay uno abajo izquierda y dos arriba derecha
                    elif tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]== jugador and tablero[fila-2][columna+2]==jugador:
                        return(True)

                elif columna == 5:
                    #Se checa si hay dos arriba izquierda y una abajo derecha 
                    if tablero[fila-2][columna-2]== jugador and tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]==jugador:
                        return(True)
                    #Se checa si hay dos abajo izquierda y una arriba derecha
                    elif tablero[fila+2][columna-2]== jugador and tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]==jugador:
                        return(True)
                    

        elif fila > 2:  
            #Se checa si hay fichas iguales en diagonal arriba a la izquierda
            if tablero[fila-1][columna-1]== jugador and tablero[fila-2][columna-2]== jugador and tablero[fila-3][columna-3]==jugador:
                return(True)


            elif fila == 3:

                if columna == 4:
                    #Se checa si hay dos arriba izquierda y una abajo derecha 
                    if tablero[fila-2][columna-2]== jugador and tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]==jugador:
                        return(True)
                    #Se checa si hay uno arriba izquierda y dos abajo derecha
                    elif tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]== jugador and tablero[fila+2][columna+2]==jugador:
                        return(True)
                    #Se checa si hay dos abajo izquierda y uno arriba derecha
                    elif tablero[fila+2][columna-2]== jugador and tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]==jugador:
                        return(True)
                    #Se checa si hay uno abajo izquierda y dos arriba derecha
                    elif tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]== jugador and tablero[fila-2][columna+2]==jugador:
                        return(True)

                elif columna == 5:
                    #Se checa si hay dos arriba izquierda y una abajo derecha 
                    if tablero[fila-2][columna-2]== jugador and tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]==jugador:
                        return(True)
                    #Se checa si hay dos abajo izquierda y uno arriba derecha
                    elif tablero[fila+2][columna-2]== jugador and tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]==jugador:
                        return(True)


            elif fila == 4:

                if columna == 4:
                    #Se checa si hay dos arriba izquierda y una abajo derecha 
                    if tablero[fila-2][columna-2]== jugador and tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]==jugador:
                        return(True)
                    #Se checa si hay uno abajo izquierda y dos arriba derecha
                    elif tablero[fila+1][columna-1]== jugador and tablero[fila-1][columna+1]== jugador and tablero[fila-2][columna+2]==jugador:
                        return(True)

                elif columna == 5:
                    #Se checa si hay dos arriba izquierda y una abajo derecha 
                    if tablero[fila-2][columna-2]== jugador and tablero[fila-1][columna-1]== jugador and tablero[fila+1][columna+1]==jugador:
                        return(True)


def gana(fila, columna, tablero, jugador):
    
    ganaV= ganaVertical(fila, columna, tablero,jugador)
    if ganaV == True:
        #print("GANÓ JUGADOR",jugador, "VERTICALMENTE")
        return True
    else:
        ganaH= ganaHorizontal(fila, columna, tablero,jugador)
        if ganaH == True:
            #print("GANÓ JUGADOR",jugador, "HORIZONTALMENTE")
            return True
        else:
            ganaD= ganaDiagonal(fila, columna, tablero,jugador)
            if ganaD == True:
                #print("GANÓ JUGADOR",jugador, "EN DIAGONAL")
                return True
    return False

def movPosibles(tablero):
    mov = []
    for i in range(7):
        if tablero[0][i] == 0:
            mov.append(i)

    return mov

def evaluarMov(movimientos, tablero, jugador):
    movEvaluados = []
    if jugador == 1:
        oponente = 2
    else:
        oponente = 1
    #tablero2 = copy.deepcopy(tablero)
    for move in movimientos:
        tablero2 = copy.deepcopy(tablero)
        mov = gravedad(move,tablero2,jugador)
        hayGanador = gana(mov,move,tablero2,jugador)
        
        horizontal, vertical, diagonal = count_connected(tablero, jugador, mov, move)

        added_score = horizontal + vertical + diagonal
        if jugador == 1:
            added_score = -added_score

        if hayGanador == False:
            movEvaluados.append([added_score, move, tablero2])
        else:
            if jugador == 1:
                movEvaluados.append([-100+added_score, move, tablero2])

            elif jugador == 2:
                movEvaluados.append([100+added_score, move, tablero2])

    return movEvaluados


def construirArbol(tablero, jugador, profundidad, nodo = None):
    if nodo == None:
        nodo = Nodo(0, "raiz", tablero)
    
    if profundidad == 0:
        return

    movimientos =  movPosibles(tablero)
    movEvaluados = evaluarMov(movimientos, tablero, jugador)
    
    for i in range(len(movEvaluados)):
        nodo.hijos.append(Nodo(movEvaluados[i][0],movEvaluados[i][1], movEvaluados[i][2]))

    if jugador == 1:
        oponente = 2
    else:
        oponente = 1
    
    for hijo in nodo.hijos:
        construirArbol(hijo.tablero, oponente, profundidad-1, hijo)

    return nodo

def print_tree(nodo, indent=0):
    print("  " * indent + f"Score: {nodo.puntaje}, Move: {nodo.movimiento}")
    for hijo in nodo.hijos:
        print_tree(hijo, indent + 1)

def imprimirTablero(tablero):
    print("1   2   3   4   5   6   7 \n")
    for row in tablero:
        for unit in row:
            if unit == 1:
                print("🔴", end="  ")
            elif unit == 2:
                print("🟡", end="  ")
            else:
                print("⚫", end="  ")
        print("\n")


def count_connected(board, player, row, col):
    # Initialize counts for horizontal, vertical, and diagonal directions
    horizontal_count = 0
    vertical_count = 0
    diagonal_count = 0

    # Check horizontally
    for c in range(len(board[0])):
        if board[row][c] == player:
            horizontal_count += 1
        else:
            horizontal_count = 0  
        # Break if 4 pieces are found in a row
        if horizontal_count >= 4:
            break

    # Check vertically
    for r in range(len(board)):
        if board[r][col] == player:
            vertical_count += 1
        else:
            vertical_count = 0
        
        # Break if 4 pieces are found in a column
        if vertical_count >= 4:
            break

    # Check diagonally (bottom-left to top-right direction)
    for r, c in zip(range(row, -1, -1), range(col, len(board[0]))):
        if r < 0 or c >= len(board[0]):
            break
        if board[r][c] == player:
            diagonal_count += 1
        else:
            break
        
    for r, c in zip(range(row + 1, len(board)), range(col - 1, -1, -1)):
        if r >= len(board) or c < 0:
            break
        if board[r][c] == player:
            diagonal_count += 1
        else:
            break
    
    # Return counts for horizontal, vertical, and diagonal connections
    return horizontal_count, vertical_count, diagonal_count
        
def find_best_play(node, maximizing_player=True):
    if not node.hijos:
        return node, node.puntaje  # If it's a leaf node, return itself and its score
    
    best_node = None
    if maximizing_player:
        max_score = float('-inf')
        for child in node.hijos:
            _, score = find_best_play(child, False)
            if score > max_score:
                max_score = score
                best_node = child
        return best_node, max_score
    else:
        min_score = float('inf')
        for child in node.hijos:
            _, score = find_best_play(child, True)
            if score < min_score:
                min_score = score
                best_node = child
        return best_node, min_score

def find_best_move(node, maximizing_player=True):
    if not node.hijos:
        return node
    
    if maximizing_player:
        best_score = float("-inf")
        best_node = None
        for child in node.hijos:
            if score >= 100:
                return child
            score = find_best_move(child, False).puntaje
            if score > best_score:
                best_score = score
                best_node = child
        return best_node
    else:
        best_score = float("inf")
        best_node = None
        for child in node.hijos:
            score = find_best_move(child, True).puntaje
            if score < best_score:
                best_score = score
                best_node = child
        return best_node