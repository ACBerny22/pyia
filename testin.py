def buscar_vecinos(tablero, posicion):
    fila_actual = posicion[0]
    columna_actual = posicion[1]
                        #  N        NE       E      SE        S     SO        O      NO
    puntos_cardinales = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0,-1), (-1, -1)]
    vecinos = []

    for punto in puntos_cardinales:
        vecino = [fila_actual + punto[0], columna_actual + punto[1]]

        # Verificar que no sea un obstaculo, o que exista dentro del tablero.
        if 0 <= vecino[0] < len(tablero) and 0 <= vecino[1] < len(tablero[0]):
            if tablero[vecino[0]][vecino[1]] == 0:
                vecinos.append(vecino)

    return vecinos

tablero = [
    [0,0,0,0],
    [1,0,0,1],
    [0,0,1,0],
    [1,0,0,0]
]

posiciones_vecinos = buscar_vecinos(tablero, [1,1])

for pos in posiciones_vecinos:
    pass