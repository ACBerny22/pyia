from collections import Counter

matrix = [
    [2.23, 'azul'],
    [2.25, 'rojo'],
    [3, 'azul'],
]

print(matrix)

colors = []

for row in matrix:
    color = row[1]
    colors.append(color)

print(colors)


# Contar las ocurrencias de cada elemento en la lista
color_counter = Counter(colors)

# Obtener el elemento más repetido
most_common_color = color_counter.most_common(1)[0][0]

print(f"El color más repetido es: {most_common_color}")

def manhattan_distance(point1, point2):
    
    return abs(point1[0] - point1[1]) + abs(point2[0] - point2[1])

print(manhattan_distance([4, 5], [1, 2]))