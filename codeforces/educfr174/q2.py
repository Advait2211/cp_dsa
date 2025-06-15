t = int(input())
from collections import Counter
import math



for _ in range(t):
    length = int(input())

    arr = list(map(int, input().split()))


    

    # ans = 0
    # ans1 = 0
    # ans2 = 0
    #
    # for i in range(len(arr)-3, 0, -1):
    #
    #     if arr[i] == 3:
    #         pass
    #     else:
    #         cur_freq = dict(Counter(arr[i + 1:]))
    #         print(cur_freq)
    #
    #         freq_1 = cur_freq.get(1, 1)
    #         freq_2 = cur_freq.get(2, 1)
    #         freq_3 = cur_freq.get(3, 1)
    #
    #         temp_ans = 0
    #
    #         if arr[i] == 1:
    #             if ans1 == 0:
    #                 ans1 = math.factorial(freq_1) + math.factorial(freq_2) + math.factorial(freq_3)
    #         elif arr[i] == 2:
    #             pass



