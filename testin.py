import pandas as pd

# Tu DataFrame original
data = {
    'vista': ['soleado', 'soleado', 'nublado'],
    'temperatura': ['alta', 'alta', 'alta'],
    'humedad': ['alta', 'alta', 'alta'],
    'viento': ['no', 'si', 'no'],
    'jugar': ['si', 'no', 'si']
}

df = pd.DataFrame(data)

# Filtrar las filas donde 'jugar' es 'si' y contar las ocurrencias de 'vista'
count_vista_si = df[df['jugar'] == 'si']['vista'].value_counts()


sum = 0
for elemento, ocurrencias in count_vista_si.items():
    sum += ocurrencias

print(sum)