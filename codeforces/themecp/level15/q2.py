# https://codeforces.com/problemset/problem/1788/B

"""
logic:

"""


def solve():
    n = int(input())
    
    a = n // 2

    if a % 10 == 9 and n % 2 == 1:
        # problem 1000 and 999
        test = 1
        val1 = 0
        val2 = 0
        nstring = str(n)
        for char in nstring:
            # print(char)
            temp = int(char)

            a = temp // 2
            b = temp - a
            # print(a, b)

            val1 *= 10
            val2 *= 10

            if test > 0:
                if b > a:
                    val1 += b
                    val2 += a
                    test *= -1
                if b == a:
                    val1 += b
                    val2 += a
            elif test < 0:
                if b > a:
                    val1 += a
                    val2 += b
                    test *= -1
                if b == a:
                    val1 += a
                    val2 += b

            
        print(val1, val2)

    else:
        b = n - a

        print(a, b)



t = int(input())

for _ in range(t):
    solve()
