def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            top = matrix[first][i]
            matrix[first][i] = matrix[last - (i - first)][first]
            matrix[last - (i - first)][first] = matrix[last][last - (i - first)]
            matrix[last][last - (i - first)] = matrix[i][last]
            matrix[i][last] = top

def print_matrix(matrix):
    for row in matrix:
        print(row)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
print_matrix(matrix)

rotate_matrix(matrix)

print("\nMatrix after 90-degree rotation:")
print_matrix(matrix)
