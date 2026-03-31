import sys
import math
input = sys.stdin.readline

def solve():
    n = int(input())
    
    if n % 2 == 0:
        print(-1, end=" ")
        return
    
    print(math.floor(math.log2(n)))
    bi = str(bin(n)[2:])
    # print(bi)

    for i in range(len(bi)-1):
        if  bi[i]== '1':
            print(2, end = " ")
        else:
            print(1, end = " ")

    

    


t = int(input())
for _ in range(t):
    solve()
    print()