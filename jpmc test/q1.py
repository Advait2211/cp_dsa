def rotate_90(matrix):
    n = len(matrix)
    new_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_matrix[j][n - 1 - i] = matrix[i][j]

    return new_matrix

def rotate_270(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[n - 1 - j][i] = matrix[i][j]

    return rotated
        

def rotate_180(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[n - 1 - i][n - 1 - j] = matrix[i][j]

    return rotated


def mirror_image(matrix):
    return matrix[::-1]

def horizontal_flip(matrix):
    return [row[::-1] for row in matrix]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
for row in matrix:
    print(row)
print("\n90 Degree Rotation:")
print(rotate_90(matrix))
print("\n180 Degree Rotation:")
print(rotate_180(matrix))
print("\n270 Degree Rotation:")
print(rotate_270(matrix))   
print("\nMirror Image:")
print(mirror_image(matrix))
print("\nHorizontal Flip:")
print(horizontal_flip(matrix))