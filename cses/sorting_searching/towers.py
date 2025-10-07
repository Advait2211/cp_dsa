import heapq

n = int(input())
a = list(map(int, input().split()))


heap = []

for x in reversed(a):
    if heap and heap[0] > x:
        heapq.heappop(heap)
    heapq.heappush(heap, x)

print(len(heap))



"""
3 8 2 1 5

5 
1 


3 8 1 2 5

5 8
2 3
1

6 3 5 4 1 2
2 4 5 
1 3 6


8 3 5 2 1



"""




