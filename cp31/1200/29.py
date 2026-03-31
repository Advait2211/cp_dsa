import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    k -= 1

    """
    cat A will follow the standard way of going around things
    cat B will be the one skipping an idx

    so when will it skip an idx?
    B _ _ _ A

    _ B _ A _  1
    _ _ A B _  2*
    _ A _ _ B  3
    A B _ _ _  4*
    _ _ B _ A  5

    every n // 2 moves B will skip a place

    so essentially be will travel k + (k // n // 2) % n

    except the only problem being if the last place is also divisible
    then what to do

    B A 1
    A B 2
    B A 3

    1 + 1 // 2 // 2 % 2 = 0
    2 + (2 // 2 // 2) % 2 = 0

    if k % (n // 2) == 0:
        in this case, exactly at that location. then i suppose we can add another value

    nope. 

    B _ A

    _ A B *
    A B _ *
    _ B A *

    _ A B
    A B _ *
    _ B A *


    """

    if n % 2 == 0:
        soln = k % n + 1
    else:
        soln = (k + (k // (n // 2))) % n + 1

    # soln += 0 if k % (n // 2) else 1
    return soln
    


t = int(input())
for _ in range(t):
    print(solve()) 