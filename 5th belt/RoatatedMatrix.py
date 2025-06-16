def rotate_matrix(matrix):
    # Transpose the matrix
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]
    
    # Reverse each row to achieve the 90-degree clockwise rotation
    rotated = [row[::-1] for row in transposed]
    
    return rotated

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Input the matrix
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Rotate the matrix
rotated_matrix = rotate_matrix(matrix)

# Output the rotated matrix
print_matrix(rotated_matrix)