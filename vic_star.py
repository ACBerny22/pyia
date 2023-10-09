class Nodo:
    def __init__(self, g, h, f, padre, posicion):
        self.g = g # Numero
        self.h = h # Numero
        self.f = f # Numero
        self.padre = padre # Nodo
        self.posicion = posicion # Lista[Numeros]

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

def trazar_camino(nodo_final):
    ruta = []
    ruta.append(nodo_final.posicion)



    return ruta

#No le hagas caso, este es el mio .-. XD.
def get_final_path(final_node, maze):
    final_path = []
    current_node = final_node

    while current_node is not None:
        final_path.append(current_node.posicion)
        current_node = current_node.padre

    # Invertir la ruta para que esté en orden desde el nodo inicial al nodo final
    final_path.reverse()

    return final_path


def manhattan(a,b):
    return abs((a[0] - b[0]) + (a[1]- b[1]))

def buscar_ruta(tablero, posicion_inicial, posicion_final):
    abiertos = []
    cerrados = []
    ruta = []

    nodo_inicial = Nodo(0, 0, 0, None, posicion_inicial)
    abiertos.append(nodo_inicial)

    while len(abiertos) > 0:
    
        nodo_actual = abiertos[0]
        indice_actual = 0

        # Verificar cual es el nodo con menor f...Y luego ese nodo
        # sera el nodo actual.
        for i, n in enumerate(abiertos):
            if n.f < nodo_actual.f:
                nodo_actual = n
                indice_actual = i
        
        for nodo in abiertos:
            if nodo.posicion == posicion_final:
                #hemos encontrado nuestro final.
                nodo_final = Nodo(0,0,0, nodo_actual, nodo.posicion)

                #encontrar el camino.
                ruta = trazar_camino(nodo_final)
                
                #Y se chingó
                break

        # Cerramos el nodo actual.
        abiertos.pop(indice_actual)
        cerrados.append(nodo_actual)

        # Sacar los vecinos de nuestro nodo actual.
        posiciones_vecinos = buscar_vecinos(tablero, nodo_actual.posicion) # Arreglo de 8 posiciones

        hijos_de_actual = []
        for pos in posiciones_vecinos:
            g = 1 + nodo_actual.g
            h = manhattan(nodo_actual.posicion, posicion_final)
            f = g + h
            nodo_nuevo = Nodo(g, h, f, nodo_actual, pos)
            hijos_de_actual.append(nodo_nuevo)
        
        for hijos in hijos_de_actual:
            abiertos.append(hijos)

    return ruta


def main():
    tablero = [
            [0,0,0,0],
            [1,0,0,1],
            [0,0,1,0],
            [1,0,0,0]
        ]
    
    punto_inicio = [0,0]
    punto_final = [3,3]

    path = buscar_ruta(tablero, punto_inicio, punto_final)
    print(path)


if __name__ == "__main__":
    main()