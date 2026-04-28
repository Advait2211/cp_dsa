import sys
input = sys.stdin.readline

def solve():
    n, m, a, b = map(int, input().split())

    """
    basically the idea is simple
    we need to find if n, 2n, 3n, 4n mod a keeps giving different answers upto m.
    same goes for m, 2m, 3m, 4m mod b keeps giving different answers upto n.

    different as in, should repeat at some interval that is acceptable. 

    okay let us think of a brute force approach, then we will optimise it. 
    """

    """
    almost there
    only getting one answer wrong
    imma just wanna hard code and test tbh


    okay tried that and i feel like this is it
    so there is some specific case where n == m 
    as in the input number is a square. 
    when the number is a squre, i have found the answer to not work
    except when a == b == 1

    lemme see though


    """
    import math

    # for i in [m, n]:
    #     for j in [a, b]:
    #         if math.gcd(i, j) != 1:
    #             return "NO"
            
    # return "YES"

    

    if math.gcd(n, a) == 1 and math.gcd(m, b) == 1:
        # print(f"{math.gcd(n, m)=}")
        # print(f"{math.gcd(n, b)=}")
        # print(f"{math.gcd(m, a)=}")
        if math.gcd(n, m) <= 2:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"
    
    """
    why does the GCD approach seem so close and logical to the answer?
    if the GCD is not the same, then it means the LCM will be when the value 

    which means the value will not recur until you reach that point

    but somehow that fails on one test case. 

    okay
    i think the other values also have to be coprime. 
    i don't know the answer, but i just have the intuition that it is that. 
    so let us check pairs until we find the answer

    so both n, m gave gcd > 1

    so it is either one of those 2, or both. 
    imma just submit till i get it right

    
    sample test cases are more useful that we thought lol

    its clearly not both. 
    so let us try a combination that works. 
    gut feels tell that its n and b, m and a.
    """


    # arr = []
    # prev = 0
    # for i in range(1, n*m//2):
    #     prev = (prev + (n * i % a)) % n
    #     arr.append(prev)

    # # if 
    # print(arr)

    


t = int(input())
for _ in range(t):
    print(solve()) 