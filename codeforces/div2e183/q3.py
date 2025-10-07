def solve():
    n = int(input())
    a = input()

    a_count = b_count = 0
    prefix = [0] * (n+1)

    for i in range(len(a)):
        if a[i] == 'a':
            a_count += 1
            prefix[i+1] = prefix[i] + 1
        else:
            b_count += 1
            prefix[i+1] = prefix[i] - 1

    if a_count == b_count:
        return 0
    if a_count == 0 or b_count == 0:
        return -1

    

    goal = a_count - b_count

    index_map = {}
    min_diff = float('inf')

    for i, val in enumerate(prefix):
        if val - goal in index_map:
            min_diff = min(min_diff, abs(i - index_map[val - goal]))
        
        index_map[val] = i


    # print(prefix)
    # print(goal)
    if min_diff == float('inf'):
        return -1
    elif min_diff == n:
        return -1
    return min_diff


    """
    find all the times that the goal appears in the code
    find the nearest 0 value to this value. 
    and then return the minimum difference between these index
    """

        

    """
    basic termination logic:
    1. if all are one value
    2. if they are already equal

    now, we get to cases where they are not equal, and both values are present
    what we need to remove:
    remove = abs(count_a - count_b)

    that is the bare minimum we want to remove. 
    now i suggest this. we set a prefix sum, to check which way the force is going. instead of using 
    abs value, it will go in negative for larger counts of b. 

    same in prefix sum. 
    then we can find a place where we can remove n elements. prefix sum will obviously take into account consecutive numbers


    there are also cases, where it is impossible to have the same number without removing all. 
    eg aabaa


    so here is this case
    -1 -2 -3 -2 -3

    there are no zeroes. but you can just remove -1 -2 -3 and get an answer. so it is not impossible




    """



t = int(input())
for _ in range(t):
    print(solve())
    # print()