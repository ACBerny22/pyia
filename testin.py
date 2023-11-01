import random

class Node: 
    def __init__(self, score, move):
        self.score = score
        self.move = move
        self.children = []

def generate_random_tree(depth):
    if depth == 0:
        return None
    else:
        score = random.randint(1, 100)  # Generate a random score
        move = "Move " + str(depth)  # Generate a move label
        node = Node(score, move)
        node.children = [generate_random_tree(depth - 1) for _ in range(random.randint(1, 4))]  # Randomly generate 1 to 4 children nodes
        return node

# Example usage
random_tree = generate_random_tree(3)  # Generating a tree with 3 levels of children
print(random_tree)