# Mauricio Bernabé Fortuna López - 19071489
# I.A. 7:00 - 8:00

import numpy as np
import matplotlib.pyplot as plt


class Node:
    def __init__(self, parent, position):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0


def get_neighbours(maze, current_node):
    # Obtenemos los adyacentes
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # 8 direcciones
    neighbours = []

    for dx, dy in directions:
        new_x = current_node.position[0] + dx
        new_y = current_node.position[1] + dy

        # Verificar que la nueva posicion este dentro de la matriz
        if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]):
            if maze[new_x][new_y] == 0:
                neighbours.append([new_x, new_y])

    return neighbours

def create_values(node, start_point, end_point):
    # Es el nodo más 10 porque es UN SOLO salto, puesto que es vecino.
    node.g = 10+node.parent.g
    #node.g = get_distance([node.position[0], node.position[1]], start_point)
    node.h = get_distance([node.position[0], node.position[1]], end_point)
    node.f = node.g + node.h

def get_final_path(final_node, maze):
    final_path = []
    current_node = final_node

    while current_node is not None:
        final_path.append(current_node.position)
        current_node = current_node.parent

    # Invertir la ruta para que esté en orden desde el nodo inicial al nodo final
    final_path.reverse()

    return final_path

# Manhattan
def get_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return (abs(x1 - x2) + abs(y1 - y2)) * 10

def find_path(maze, start_point, end_point):
    
    i = 0
    path = []
    # Creacion del nodo inicial
    start_node = Node(None, start_point)
    start_node.g = 0
    start_node.h = get_distance(start_point, end_point)
    start_node.f = start_node.g + start_node.h

    # Establecemos el nodo final
    end_node = Node(None, end_point)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []
    to_print = []

    open_list.append(start_node)

    #Aqui iria el while
    while len(open_list) > 0:
        current_node = open_list[0]
        current_node_index = 0

        # Elegimos el nodo con el que trabajermos primero, o sea, el del menor costo
        # Tambien extraemos el indice del nodo dentro de la lista, puesto que ese es el que vamos a popear,
        # obviamente tenemos que saber cual vamos a popear, no te pases.
        for i, node in enumerate(open_list):
            if node.f < current_node.f:
                current_node = node
                current_node_index = i

        # Nomas pa ver cual eligio
        # print(current_node.position)

        if current_node.position == end_node.position:
            path = get_final_path(current_node, maze)
            #path = transform_path(maze, path)
            break


        # Quitamos el nodo inicial de la open_list y la ponemos en el closed_list
        open_list.pop(current_node_index)
        closed_list.append(current_node)

        for node in closed_list:
            to_print.append(node.position)
        
        print("The nodes in this lap are: ")
        print(node.position)

        to_print = []

        # Obtenemos los vecinos
        neighbours_pos = get_neighbours(maze, current_node)

        # Le creamos un nodo a cada posicion, le ponemos los valores y los ponemos en una lista de todos los hijos
        # de esta iteracion
        children = []
        for pos in neighbours_pos:
            new_node = Node(current_node, pos)
            create_values(new_node, start_point, end_point)

            children.append(new_node)
            
        # los a­ñadimos a la open_list
        for child in children:
            open_list.append(child)

        i += 1

    return path



def main():

    # (fila, columna)
    maze = np.array([
        [0,1,0,0,0,0],
        [0,1,0,1,0,1],
        [1,0,1,1,1,0],
        [0,1,1,0,1,1],
        [0,0,0,1,0,0],
    ])


    start_point = [0,0]
    end_point = [4,5]


    path = find_path(maze, start_point, end_point)
    print(path)
    #print(obstaculos)
    #create_maze_2(path, obstaculos)

    print(get_obstacles(maze))
    create_maze(maze, path)

def get_obstacles(maze):

    obstacles = []

    #We need indexes!!
    for row in maze:
        for column in row:
            if column == 1:
                obstacles.append([row, column])

    obstacles = transform_path(maze, obstacles)
    return obstacles


def transform_path(matrix, path):
    # Get the number of rows and columns in the matrix
    num_rows, num_cols = matrix.shape
    translated_route = []

    for node in path:
        # Translate the indices
        x = node[1]  # Column index becomes x-coordinate
        y = num_rows - 1 - node[0]  # Invert the row index and subtract from the total rows to get y-coordinate
        translated_route.append([x,y])

    return translated_route

def create_maze(maze, path):
    num_rows, num_cols = maze.shape

    # Create a figure and axis
    fig, ax = plt.subplots()

    def update_cell_color(row, col, new_color):
        cell_color = 'gray' if maze[row, col] == 1 else 'white'
        ax.add_patch(plt.Rectangle((col, num_rows - row - 1), 1, 1, color=new_color))

        

    # Iterate through the matrix and create a colored rectangle for each cell
    for i in range(num_rows):
        for j in range(num_cols):
            cell_color = 'slategray' if maze[i, j] == 1 else 'white'
            ax.add_patch(plt.Rectangle((j, num_rows - i - 1), 1, 1, color=cell_color))

    # Set the aspect ratio to equal to ensure square cells
    ax.set_aspect('equal')

    # Set axis limits to include all cells
    ax.set_xlim(0, num_cols)
    ax.set_ylim(0, num_rows)

    for point in path:
        update_cell_color(point[0], point[1], 'tomato')
        
    plt.show()


limites_x = (0, 10)  # Límites para el eje X
limites_y = (0, 10)  # Límites para el eje Y

def actualizar_grafica(ruta_actual, obstaculos):
    x, y = zip(*ruta_actual)  # Separar las coordenadas x e y de la ruta
    plt.clf()  # Limpiar la figura anterior

    # Dibujar la ruta
    plt.plot(x, y, marker='o', linestyle='-', color='b')

    # Dibujar los obstáculos en rojo
    for obstaculo in obstaculos:
        plt.scatter(obstaculo[0], obstaculo[1], color='red', marker='s', s=200)

    plt.xticks(range(int(limites_x[0]), int(limites_x[1]) + 1))
    plt.yticks(range(int(limites_y[0]), int(limites_y[1]) + 1))

    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.title('Recorrido de la Ruta')
    plt.xlim(limites_x)  # Establecer límites en el eje X
    plt.ylim(limites_y)  # Establecer límites en el eje Y
    plt.grid(True)

    plt.pause(0.5)  # Pausa para controlar la velocidad de actualización

def create_maze_2(ruta, obstaculos):
    # Inicializar la figura
    plt.figure()

    # Recorrer la ruta y actualizar la gráfica
    for i in range(len(ruta)):
        ruta_actual = ruta[:i + 1]  # Obtener la porción de la ruta hasta el punto actual
        actualizar_grafica(ruta_actual, obstaculos)

    plt.show()

if __name__ == '__main__':
    main()

