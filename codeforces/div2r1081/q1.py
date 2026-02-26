def solve():
    n = int(input())
    a = input()
    ans = 1
    cont = False

    for i in range(1, n):
        if a[i] != a[i-1]:
            ans += 1
        else:
            cont = True
    
    if len(a) == len(set(a)):
        return ans
    
    if a[0] == a[-1]:
        return ans
    
    if cont:
        return ans+1
    
    return ans
    
    """
    abbc

    bccb - cbbc
    abbb - babb
    baabb - bbbaa, abbba, bbbaa, bbaab

    aabcbd - abcbda
    
    """

    if a[0] == a[-1]:
        return 




t = int(input())
for _ in range(t):
    print(solve())