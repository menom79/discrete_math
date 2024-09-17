import numpy as np

# Adjacency matrix
A = np.array([
    [0, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 0]
])

# a) Two-step routes from node 3 to node 5
A2 = np.linalg.matrix_power(A, 2)
two_step_routes = A2[2, 4]  # Index 2 is node 3, and index 4 is node 5 (in 0-based indexing)
print(f"Two-step routes from node 3 to node 5: {two_step_routes}")

# b) Five-step routes from node 6 to node 4
A5 = np.linalg.matrix_power(A, 5)
five_step_routes = A5[5, 3]  # Index 5 is node 6, and index 3 is node 4
print(f"Five-step routes from node 6 to node 4: {five_step_routes}")

# c) 28-step routes from node 2 to node 1
A28 = np.linalg.matrix_power(A, 28)
twenty_eight_step_routes = A28[1, 0]  # Index 1 is node 2, and index 0 is node 1
print(f"28-step routes from node 2 to node 1: {twenty_eight_step_routes}")
