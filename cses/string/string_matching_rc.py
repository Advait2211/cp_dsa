
import sys
import math
input = sys.stdin.readline


def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m > n:
        return []

    MOD = (1 << 61) - 1   # Mersenne prime — very low collision chance
    BASE = 131

    # Precompute BASE^m mod MOD
    power = 1
    for _ in range(m):
        power = power * BASE % MOD

    # Hash the pattern and first window
    pat_hash = 0
    win_hash = 0
    for i in range(m):
        pat_hash = (pat_hash * BASE + ord(pattern[i])) % MOD
        win_hash = (win_hash * BASE + ord(text[i]))    % MOD

    results = []
    for i in range(n - m + 1):
        if win_hash == pat_hash:
            if text[i:i+m] == pattern:   # verify — guards against hash collision
                results.append(i)

        if i + m < n:
            # Roll the window: remove leftmost char, add next char
            win_hash = (win_hash * BASE - ord(text[i]) * power + ord(text[i+m])) % MOD

    return results


s = input()
t = input()

print(len(rabin_karp(s, t)))

