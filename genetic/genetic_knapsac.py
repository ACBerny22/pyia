import random

W = 100
v = [10,20,30,40, 54, 56, 23, 12]
w = [30,10,40,20, 12, 45, 64, 24]


def main():
    genetic()

# (1,2,3)
def foo(solution):
    total_value = 0
    total_weight = 0
    for i in range(len(solution)):
        total_value = total_value + (v[i]*solution[i])
        total_weight = total_weight + (w[i]*solution[i])
    
    if total_weight > W:
        return 0
    
    return total_value

def fitness(solution):
    ans = foo(solution)

    if ans == 0:
        return -1
    else:
        return ans

def crossover(solucion1, solucion2):
    punto_corte = 1 
    nueva_solucion1 = solucion1[:punto_corte] + solucion2[punto_corte:]
    return mutacion(nueva_solucion1, 0.6)


# Apply mutation
def mutacion(solution, mut_rate):
    to_list = list(solution)
    for i in range(len(to_list)):
        if random.random() < mut_rate:
            # Mutate a little bit
            to_list[i] = random.randint(0,1)
    return tuple(to_list)

def print_l(array):
    for a in array:
        print(a)

def genetic():
    # Init population.
    # Generate solutions.
    solutions = []
    for s in range(1):
        sol = (random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1))
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
        print("=============== Best One ===============")
        print(solutions_with_rank[0])


        if solutions_with_rank[0][0] > 9999:
            break; 

        # Get best solutions
        best_solutions = solutions_with_rank[:100]

        """
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
        """


if __name__ == '__main__': 
    main()
