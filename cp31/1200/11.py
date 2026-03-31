import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = input().strip()

    """
    basic observation says that first removal will have the cost i.
    the trouble begins from the second removal. 
    we need to find out, the removed indices are a part of to be removed indices

    we could compute factors, but that would be too expensive. 
    could we use a systen like sieve? 
    like mark the elements which have been cleaned in the array?

    um sieve would fit in the TC, but the problem with sieve would be that iit does not 
    find the cheapest replacement. like it would mark 6 as 2, but if 4 is not marked, then 2 is invalid
    
    can we use this observation?
    2 is only valid till 4, post that, it cannot be used.
    3 is only valid till 6 and so on. 
    so lifespan of a variable is the variable itself.
    which can be renewed if the relevent variable is in contact. 

    we can do reverse mapping
    so if we find an element, we can just map its x2 value. which would jjust end up being the cost. 

    beaut. this should work. 

    """
    # miss = [n+1] * (n+1)
    # cost = 0


    # for i in range(n):
    #     # print(f"{cost= }")
    #     if a[i] == '0':
    #         i += 1
    #         if i + i <= n:
    #             miss[i + i] = min(i, miss[i + i])
    #         if miss[i] != (n+1):
    #             cost += miss[i]
    #             if i + miss[i] <= n:
    #                 miss[i+miss[i]] = min(miss[i], miss[i+miss[i]])
    #         else:
    #             cost += i

    # print(miss)

    min_cost = [0] * (n + 1)

    for k in range(1, n + 1):
        j = k
        while j <= n:
            if a[j - 1] == '0':
                if min_cost[j] == 0:
                    min_cost[j] = k
                else:
                    min_cost[j] = min(min_cost[j], k)
                j += k
            else:
                break

    return sum(min_cost[i] for i in range(1, n + 1) if a[i - 1] == '0')

    


t = int(input())
for _ in range(t):
    print(solve()) 