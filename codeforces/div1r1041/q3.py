def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))


    largest_diff = second_largest_diff = float('inf')
    largest_idx = second_largest_idx = -1

    arr = []

    for i in range(n):
        num = abs(a[i] - b[i])
        if num > largest_diff:
            second_largest_diff = largest_diff
            second_largest_idx = largest_idx

            largest_diff = num
            largest_idx = i
        elif largest_diff > num > second_largest_diff:
            second_largest_diff = num
            second_largest_idx = i

    
        
    best_i = largest_idx
    best_j = second_largest_idx

    print(a[best_i], a[best_j], b[best_i], b[best_j])

    thing = sorted([a[best_i], a[best_j], b[best_i], b[best_j]])

    a[best_i] = thing[-1]
    a[best_j] = thing[-2]
    b[best_i] = thing[0]
    b[best_j] = thing[1]

    soln = 0

    for i in range(n):
        soln += abs(a[i] - b[i])

    return soln

    
t = int(input())
 
for _ in range(t):
    # print("output: ")
    print("output: ", solve())