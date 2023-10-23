# Mauricio Bernabé Fortuna López - 19071489
# I.A. 7:00 - 8:00

import random
import time


# (1,2,3)
def foo(solution):
    return 2*solution[0]**5 - 5*solution[1]**3 + 2*solution[2]**2 - 25

def fitness(solution):
    ans = foo(solution)

    if ans == 0:
        return 999999
    else:
        return abs(1/ans)

def crossover(solucion1, solucion2):
    punto_corte = 1 
    nueva_solucion1 = solucion1[:punto_corte] + solucion2[punto_corte:]
    return mutacion(nueva_solucion1, 0.8)


# Apply mutation
def mutacion(solution, mut_rate):
    to_list = list(solution)
    for i in range(len(to_list)):
        if random.random() < mut_rate:
            # Mutate a little bit
            to_list[i] = to_list[i] * random.uniform(0.99, 1.01)
    return tuple(to_list)

def print_l(array):
    for a in array:
        print(a)

i = 0
def genetic():

    # Init population.
    # Generate solutions.
    solutions = []
    for s in range(10000):
        sol = (random.uniform(0,1000), random.uniform(0,1000), random.uniform(0,1000))
        solutions.append(sol)

    # Loop over the generations
    for i in range(10000):

        # Evaulate the solutions.
        solutions_with_rank = []
        for s in solutions:
            solutions_with_rank.append((fitness(s), s))

        # Order the solutions.
        solutions_with_rank.sort()
        solutions_with_rank.reverse()

        # Print the very best
        print("=============== Best One in gen:", i, "===============")
        print(solutions_with_rank[0])


        if solutions_with_rank[0][0] > 9999:
            return best_solutions[0]
            break; 

        # Get best solutions
        best_solutions = solutions_with_rank[:100]

        
        # Get every element in the best solutions
        elements = []
        for s in best_solutions:
            elements.append(s[1])

        new_generation = []
        for _ in range(1000):
            element_1 = random.choice(elements)
            element_2 = random.choice(elements)
            new_boi = crossover(element_1, element_2)
            new_generation.append(new_boi)
            
        solutions = new_generation
        i += 1

def main():

    inicio = time.time()
    solution = genetic()
    fin = time.time()
    print("Tiempo de ejecucion: ", fin-inicio)

    evaluation = foo(solution[1])
    print("La solucion es: ", (evaluation+25)) 


    error = (25 - evaluation)/(25*100)
    precision = 100 - error
    print("La presicion es de: ", precision)


if __name__ == '__main__': 
    main()
