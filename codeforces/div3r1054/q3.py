# import psutil

# io = psutil.net_io_counters()
# print(f"Total Download: {io.bytes_recv/1024/1024:.2f} MB")
# print(f"Total Upload: {io.bytes_sent/1024/1024:.2f} MB")

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a_set = set(a)

    missing = 0

    for i in range(0, k):
        if i not in a_set:
            missing += 1

    return max(a.count(k), missing)




t = int(input())
for _ in range(t):
    print(solve())