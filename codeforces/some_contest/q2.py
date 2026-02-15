def mex(s):
    m = 0
    while m in s:
        m += 1
    return m

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # 0 1 2
    """
    from the information given we know for sure the final array will be of length k - 1
    the largest possible solution would be k

    so we need to check if we can reach upto that either from 0 or from 1
    because otherwise we will run into TLE finding the best MEX with n sq time complexity.

    this is multi objective. we also want to find the best MEX solution, but we will be eliminating the best 
    n - k + 1 solutions. until it is not possible

    
    okay so that approach of unique elements does not hold

    """
    # if unique elements > available elements
    # sett = set(a)
    # if len(sett) <= k:
    #     a = sorted(a)
    #     return mex(set(a[:k]))

    

    # # if not, we start deleting larger elements
    # # we need to delete diff number of elements
    # # how many last elements do we want to delete?
    # # total n elements. we delete diff duplicates first
    # # 

    # duplicates = n - len(sett)
    # arr = list(sett)
    # arr.sort()
    # # elements to be deleted are n - d - k + 1
    # delete = n - duplicates - k + 1
    # # print("array", arr)
    # arr = arr[:-(delete-1)]
    # # print("array", arr)
    # sett = set(arr)

    # return mex(sett)


    # a = sorted(a)

    # if val is less than k, and its frequency is more than 1, decrement ans by 1
    # if val is greater than equal to k, it is better
    # so we just need to check how many elements less than k are duplicates - ie taking up space
    # ans = k
    # # soln = []

    # for i in range(1, min(k+1, n)):
    #     if a[i] == a[i-1]:
    #         if a[i] < k:
    #             ans -= 1

    # ans = max(1, ans)
    # return min(ans, mex(a))

    # major observation - order does not matter

    from collections import Counter
    # freq = Counter(a)
    # val = 0
    # k2 = k
    # total = 0

    # while k > 0:
    #     if freq[val] < k:
    #         freq[val] = 1
    #         k -=1
    #         val += 1
    #     else:
    #         break
    
    # val = 0
    # while total < k2:
    #     total += freq[val]
    #     if total == k2:

    #     val += 1
    # print(freq)


    """
    bohot bakchodi hogayi yeh question kyu nahi ho raha


    In the end, you will have only k-1 elements
    the maximum answer can be k

    so the goal is to have 1 element of all the values less than k, such that the answer will be k
    
    if we have a missing value, we simply break and return and say that will be the answer, since 
    the answer cannot be larger than that

    what if we have duplicates?
    well we can delete duplicates - as long as we satisfy the maximum mex criteria.

    """


    freq = Counter(a)

    used = 0
    mex = 0

    while True:
        if freq[mex] == 0:
            break
        if used + 1 > k - 1:
            break
        used += 1
        mex += 1

    return(mex)




    



t = int(input())
for _ in range(t):
    print(solve())