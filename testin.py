import numpy as np
import pandas as pd

# Establece una semilla aleatoria para reproducibilidad
np.random.seed(42)

# Genera puntos para la clase A (primer clúster)
class_a_x = np.random.normal(2, 1, 50)
class_a_y = np.random.normal(3, 1, 50)
class_a = pd.DataFrame({'x_coord': class_a_x, 'y_coord': class_a_y, 'class': 'A'})

# Genera puntos para la clase B (segundo clúster)
class_b_x = np.random.normal(7, 1, 50)
class_b_y = np.random.normal(7, 1, 50)
class_b = pd.DataFrame({'x_coord': class_b_x, 'y_coord': class_b_y, 'class': 'B'})

# Genera puntos para la clase C (tercer clúster)
class_c_x = np.random.normal(4, 1, 50)
class_c_y = np.random.normal(7, 1, 50)
class_c = pd.DataFrame({'x_coord': class_c_x, 'y_coord': class_c_y, 'class': 'C'})

# Combina los DataFrames en un conjunto de entrenamiento
training_set = pd.concat([class_a, class_b, class_c], ignore_index=True)

# Muestra las primeras filas del conjunto de entrenamiento
print(training_set.head())