# import math

# n, q = map(int, input().split())
# a = list(map(int, input().split()))


# val = 0
# maxval = math.floor(math.log2(n))
# arr = [[0]*n for _ in range(maxval)]
# # print(maxval)

# for i in range(maxval+1):
#     arr.append([])
#     skip = 2 << i
#     for j in range(n - skip + 1):
#         mini = a[j]
#         # base case: single elements
#         if i == 0:
#             arr[i].append(a[j])
#         else:
#             half = skip >> 1
#             arr[i][j] = \
#                         min(
#                             arr[i-1][j],
#                             arr[i-1][j + 2 ** (i-1)]
#                         )

# # print(arr)

# # for _ in range(q):
# #     l, r = map(int, input().split())
# #     l-= 1
# #     r-= 1
# #     diff = r - l + 1
# #     difflog = math.floor(math.log2(diff))
# #     ddiff = diff - (2 ** difflog)

# #     # print(diff, difflog, ddiff)
    
# #     mini = arr[difflog][l]
# #     for i in range(ddiff):
# #         mini = min(mini, arr[difflog][l+i])

# #     # print(f"{mini=}")
# #     print(mini)

import math

n, q = map(int, input().split())
a = list(map(int, input().split()))

maxval = math.floor(math.log2(n))
arr = [[0]*n for _ in range(maxval + 1)]

for i in range(maxval + 1):
    skip = 1 << i

    for j in range(n - skip + 1):

        if i == 0:
            arr[i][j] = a[j]

        else:
            half = skip >> 1
            arr[i][j] = min(
                arr[i-1][j],
                arr[i-1][j + half]
            )

for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1

    length = r - l + 1
    k = math.floor(math.log2(length))

    print(min(arr[k][l], arr[k][r - (1<<k) + 1]))