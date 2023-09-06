# Mauricio Bernabé Fortuna López - 19071489
# I.A. 7:00 - 8:00

import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt


EUCLIDIANA = 1
MANHATTAN = 2
JACCARD = 3

archivo_csv = './files/too_many.csv'  # Reemplaza con la ruta de tu archivo CSV
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

def graphic(graph_body, colors):
    for class_label, color in colors.items():
        class_data = graph_body[graph_body['class'] == class_label]
        plt.scatter(class_data['x_coord'], class_data['y_coord'], c=color, label=class_label)

    plt.show()
   
def worker(new_dots, frame, n, metric):

    comparison_matrix = []
    value_columns = frame.columns[:-1]  # Exclude the last column

    #coord_matrix are the new dots.
    for coord_matrix in new_dots:
        for index, row in frame.iterrows():
            #coord_df is the ones that are already classified.
            coord_df = [row[column] for column in value_columns]  # Add more dimensions.

            if metric == 1:
                distance = euclidean_distance(coord_matrix, coord_df)
            elif metric == 2:
                distance = manhattan_distance(coord_matrix, coord_df)
            elif metric == 3:
                distance = jaccard_distance(coord_matrix, coord_df)

            class_label = row['class']  # Get the class label

            # Store the comparison data in a list.
            comparison_data = [coord_matrix] + [coord_df] + [class_label] + [distance]
            comparison_matrix.append(comparison_data)

        #Now that we have a matrix with everything, wee need to fiter only the ones that are closer.
        neighbors = get_neighbors(n, comparison_matrix)

        #Now that we have only the closer ones, we need to know which is the dominant class.
        most_common_class = neighbors['class'].value_counts().idxmax()

        #Now assign the dominant class to the input dot.
        coord_matrix_values = coord_matrix

        #Add the most_common_class at the end
        #coord_matrix_values.append(most_common_class)
        #frame.loc[len(frame.index)] = coord_matrix_values

        #Reset the comparision_matrix for the next dot.
        comparison_matrix = []

    return most_common_class

def runtime(K, new_dot, training_set, ):
    return 0  

if __name__ == '__main__': 

    new_dot = [
        [2.1, 3.9], 
    ]

    colors = {'A': 'red', 'B': 'blue', 'C': 'green', 'D': 'purple', 'E': 'orange'}

    graphic(dataframe, colors)


    result_df = pd.DataFrame(columns=['K', 'Class'])

    # 1: Euclidiana
    # 2: Manhattan
    # 3: Jaccard
    for i in range(1, 10):
        dataset = worker(new_dot, dataframe, i, EUCLIDIANA)
        result_df = result_df._append({'K': i, 'Class': dataset}, ignore_index=True)

    print("-------------------------------------")
    print("Para el punto:", *new_dot)
    print("-------------------------------------")
    print(result_df.to_string(index=False))

