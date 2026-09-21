import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if a.count(0) == 1:
        print("NO", end = "")
        return

    print("YES")

    if a.count(0) == 2:
        cnt = 0
        s = ["A", "B"]

        for i in range(n):
            if a[i] == 0:
                print(s[cnt], end = "")
                cnt = (cnt + 1) % 2
            else:
                print("C", end="")


        return
                
        
    
    cnt = 0
    s = ["A", "B", "C"]

    for i in range(n):
        if a[i] == 1:
            print("A", end = "")
        elif a[i] == 0:
            print(s[cnt], end = "")
            cnt = (cnt + 1) % 3
        else:
            print("B", end = "")

        
    


t = int(input())
for _ in range(t):
    solve()
    print()