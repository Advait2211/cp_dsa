def solve2():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    """
    damn this is a hard question

    problems:
    1. how do you decide which is the optimal prime number?
    2. which numbers to delete? 

    one important thing i got sorted, after deciding where to make all elements reach is that, we can only have that 
    element if it is greater than n * (n+1)

    oops that's wrong

    3 - minimum 12
    4 - minimum 16
    5 - minimum 20
    6 - minimum 24

    so basically the value has to be greater than n * 4 - checks out


    back to the original question. how to define n?

    n could start with the smallest value present. n cannot be smaller than the smallest value present right?
    this is assuming we don't delete the smallest value


    okay so we got this, 

    n is the smallest value in the range. 
    

    now to the next question. 
    which numbers should be deleted?


    ideally i would say the largest prime numbers should be deleted. 
    but in some cases we would have to delete the starting few numbers such that the largest numbers have the same GCD

    so the idea i have is this
    we sort the array
    we take the first element as the smallest or as the target gcd


    we iterate from the last element. 
    and check if they are greater than x (x = 4 * num)

    if they are, that means we can break them down into small enough pieces to use
    if we manage to iterate the entire array, then we delete the first element and repeat
    if we do not manage to iterate the entire array, we return 1



    ideas for the 3rd question, i was not able to implement it in time:

1. how do we find the optimal gcd?
2. ⁠which numbers to delete?

my answers

the smallest number could potentially be the optimal gcd, but we may delete the first element as well. for this, we use a loop, checking if more than k numbers (k is the number of elements we can delete) exist which are not reachable by element. 

an element is not reachable, if it is not dividable by n, not equal to 3 * n or smaller than 4 * n. 


now if this loop runs successfully for the smallest number, we try it for the second (till k)


and we store the max gcd reachable. ie the max value of n where all numbers are reachable
    """

    a = sorted(a)
    soln = 1
    
    for j in range(k+1):
        target = a[j] * 4
        count = 0

        i = j+1
        while i < n and a[i] < target:
            if a[i] % a[j] != 0:
                count += 1

            i += 1

        # if count > k and j == 0:
        #     return 1
        
        if count + j <= k:
            soln = a[j]
        
    
    return soln


from bisect import bisect_right

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    
    # Frequency map
    freq = {}
    for x in a:
        freq[x] = freq.get(x, 0) + 1
    
    # print(freq)
    
    ans = 1
    
    for g in range(2, n + 1):
        # Count numbers < 4*g
        count = bisect_right(a, 4*g - 1)
        
        # Subtract numbers that are multiples of g (g, 2g, 3g)
        for mult in range(1, 4):
            count -= freq.get(mult * g, 0)
        
        if count <= k:
            ans = g
    
    return(ans)




t = int(input())
for _ in range(t):
    print(solve())
    # print()


    