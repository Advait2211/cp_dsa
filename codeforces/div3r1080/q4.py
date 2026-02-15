def solve():
    n = int(input())
    a = list(map(int, input().split()))

    """
    after creating tables, only 2 things remain to figure out
    what is the gain 
    like first and the last values are obviously going to be the sum of 1 to (n-1), which is simple to get by n * (n-1) // 2
    but what about the value after that? how much does it lose. 

    now that i think about it, does it really matter?
    can we just make equations to compute which value can give which from a smaller equation and then try on a larger situation
    and if it just works, we don't have to check that. if it doesn't work, we know what wrong if the code is correct

    (first + last) // (n-1)
    and the equation we get from this is 
    the sum of all a1 to an
    """

    """
    what we got from this is this
    first + last // (n-1)
    sum of all

    then for 8
    first + second last = last
    second + last = first

    third + seventh = second
    second + fifth = fourth

    for 6
    first + second last = last
    second + last = first

    second + fourth = fourth
    third + fifth = second
    second + fourth = fifth
    """


    total = (a[0] + a[-1]) // (n-1)

    print(total)

    first = ((a[1] + a[-1]) - (n-1)) // 2

    print(first)




t = int(input())
for _ in range(t):
    print(solve())