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
    #Distancia entre el nodo nuevo y el nodo inicial
    node.g = node.g+1
    node.h = get_distance([node.position[0], node.position[1]], end_point)
    node.f = node.g + node.h

def get_final_path(final_node):
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
            path = get_final_path(current_node)
            print(path)
            break


        # Quitamos el nodo inicial de la open_list y la ponemos en el closed_list
        open_list.pop(current_node_index)
        closed_list.append(current_node)

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

        # Imprimmos cada que se actualiza la open_list, para propositos de graficación, no le
        # hagas caso a esto plox. 
        for explored in open_list:
            print(explored.position)

        i += 1

    return path


def main():

    # (fila, columna)
    maze = np.array([
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,1,0,0,0],
        [0,0,1,0,0,0],
        [0,0,1,0,0,0],
        [0,0,0,0,0,0],
    ])

    start_point = [5,0]
    end_point = [0, 5]

    path = find_path(maze, start_point, end_point)

    create_maze(maze, path)



def create_maze(maze, path):
    num_rows, num_cols = maze.shape

    # Create a figure and axis
    fig, ax = plt.subplots()

    def update_cell_color(row, col, new_color):
        cell_color = 'black' if maze[row, col] == 1 else 'white'
        ax.add_patch(plt.Rectangle((col, num_rows - row - 1), 1, 1, color=new_color))

    # Iterate through the matrix and create a colored rectangle for each cell
    for i in range(num_rows):
        for j in range(num_cols):
            cell_color = 'black' if maze[i, j] == 1 else 'white'
            ax.add_patch(plt.Rectangle((j, num_rows - i - 1), 1, 1, color=cell_color))

    # Set the aspect ratio to equal to ensure square cells
    ax.set_aspect('equal')

    # Set axis limits to include all cells
    ax.set_xlim(0, num_cols)
    ax.set_ylim(0, num_rows)

    for point in path:
        update_cell_color(point[0], point[1], 'red')
    plt.show()



if __name__ == '__main__':
    main()

