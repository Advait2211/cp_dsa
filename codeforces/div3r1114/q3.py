import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = input()
    b = input()

    i1 = a.count('1')
    i0 = a.count('0')

    o1 = b.count('1')
    o0 = b.count('0')

    if i1 != o1:
        return "NO"

    iodd, ieven = 0, 0
    oodd, oeven = 0, 0

    for i in range(n):
        if a[i] == '1':
            if i % 2 == 0:
                ieven += 1
            else:
                iodd += 1

    for i in range(n):
        if b[i] == '1':
            if i % 2 == 0:
                oeven += 1
            else:
                oodd += 1


    if ieven == oeven:
        return "YES"
    return "NO"


    


t = int(input())
for _ in range(t):
    print(solve()) 