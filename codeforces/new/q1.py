import math

def factors(n):
        a = n // 2
        b = n // 3
        c = n // 5
        d = n // 7

        ab = n // 6
        ac = n // 10
        ad = n // 14
        bc = n // 15
        bd = n // 21
        cd = n // 35

        abc = n // 30
        abd = n // 42
        acd = n // 70
        bcd = n // 105

        abcd = n // 210

        total = (a + b + c + d) - (ab + ac + ad + bc + bd + cd) + (abc + abd + acd + bcd) - abcd
        return total

def solve():
    start, end = map(int, input().split())
    # 2, 3, 5, 7
    return ((end - start + 1) - (factors(end) - factors(start - 1)))
    
    
 
 
t = int(input())
 
for _ in range(t):
    print(solve())