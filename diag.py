a = [1,2,3,4]
b = [7,6,5,4,7]

resultado = []

for i in range(max(len(a), len(b))):
    suma = a[i % len(a)] + b[i % len(b)]
    resultado.append(suma)

print(resultado)
