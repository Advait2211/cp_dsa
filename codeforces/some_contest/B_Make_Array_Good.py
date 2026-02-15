import math

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    print(n)

    for i in range(0, n):
        '''
        1011 -> 10000  - 1011
        '''

        print(i+1, 2 ** math.ceil(math.log2(a[i])) - a[i])

        # x = format(a[i], 'b')
        # y = len(x) - 1
        # soln = [1]
        # soln.append([0] * y)
        # print(soln)


t = int(input())

for _ in range(t):
    solve()