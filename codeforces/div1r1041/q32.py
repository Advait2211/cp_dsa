def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))


    best_i, best_j = 0, 1

    min_temp = float('inf')
    min_diff = -1
    largest, sec_largest = float('-inf'), float('-inf')
    largest_i, sec_largest_i = -1, -1

    for i in range(n):            
        x = abs(a[i] - b[i])
        if x > largest:
            sec_largest = largest
            sec_largest_i = largest_i
            largest = x
            largest_i = i
        elif x > sec_largest:
            sec_largest = x
            sec_largest_i = i

        # for j in range(i + 1, n):
        #     values = [a[i], a[j], b[i], b[j]]
            # new
            # values = sorted(values)
            # temp2 = 0
            # temp2 += values[-1] - values[0]
            # temp2 += values[-2] - values[1]
            # if temp2 < min_temp:
            #     min_temp = temp2
            #     best_i = i
            #     best_j = j

            # old
            # diff = max(values) - min(values)
            # if diff < min_diff:
            #     min_diff = diff
            #     best_i, best_j = i, j
            

    # print(a[largest_i], a[sec_largest_i], b[largest_i], b[sec_largest_i])

    thing = sorted([a[largest_i], a[sec_largest_i], b[largest_i], b[sec_largest_i]])
    # print(thing)

    a[largest_i] = thing[-1]
    a[sec_largest_i] = thing[-2]
    b[largest_i] = thing[0]
    b[sec_largest_i] = thing[1]

    soln = 0

    for i in range(n):
        soln += abs(a[i] - b[i])

    return soln

    
t = int(input())
 
for _ in range(t):
    # print("output: ")
    print(solve())


    """
    1 2 8 10

    10 1
    2 8
    """