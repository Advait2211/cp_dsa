import sys
input = sys.stdin.readline

"""
um so how would we solve it
quite an intriguing question

okay no yap

option 1:
find all palindromes in O(1) and then find the mex

option 2:
find what would lead to a large mex and then check if that is a palindrome


what we know is this:
one number can only come twice. 

and in order for it to have a large mex, it needs to have 0-1-2-3-4 and so on in it. 

so can we just have binary search on answers?
like a value would be possible

mmhmm, a part of a palimdrome would still be a palindrome. 
so if we say 4 is possible, that could also end up meaning 5 is possible

how would we write the helper function for this?
i don't think binary search is the optimal approach because there is this piece of information
"each piece only comes twice"

so for it to be a palindrome, either that value will come in the center and be once
or be equidistant from the center.

can we compute the distance between the same values and use that somehow?
we don't need to do that to all values

start off with 0

take this string
0 1 2 1 0 2
1 2 3 4 5 6

0 - 3
1 - 1
2 - 2



so there are a few cases:
take both zeroes
take first zero
take second zero

hmm we have 2 options:
write a checker function
or expand on this

lemme think on the checker function for a second

0 1 2 1 0 2
we have to check if 1 is possible
for that we just need to take 0, therefore possible

now to check for 2
okay that is not possible according to me

we have to use this information of the distance between the two values

okay so we take the difference between two zeros

ugh i cannot figure out which one would work
greedy or binary search on answerss

imma try binary search because i am not very sure i can do this using greedy
"""

from collections import defaultdict

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    pos = defaultdict(list)

    for i, val in enumerate(a):
        pos[val].append(i)

    # print(pos)

    # def check(mid):
    #     """
    #     the goal here is to check if this case be written properly
    #     0 1 2 1 0 2

    #     we need to find for say mid = 2

    #     how do we find if palindrome exists where mid = 2?
    #     oh oh ohhh

    #     so either 1 is in the middle
    #     or 1 is equidistant from some value
    #     and that value has to be the center
    #     f did i just find the greedy optimal solution?
    #     """
    #     low = pos[mid][0]
    #     high = pos[mid][1]

    #     print(mid)
    #     print(low, high)

    #     # we need to check if this value is the center value or not
    #     # we also need to check if all the values smaller than mid are present in the in palindrome

    #     # case 1: both are present in the palindrome
    #     diff = high - low
    #     check = set(range(mid + 1))

    #     if diff % 2 == 1: # one center element
    #         while high != low:
    #             if a[high] != a[low]:
    #                 return False
    #             check.remove(a[high])
    #     else: # two center elements
    #         pass


    #     return True

    # l = 1
    # r = n-1

    # while l <= r:
    #     mid = (l+r) // 2

    #     if check(mid):
    #         l = mid
    #     else:
    #         r = mid - 1

    #     break

    """
    we don't need binary search

    the logic is simple

    either both 0s are there, or they are not

    if both are there
    then:
    either again they are the center (if they are back to back)

    so basically our approach is to make the largest possible palindrome having both 0 and 1
    oh wait
    we will get stuck here
    """



    # case 1: both zeros are present in the palindrome
    low = pos[0][0]
    high = pos[0][1]
    diff = high - low

    mex = 0
    i = 0

    visited1 = set()

    while high >= low:
        visited1.add(a[high])
        # print(high, low)
        if a[high] != a[low]:
            # we have to check for single zero approach
            mex = 1
            break
        
        high -= 1
        low += 1

    if mex == 0:
        low = pos[0][0]
        high = pos[0][1]


        while high < (2 * n) and low >= 0:
            # print(high, low)
            if a[high] == a[low]:
                visited1.add(a[high])
                high += 1
                low -= 1

            else:
                break
        i = 1
        while i in visited1:
            i += 1

        mex = max(i, mex)

    # case 2: only 1 zero is involved. 
    # how do we tackle this case
    # one zero, ie that element is forced to be the center

    visited1 = set()
    # for the first zero
    low = pos[0][0] - 1
    high = pos[0][0] + 1
    

    while low >= 0 and high < (2 * n):
        if a[low] != a[high]:
            break

        visited1.add(a[high])
        high += 1
        low -= 1

    i = 1
    while i in visited1:
        i += 1

    mex = max(i, mex)



    visited1 = set()
    # for the first zero
    low = pos[0][1] - 1
    high = pos[0][1] + 1
    

    while low >= 0 and high < (2 * n):
        if a[low] != a[high]:
            break

        visited1.add(a[high])
        high += 1
        low -= 1

    i = 1
    while i in visited1:
        i += 1

    mex = max(i, mex)

    return mex



        

    


t = int(input())
for _ in range(t):
    print(solve()) 