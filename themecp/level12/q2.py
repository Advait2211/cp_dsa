# https://codeforces.com/problemset/problem/1847/B

"""

"""

# def solve():
#     n = int(input())
#     a = list(map(int, input().split()))

#     total_and = a[0]
#     for x in a[1:]:
#         total_and &= x

#     group_count = 0
#     current_and = a[0]

#     for i in range(1, n):
#         current_and &= a[i]
#         if current_and == total_and:
#             group_count += 1
#             if i < n - 1:
#                 current_and = a[i + 1]
#                 i += 1
#             else:
#                 break

#     return(group_count if total_and != 0 else group_count + 1)
            



# t = int(input())

# for _ in range(t):
#     print(solve())


for i in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	r = 0
	b = -1
	for i in range(n):
		b &= a[i]
		if b == 0:
			r += 1
			b = -1
	print(r if r > 0 else 1)