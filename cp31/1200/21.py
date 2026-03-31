import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    """
    so they say
    ai * aj = i + j

    now cannot check all pairs. 

    q25 was something like this
    aj - ai = j - i
    which was translated to 
    aj - j = ai - i
    which then we could just subtract all indices to get permutations. 

    so here
    say you have ai and i 
    how would the eqn translate?

    ai = 3
    i = 1

    3 aj - 1 - j = 0
    or 
    3aj = 1 + j

    checking for all values would be too time consuming
    um wait. 
    can't we just solve it logically?

    3aj - 1 = j
    let aj = 1
    j = 2
    let aj = 2
    j = 5
    damn it. 

    ai = (i + j) / aj

    3 = (1 + j) / aj
    ai * aj = i + j

    (ai * aj) - i = j

    ai - i / aj = j / aj
    3 - 1 / aj = j / aj
    3 = j + 1 / aj

    ah fuck
    i got the solution
    infact i had gotten the solution 
    the very same. 
    but i missed this. 
    i thought you can repeat values something like 1 1 1 1 1 1 1 1
    but you can't therefore you reach a critical threshold soon

    dammit. 

    now implement without reading the solution
    """

    a = sorted(enumerate(a), key=lambda x: x[1])

    # print(a)
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            # print(a[i][1] * a[j][1])
            if a[i][1] * a[j][1] > 2 * n:
                break
            elif a[i][1] * a[j][1] == a[i][0] + a[j][0] + 2:
                
                cnt += 1


    return cnt

























    


t = int(input())
for _ in range(t):
    print(solve()) 