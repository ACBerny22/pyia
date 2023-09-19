# Mauricio Bernabé Fortuna López - 19071489
# I.A. 7:00 - 8:00

import pandas as pd
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


archivo_csv = './files/example2.csv'  # Reemplaza con la ruta de tu archivo CSV
dataframe = pd.read_csv(archivo_csv)

def euclidean_distance(point1, point2):
    squared_distances = [(a - b)**2 for a, b in zip(point1, point2)]
    return math.sqrt(sum(squared_distances))

def get_neighbors(n, matrix):

    comparison_df = pd.DataFrame(matrix, columns=(['newdot', 'dot', 'class', 'distance']))
    sorted_comparison_df = comparison_df.sort_values(by='distance')

    return sorted_comparison_df.head(n)
   
def worker(new_dots, frame):

    comparison_matrix = []
    value_columns = frame.columns[:-1]  # Exclude the last column

    #coord_matrix are the new dots.
    for coord_matrix in new_dots:
        for index, row in frame.iterrows():
            #coord_df is the ones that are already classified.
            coord_df = [row[column] for column in value_columns]  # Add more dimensions.
            distance = euclidean_distance(coord_matrix, coord_df)
            class_label = row['class']  # Get the class label

            # Store the comparison data in a list.
            comparison_data = [coord_matrix] + [coord_df] + [class_label] + [distance]
            comparison_matrix.append(comparison_data)

        #Now that we have a matrix with everything, wee need to fiter only the ones that are closer.
        neighbors = get_neighbors(3, comparison_matrix)

        #Now that we have only the closer ones, we need to know which is the dominant class.
        most_common_class = neighbors['class'].value_counts().idxmax()

        #Now assign the dominant class to the input dot.
        coord_matrix_values = coord_matrix

        #Add the most_common_class at the end
        coord_matrix_values.append(most_common_class)
        frame.loc[len(frame.index)] = coord_matrix_values

        #Reset the comparision_matrix for the next dot.
        comparison_matrix = []

    return frame
    

if __name__ == '__main__': 
    dots_2d = [
        [4,5], 
        [18,20], 
        [12,10],
        [5,5],
        [13,15.2],
        [18,1],
        [17,2],
    ]

    dots_2d_2 = [
        [3,3.7],
        [3.2,1.5],
        [2.1,4.67],
        [1.2,2.5],
        [4.6,4.2],
    ]

    dots_3d = [
    [25, 8, 4],
    [8, 26, 9],
    [16, 9, 12],
    ]

    dots_6d = [
    [2.8,2.4,4.5,4.0,5.7,6.5]
    ]


    # Mapea los colores a colores reales que quieras utilizar
    colors = {'A': 'red', 'B': 'blue', 'C': 'green', 'D': 'purple', 'E': 'orange'}

        # Crea una figura 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Itera sobre las filas del DataFrame y traza los puntos con colores correspondientes
    for index, row in dataframe.iterrows():
        x, y, z, color = row['x_coord'], row['y_coord'], row['z_coord'], row['class']
        ax.scatter(x, y, z, c=colors[color], label=color)
        ax.scatter([dot[0] for dot in dots_3d], [dot[1] for dot in dots_3d], [dot[2] for dot in dots_3d], c='black', label='Additional Point')


    # Agrega etiquetas de ejes
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')

    # Muestra el gráfico 3D
    plt.show()

    """
    colors = {'A': 'red', 'B': 'blue', 'C': 'green', 'D': 'purple', 'E': 'orange'}
    for class_label, color in colors.items():
        class_data = dataframe[dataframe['class'] == class_label]
        plt.scatter(class_data['x_coord'], class_data['y_coord'], c=color, label=class_label)
        plt.scatter([dot[0] for dot in dots_2d_2], [dot[1] for dot in dots_2d_2], c='black', label='Additional Point')

    plt.show()
    """

    dataset = worker(dots_3d, dataframe)
    print(dataset)


    # Supongamos que tienes un DataFrame llamado 'df' con cuatro columnas: x, y, z y color
    # Por ejemplo:
    # df = pd.DataFrame({'x': [1, 2, 3, 4],
    #                    'y': [2, 3, 4, 5],
    #                    'z': [3, 4, 5, 6],
    #                    'color': ['A', 'B', 'C', 'D']})

    # Crea una figura 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Itera sobre las filas del DataFrame y traza los puntos con colores correspondientes
    for index, row in dataset.iterrows():
        x, y, z, color = row['x_coord'], row['y_coord'], row['z_coord'], row['class']
        ax.scatter(x, y, z, c=colors[color], label=color)

    # Agrega etiquetas de ejes
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')

    # Muestra el gráfico 3D
    plt.show()




    """
    colors = {'A': 'red', 'B': 'blue', 'C': 'green', 'D': 'purple', 'E': 'orange'}
    for class_label, color in colors.items():
        class_data = dataset[dataset['class'] == class_label]
        plt.scatter(class_data['x_coord'], class_data['y_coord'], c=color, label=class_label)

    plt.show()
    """