import time

s = '1234567890' * 10**4  # 100k characters

# Method 1: repeated int(s[i])
start = time.time()
total = 0
for i in range(len(s)):
    total += int(s[i])
print("Repeated int(s[i]) took:", time.time() - start)

# Method 2: map once
start = time.time()
digits = list(map(int, s))
total = sum(digits)
print("map(int, s) once took:", time.time() - start)
