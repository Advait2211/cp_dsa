import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    a2 = sorted(a, reverse=True)
    b2 = sorted(b, reverse=True)
    c2 = sorted(c, reverse=True)

    """
    potential cases
    all 3 maxes are on individual indices - no problem
    2 maxes are on the same indice (multiple maxes may be present in the same array)
    all 3 maxes are on the same indice.

    2 maxes are on the same indice:
    we take the individual max - (oh, this may be lower than second lowest of some other array)

    a simplest algorithm would be to make a map with indices as keys. 
    with this structure:
    {
        indice:{
            a: maxval
            b: maxval
            (only )
        }
    }

    the problem basically boils down to having 9 numbers. 
    3 from each array. 
    and the goal is maximation of the sum, keeping in mind that they have to be from different indices
    and different arrays.
    
    a2[0], a2[1], a2[3]
    .....

    but this does not account for indices

    but how many combinations can we make with this?
    9c3 right? so we just check every combination, first check if it is valid and then return max of valid

    so basically i want to store all 9 in an array. they won't be just numbers. they will have 2 properties - 
    1. index
    2. source list

    if any of them match, that combination is invalid. 

    and we can just have a i, j, k loop to check all possible combinations

    the only bug i see in this question is that what if all numbers are the same? 
    like 100 100 100 100 
    something like that. is the system robust enough to deal with this as well? 
    well i suppose it should be since we are considering all combinations
    """

    a2 = sorted(enumerate(a), key=lambda x: x[1], reverse=True)
    b2 = sorted(enumerate(b), key=lambda x: x[1], reverse=True)
    c2 = sorted(enumerate(c), key=lambda x: x[1], reverse=True)

    # print(a2, b2, c2)

    top = [a2[0], a2[1], a2[2], b2[0], b2[1], b2[2], c2[0], c2[1], c2[2]]

    # print(top)
    max_sum = 0

    for i in range(3):
        for j in range(3, 6):
            for k in range(6, 9):
                # check if valid
                temp = [top[i][0], top[j][0], top[k][0]]
                temp = set(temp)
                if len(temp) == 3:
                    max_sum = max(max_sum, top[i][1] + top[j][1] + top[k][1])

    return max_sum

            








    


t = int(input())
for _ in range(t):
    print(solve())