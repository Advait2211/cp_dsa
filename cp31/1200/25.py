import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    """
    a[j] - a[i] = j - i


    so difference between the pair of values should be the same as distance between the values

    can we use some modified two-sum approach?
    that would have worked, but that problem is we are not looking for a constant value. 
    the value may be between value - 1 to value - (index of value)

    so what can we do ?

    3 5 1 4 6 6
      4 5 6 7 8
        6 7 8 9
          2 3 4
            5 6
              7 

    aj - j = ai - i

    3 4 -1 1 2 1


    """

    for i in range(n):
        a[i] -= i

    from collections import Counter

    freq = Counter(a)

    soln = 0

    for key, value in freq.items():
        if value > 1:
            soln += (value * (value-1)) // 2

    return soln

    


    


t = int(input())
for _ in range(t):
    print(solve())