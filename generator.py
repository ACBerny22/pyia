import pandas as pd
import numpy as np

# Genera puntos para la clase A (agrupados en un lado)
class_a_x = np.random.normal(2, 1, 50)
class_a_y = np.random.normal(2, 1, 50)
class_a = pd.DataFrame({'x_coord': class_a_x, 'y_coord': class_a_y, 'class': 'A'})

# Genera puntos para la clase B (agrupados en otro lado)
class_b_x = np.random.normal(8, 1, 50)
class_b_y = np.random.normal(2, 1, 50)
class_b = pd.DataFrame({'x_coord': class_b_x, 'y_coord': class_b_y, 'class': 'B'})

# Genera puntos para la clase C (agrupados en otro lado)
class_c_x = np.random.normal(2, 1, 50)
class_c_y = np.random.normal(8, 1, 50)
class_c = pd.DataFrame({'x_coord': class_c_x, 'y_coord': class_c_y, 'class': 'C'})

# Genera puntos para la clase D (agrupados en otro lado)
class_d_x = np.random.normal(8, 1, 50)
class_d_y = np.random.normal(8, 1, 50)
class_d = pd.DataFrame({'x_coord': class_d_x, 'y_coord': class_d_y, 'class': 'D'})

# Combina los DataFrames en uno solo
dataset = pd.concat([class_a, class_b, class_c, class_d], ignore_index=True)

# Guarda el conjunto de datos en un archivo CSV
dataset.to_csv('conjunto_de_datos.csv', index=False)

# Muestra las primeras filas del conjunto de datos
print(dataset.head())
