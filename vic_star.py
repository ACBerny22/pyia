
import random

matrix = [[24,  15, 67, 24, 5,  14, 6],
          [45,  24, 64, 97, 43, 6,  12],
          [90,  37, 73, 32, 10, 78, 32],
          [27,  65, 39, 25, 9,  85, 32],
          [47,  27, 56, 48, 72, 20, 95]]

def generate_solutions(ammount):
    sols = []
    for a in range(ammount):
        individual = []
        for i in range(len(matrix[0])):
            number = random.randint(0,len(matrix)-1)
            individual.append(number)

        sols.append(individual)

    return sols


sols = generate_solutions(20)

padre1 = [1,2,3,4,5,6,7]
corte = 3

padre1Div = [padre1[:corte]] + [padre1[corte:]]

print(padre1Div)