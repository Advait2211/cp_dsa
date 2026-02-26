def sieve(a, b_max):
    s = [0] * (b_max+1)

    for i in a:
        for j in range(i, b_max + 1, i):
            s[j] += 1

    return s



def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    s = sieve(set(a), max(b))
    cnt = 0

    # how many of alice's elements, can bob steal?
    # so basically we have to find number of pairs where y is divisible by some x
    # but not some other x. and that other x can be used to capture that value in bob's favour
    # alice plays first, so she will capture a value that can be shared. 
    x = len(set(a))
    shared = 0
    for val in b:
        if s[val] > 0 and s[val] < x:
            shared += 1
        elif s[val] > 0:
            cnt += 1
        

    acnt = m - (cnt + shared)

    cnt += 1 if shared % 2 == 1 else 0

    if cnt > acnt:
        return "Alice"
    else:
        return "Bob"


    



t = int(input())
for _ in range(t):
    print(solve())