def solve():
    n = int(input())
    s = input()

    # print(s[1])

    for i in range(1, n-1):
        if s[i] in s[:i] or s[i] in s[i+1:]:
            # print(i)
            # print(s[i])
            # print(s[:i])
            # print(s[i+1:])
            return "Yes"
    return "No"




t = int(input())

for _ in range(t):
    print(solve())