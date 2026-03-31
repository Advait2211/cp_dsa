# https://codeforces.com/contest/1765/problem/M

"""
my logic: find the smallest prime factor, and then allot it in this way:
say the number given is 35
smallest prime factor is 5
35 / 5 = 7
 
therefore we will return 7, 7 * (5 - 1) = 7, 28
"""
def smallest_prime_factor(n):
    if n <= 1:
        return None
 
    if n % 2 == 0:
        return 2
 
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
 
    return n
 
 
def solve():
    num = int(input())
 
    spf = smallest_prime_factor(num)
    # print(spf)
    soln = num // spf
 
    print(soln, soln * (spf-1))
 
    
    
 
 
t = int(input())
 
for _ in range(t):
    solve()