def solve():
    n = int(input())
    a = input()
    an = []

    """
    alright, time for intuition

    we can only have 2 elements back to back of the same type. 
    
    if the string is of even length, you cannot have 'aa' at the start

    similarly, if the string is of odd length, you cannot have 'bb' at the start

    another constraint to remember is that, where we have question marks, while we can put back both 'a' and 'b'
    the count(a) - count(b) == 1 if odd else 0

    whether it is an 'a' or 'b' cannot be determined just from the previous characters. future characters need to be 
    considered as well

    let us not think about that for a second, that seems like the wrong direction. 

    for each choice, you have 2 branches. is this like an dp question?
    like where there is a question mark, we try both, until we find a breaking point. else 

    ababab
    a?b?ba


    crutial observation. 
    if the number of ?s is even, then nothing matters
    if it is odd, then something might be changing
    """

    os = []

    for i in range(n):
        if i % 2 == 0:
            os.append('a')
        else:
            os.append('b')
        
        an.append(a[i])

    # print(os)
    # print(an)

    # l = 0
    # r = n-1
    # i = 0

    # while i < n:
        
    #     if an[i] == 'a':
    #         if os[l] == 'a':
    #             l += 1
    #         elif os[r] == 'a':
    #             r -= 1
    #         else:
    #             return "NO"
    #     elif an[i] == 'b':
    #         if os[l] == 'b':
    #             l += 1
    #         elif os[r] == 'b':
    #             r -= 1
    #         else:
    #             return "NO"
    #     else:
    #         cont = 0
    #         while i < n and an[i] == '?':
    #             cont += 1
    #             i += 1

    #         # i -= 1
    #         if i == n:
    #             return "YES"

    #         if cont % 2 == 0:
    #             l += cont
    #             continue
    #         else:

    #             # print(f"{an[i]=}")
    #             # print(f"{os[l+cont]=}")
    #             # print(f"{os[r]=}")
    #             # try moving left
    #             l2 = l + cont
    #             if an[i] == os[l2] or an[i] == os[r]:
    #                 l = l2
    #                 # print("hello")
    #                 continue


    #             # try moving right
    #             r2 = r - cont
    #             if an[i] == os[l] or an[i] == os[r2]:
    #                 r = r2
    #                 # print ("bye")
    #                 continue
                
    #             return "NO"


    #     i += 1

    # return "YES"

    """
    say you have odd length
    ababab

    frontier = first and last
    so making a standard case
    ababab - even
    ababa - odd, convert to abab - even, this can be done by checking the first element

    so now, your frontier is ab
    so basically you cannot have aa or bb in this. 
    you may have ab + ba but not in this indexing. 
    """

    i = 0

    if n % 2 != 0:
        if an[0] == 'b':
            return "NO"
        i += 1

    while i < n:
        if an[i] == 'a' and an[i+1] == 'a':
            return "NO"
        if an[i] == 'b' and an[i+1] == 'b':
            return "NO"
        
        i += 2

    return "YES"




    



t = int(input())
for _ in range(t):
    print(solve())