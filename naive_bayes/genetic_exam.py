import random

"""
matrix = [[24,15,67,24,5,14,6],
          [45,24,64,97,43,6,12],
          [90,37,73,32,10,78,32],
          [27,65,39,25,9,85,32],
          [47,27,56,48,72,20,95]]
"""

matrix = [
    [78, 84, 40, 6, 46, 8, 30, 49, 89, 28, 13, 1, 53, 53, 45, 90, 19, 48, 17, 26],
    [84, 31, 79, 69, 41, 19, 46, 51, 95, 23, 52, 14, 45, 2, 69, 94, 14, 50, 13, 69], 
    [18, 20, 5, 88, 83, 49, 62, 6, 48, 30, 34, 5, 90, 52, 49, 46, 79, 71, 53, 82],   
    [75, 88, 34, 1, 17, 12, 28, 84, 37, 28, 87, 19, 35, 31, 87, 80, 79, 10, 71, 61], 
    [62, 47, 16, 99, 61, 59, 29, 16, 2, 96, 7, 65, 69, 28, 50, 97, 86, 27, 9, 22],   
    [67, 94, 15, 80, 10, 61, 64, 48, 79, 74, 36, 86, 78, 48, 67, 78, 45, 9, 70, 42], 
    [40, 58, 64, 32, 57, 48, 38, 100, 2, 24, 54, 42, 24, 26, 19, 25, 99, 48, 53, 33],
    [85, 25, 86, 88, 71, 5, 47, 65, 15, 91, 26, 22, 3, 77, 15, 96, 56, 88, 97, 45],
    [97, 82, 86, 31, 24, 3, 43, 26, 5, 7, 58, 86, 12, 89, 39, 22, 81, 54, 14, 64],
    [69, 43, 45, 98, 82, 65, 61, 92, 38, 5, 18, 66, 70, 12, 74, 70, 61, 7, 45, 96],
    [65, 98, 57, 40, 50, 52, 47, 42, 16, 73, 3, 37, 91, 87, 92, 52, 36, 53, 7, 88],
    [42, 87, 100, 26, 98, 58, 2, 13, 73, 9, 79, 41, 44, 32, 3, 40, 71, 100, 87, 34],
    [100, 9, 35, 60, 97, 48, 62, 99, 55, 42, 82, 75, 95, 46, 51, 63, 3, 89, 61, 60],
    [73, 99, 23, 3, 27, 66, 100, 40, 82, 76, 48, 57, 56, 43, 88, 39, 51, 23, 98, 60],
    [46, 63, 100, 45, 19, 2, 37, 69, 49, 24, 46, 19, 56, 44, 1, 90, 94, 58, 32, 71]
]

def main():
    genetic()
    

# Works as Fitness too.
def foo(solution):
    total_value = 0
    for j in range(len(matrix[0])):
        #print(matrix[solution[j]][j])
        total_value += matrix[solution[j]] [j]

    return total_value

def generate_solutions(ammount):
    sols = []
    for a in range(ammount):
        individual = []
        for i in range(len(matrix[0])):
            number = random.randint(0,len(matrix)-1)
            individual.append(number)

        sols.append(individual)

    return sols
    

def fitness(solution):
    ans = foo(solution)

    if ans == 0:
        return -1
    else:
        return ans

def crossover(solucion1, solucion2):
    punto_corte = random.randint(0, len(matrix[0])-1)
    nueva_solucion1 = solucion1[:punto_corte] + solucion2[punto_corte:]
    return mutacion(nueva_solucion1, 0.2)


# Apply mutation
def mutacion(solucion, mut_rate, limite=len(matrix)-1):
    nueva_solucion = []

    for elemento in solucion:
        if random.random() < mut_rate:  # Comprueba si ocurre una mutación basada en el factor de mutación
            nuevo_elemento = elemento + random.randint(-5, 5)  # Muta el elemento sumando un valor aleatorio entre -14 y 14
            nuevo_elemento = min(max(nuevo_elemento, 0), limite)  # Asegura que el elemento esté en el rango [0, limite]
        else:
            nuevo_elemento = elemento  # No hay mutación en este elemento

        nueva_solucion.append(nuevo_elemento)

    return nueva_solucion


def print_l(array):
    for a in array:
        print(a)

def genetic():
    # Init population.
    # Generate solutions.
    solutions = []
    solutions = generate_solutions(10000)
    
    # Loop over the generations
    for i in range(10000):

        # Evaulate the solutions.
        solutions_with_rank = []
        for s in solutions:
            solutions_with_rank.append((foo(s), s))

        # Order the solutions.
        solutions_with_rank.sort()

        # Print the very best
        print("=============== Best One in Gen:", i, "===============")
        print(solutions_with_rank[0])


        if solutions_with_rank[0][0] < 140:
           break; 

        # Get best solutions
        best_solutions = solutions_with_rank[:100]

        #print(best_solutions)

        
        # Get every element in the best solutions
        elements = []
        for s in best_solutions:
            elements.append(s[1])

        #print(elements)
        
        new_generation = []
        for _ in range(1000):
            element_1 = random.choice(elements)
            element_2 = random.choice(elements)
            new_boi = crossover(element_1, element_2)
            new_generation.append(new_boi)
            
        solutions = new_generation

if __name__ == '__main__': 
    main()
