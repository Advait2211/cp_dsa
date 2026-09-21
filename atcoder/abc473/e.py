import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    presum = [a[0]]
    mpsm = [0, a[0] % k]

    for i in range(1, n):
        presum.append(presum[i-1] + a[i])
        mpsm.append(presum[i] % k)


    # print(mpsm)

    s = set()
    ans = 0

    for i in range(n+1):
        if mpsm[i] in s:
            ans += 1
            s = set()

        s.add(mpsm[i])

        # print(s)

    return ans
    
    


t = 1
for _ in range(t):
    print(solve()) 