# https://codeforces.com/problemset/problem/1986/D

"""
logic:

"""


def solve():
    n = int(input())
    a = input()

    if n == 2:
        return int(a)
    if n == 3:
        if a[0] == 0 or a[2] == 0:
            return 0
        if a[0] > a[1]:
            return int(a[0]) + 10 * int(a[1]) + a[2]
        else:
            return 10 * int(a[0]) + int(a[1]) + a[2]
        
    if '0' in a:
        return 0
    
    a = list(map(int, a))
    
    suma = [a[0]]

    for i in range(n-1):
        temp = suma[-1] + min(a[i]+a[i+1], a[i] * a[i+1])
        suma.append(temp)

    print(suma)
    

        



t = int(input())

for _ in range(t):
    print(solve())
