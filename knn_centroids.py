# Mauricio Bernabé Fortuna López - 19071489
# I.A. 7:00 - 8:00

import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

EUCLIDIANA = 1
MANHATTAN = 2
JACCARD = 3

archivo_csv = './files/example3.csv'  # Reemplaza con la ruta de tu archivo CSV
dataframe = pd.read_csv(archivo_csv)

def euclidean_distance(point1, point2):
    squared_distances = [(a - b)**2 for a, b in zip(point1, point2)]
    return math.sqrt(sum(squared_distances))

def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

def jaccard_distance(point1, point2):
    set1 = set(point1)
    set2 = set(point2)
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    jaccard_dist = 1 - (intersection / union)
    return jaccard_dist

def get_neighbors(n, matrix):

    comparison_df = pd.DataFrame(matrix, columns=(['newdot', 'dot', 'class', 'distance']))
    sorted_comparison_df = comparison_df.sort_values(by='distance')

    return sorted_comparison_df.head(n)

def graphic(graph_body, colors, dot, centroids, is_final):

    # Dibuja los puntos del dataframe
    for class_label, color in colors.items():
        class_data = graph_body[graph_body['class'] == class_label]
        plt.scatter(class_data['x_coord'], class_data['y_coord'], c=color, label=class_label)

    # Dibuja el punto nuevo
    if(not is_final):
        plt.scatter([dot[0] for dot in new_dot], [dot[1] for dot in new_dot], c='black', label='Additional Point')
    
    # Dibuja los centroides
    plt.scatter(centroids['x'], centroids['y'], marker='*', color='firebrick', s=100)

    # Dibuja un círculo alrededor del clúster utilizando la distancia al centroide
    
    for index, row in centroids.iterrows():
        circle = plt.Circle(( row['x'], row['y']), max(row['std_x'], row['std_y']), fill=False, linestyle='dotted', color='black')
        plt.gca().add_patch(circle)
    
    plt.show()

def get_centroids(classes, sub_dataframes):

    centroids = []
    centroids_df = pd.DataFrame(columns=['x', 'y', 'std_x', 'std_y', 'class'])

    for classifcation in classes:
        centroid_x = sub_dataframes[classifcation]['x_coord'].mean()

        # Calcula la media de las coordenadas Y
        centroid_y = sub_dataframes[classifcation]['y_coord'].mean()

        # Calcula la desviacion estandar y la añade a cada centroide.
        std_x = sub_dataframes[classifcation]['x_coord'].std()
        std_y = sub_dataframes[classifcation]['y_coord'].std()

        # El centroide será un punto con las coordenadas (centroid_x, centroid_y, std_x, std_y)
        centroids.append([centroid_x, centroid_y, std_x, std_y])
        centroids_df = centroids_df._append({'x': centroid_x, 'y': centroid_y, 'std_x':std_x, 'std_y':std_y, 'class':classifcation}, ignore_index=True)
    
    return centroids_df
   

def worker_2(centroids, new_dot, distance):

    distances = []
    out = []

    for i in range(len(new_dot)):
        for index, row in centroids.iterrows():
            x_cord = row['x']
            y_cord = row['y']

            print(x_cord)
            print(y_cord)
            
            if(distance == 1):
                calc = euclidean_distance([x_cord, y_cord], new_dot[i])
            elif(distance == 2):
                calc = manhattan_distance([x_cord, y_cord], new_dot[i])
            elif(distance == 3):
                calc = jaccard_distance([x_cord, y_cord], new_dot[i])

            distances.append(calc)

        print(distances)
        centroids['distance'] = distances

        valor_minimo = centroids['distance'].min()
        fila_con_minimo = centroids.loc[centroids['distance'] == valor_minimo]

        distances = []

        dataframe.loc[len(dataframe.index)] = [new_dot[i][0], new_dot[i][1], fila_con_minimo['class'].values[0]]
        element = [new_dot[i][0], new_dot[i][1], fila_con_minimo['class'].values[0]]
        out.append(element)

    return out

if __name__ == '__main__': 

    new_dot = [
        [10.6839585, 2.765],
        [9.5544645, 17.729107],
        [14.650000, 6.100000],
    ]

    colors = {'A': 'tomato', 'B': 'cornflowerblue', 'C': 'mediumseagreen', 'D': 'darkviolet', 'E': 'orange'}

    # Agrupamos el dataframe en sub_dataframes para separar clases.
    grouped = dataframe.groupby('class')
    sub_dataframes = {class_label: group for class_label, group in grouped}

    # Obtenemos todas las clases disponibles.
    classes = dataframe['class'].unique()

    # Obtenemos el centroide para cada clase.
    centroids = get_centroids(classes, sub_dataframes)
    print(centroids)

    # Graficamos el dataset de entrenamiento con sus respectivos centroides.
    graphic(dataframe, colors, new_dot, centroids, False)

    to_graph = worker_2(centroids, new_dot, EUCLIDIANA)
    print(to_graph)

    #--------------------------------#

    grouped = dataframe.groupby('class')
    sub_dataframes = {class_label: group for class_label, group in grouped}

    # Obtenemos todas las clases disponibles.
    classes = dataframe['class'].unique()

    # Obtenemos el centroide para cada clase.
    centroids = get_centroids(classes, sub_dataframes)
    print(centroids)

    # Graficamos el dataset de entrenamiento con sus respectivos centroides.
    graphic(dataframe, colors, new_dot, centroids, True)

