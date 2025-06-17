def solve():
    m, n = map(int, input().split())
    matrix = [0 * n] * m

    for i in range(m):
        matrix[i] = list(map(int, input().split()))

    # print(matrix)

    max_val = float('-inf')
    positions = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                positions = [(i, j)]

            elif matrix[i][j] == max_val:
                positions.append((i, j))

    # print(positions)
    row_unique_rows = set()
    row_unique_cols = set()

    row_unique_rows.add(positions[0][0])

    col_unique_rows = set()
    col_unique_cols = set()

    col_unique_cols.add(positions[0][1])

    count = 0
    
    for i, j in positions:
        # row based
        pass
    # fuckit
        
        
    # print(positions)
    # print(row_dependency, col_dependency)
    # print(unique_rows, unique_cols)


t = int(input())

for _ in range(t):
    print(f"Output: {solve()}")
    # print(solve())