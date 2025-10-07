"""
abababa
aaaabbb
bbbaaaa
aabbbaa
abbbaaa
aaabbba
bbaaaab
baaaabb
"""

# nah, the intuition is to bring all 'a' or 'b' together. 

def solve():
    n = int(input())
    s = input().strip()

    posa = [i for i, ch in enumerate(s) if ch == 'a']
    posb = [i for i, ch in enumerate(s) if ch == 'b']

    def min_swaps(positions):
        if not positions:
            return float('inf')
        k = len(positions)
        median = positions[k // 2]
        target = [median - (k // 2) + i for i in range(k)]
        return sum(abs(p - t) for p, t in zip(positions, target))

    ans = min(min_swaps(posa), min_swaps(posb))
    return(ans)




t = int(input())

for _ in range(t):
    print(solve())