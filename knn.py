import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

archivo_csv = './files/example.csv'  # Reemplaza con la ruta de tu archivo CSV
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
    new_dots = [
        [4,5], 
        [18,20], 
        [12,10],
        [5,5],
        [13,15.2],
    ]
    coordinates_matrix = [
    [25, 8, 4],
    [8, 26, 9],
    [16, 9, 12],
    ]

    dataset = worker(new_dots, dataframe)
    print(dataset)

    colors = {'A': 'red', 'B': 'blue', 'C': 'green', 'D': 'purple', 'E': 'orange'}
    for class_label, color in colors.items():
        class_data = dataset[dataset['class'] == class_label]
        plt.scatter(class_data['x_coord'], class_data['y_coord'], c=color, label=class_label)

    plt.show()



#ily ily2

#Te dije varias vecees que mas de un día iba a llevarte el desayuno a la cama! 
#aii, lo sé yy yo tambien a ti y te voy a cocinar muy rico y ambos tambien los vamos a hacer juntos
#Super sii!! Te quiero muuucho!!
#y yo te quiero mucho a ti!!

#Por todo lo que hemos dicho mientras...Jugamos
