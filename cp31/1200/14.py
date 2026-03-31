import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = [[0] * (n)] * n

    for i in range(n):
        a[i] = input().strip()

    # print(a)

    # print(type(a[0][0]))

    """
    for a 3x3
    00 02 22 20

    01 12 21 10

    fuck
    this was annoying
    took 20 mins
    but got it


    go from 00 to 0(n-1)

    and then 11 to 1(n-1-1)

    and so on till (n-1)//2

    ts took 44 mins. hard question. worth it. 
    """

    
    cost = 0
    for i in range(0, (n-1)//2+1):
        for j in range(i, (n-i-1)):
            p = int(i)
            q = int(j)
            z = 0
            o = 0
            for _ in range(4):
                if a[p][q] == '0':
                    z += 1
                else:
                    o += 1

                p, q = int(q), (n - 1 - p)
            # print(z, o)
            if z == o:
                cost += 2
            elif z == 4 or o == 4:
                pass
            else:
                cost += 1

    return cost
            


    # if n%2 == 1:
        # check if center
        # oh nvm it doesn't matter




    


t = int(input())
for _ in range(t):
    print(solve()) 