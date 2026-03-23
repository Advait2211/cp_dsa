import sys
input = sys.stdin.readline

"""
it will take only 2 moves as the maximum
you can literally do this using the last and the second last element and get guaranteed result


"""

def solve():
    n, t = input().split()
    n = int(n)
    s = input().strip()
    a = []
    seta = set()

    for c in s:
        a.append(c)
        seta.add(c)

    if len(seta) == 1 and next(iter(seta)) == t:
        print(0)
        return
    
    if a[-1] == t:
        print(1)
        print(n)
        return
    
    for i in range(n-1, -1, -1):
        if a[i] == t:
            break

    i += 1

    if i > n // 2:
        print(1)
        print(i)
        return
    
    # only case remains where there is not correct element in the second half. 
    # in this case, simply taking the last two elements would work

    print(2)
    print(n-1, n)
    # print()

    # print(i)

    # print(a)
    # print(seta)



    
    


t = int(input())
for _ in range(t):
    solve()