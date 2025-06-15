import math

def solve():
    n = int(input())
    
    a = list(map(int, input()))
    b = list(map(int, input()))

    if 1 not in a:
        return True
    
    count1, count2 = 0, 0

    for i in range(0, n, 2):
        if a[i] == 1:
            count1 += 1
        if b[i] == 0:
            count2 -= 1

    for i in range(1, n, 2):
        if a[i] == 1:
            count2 += 1
        if b[i] == 0:
            count1 -= 1
    # print(count1, count2)
    if count1 <= 0 and count2 <= 0:
        return True
    else:
        return False
    

t = int(input())

for _ in range(t):
    if solve() == False:
        print("NO")
    else:
        print("YES")