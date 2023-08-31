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
