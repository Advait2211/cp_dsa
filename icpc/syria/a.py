n, k = map(int, input().split())
a = list(map(int, input().split()))

prefix = []

for i in range(len(a)):
    if a[i] % k == 0:
        prefix.append(1)
    else:
        prefix.append(0)

# print(prefix)

pf2 = [0] * (n + 1)


for i in range(len(prefix)):
    pf2[i+1] = (pf2[i] + prefix[i]) % k

# print(pf2)
    

mapper = {0: 1}
solution = 0
 
for i in range(1, n + 1):
    val = pf2[i]
    solution += mapper.get(val, 0)
    mapper[val] = mapper.get(val, 0) + 1
 
print(solution)
