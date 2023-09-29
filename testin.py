import matplotlib.pyplot as plt
import random
import time
import numpy as np

# Datos de ejemplo: una lista de coordenadas que representan la ruta
ruta = [[3, 0], [2, 1], [2, 2], [1, 3], [1, 4], [0, 5], [1, 6]]

# (fila, columna)
maze = np.array([
    [0,0,1,0,0,0,0,0],
    [0,0,1,0,0,1,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
])

def translate_matrix_indices_to_coordinates(matrix, path):
    # Get the number of rows and columns in the matrix
    num_rows, num_cols = matrix.shape
    translated_route = []

    for node in path:
        # Translate the indices
        x = node[1]  # Column index becomes x-coordinate
        y = num_rows - 1 - node[0]  # Invert the row index and subtract from the total rows to get y-coordinate
        translated_route.append([x,y])

    return translated_route

limites_x = (0, 10)  # Límites para el eje X
limites_y = (0, 10)  # Límites para el eje Y

# Crear una función que actualice la gráfica con la ruta
def actualizar_grafica(ruta_actual):
    x, y = zip(*ruta_actual)  # Separar las coordenadas x e y de la ruta
    plt.clf()  # Limpiar la figura anterior
    plt.plot(x, y, marker='o', linestyle='-', color='b')  # Dibujar la ruta
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.title('Recorrido de la Ruta')
    plt.xlim(limites_x)  # Establecer límites en el eje X
    plt.ylim(limites_y)  # Establecer límites en el eje Y
    plt.grid(True)
    plt.pause(0.5)  # Pausa para controlar la velocidad de actualización


def create_maze(ruta):

    # Inicializar la figura
    plt.figure()

    #ruta = [(y, x) for x, y in ruta]

    # Recorrer la ruta y actualizar la gráfica
    for i in range(len(ruta)):
        ruta_actual = ruta[:i + 1]  # Obtener la porción de la ruta hasta el punto actual
        actualizar_grafica(ruta_actual)

    plt.show() 

print(translate_matrix_indices_to_coordinates(maze, ruta))

nueva_ruta = translate_matrix_indices_to_coordinates(maze, ruta)
create_maze(nueva_ruta)