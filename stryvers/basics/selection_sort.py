from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # selection sort
        for i in range(len(nums)):
            cur_min = i
            for j in range(i, len(nums)):
                if nums[j] < nums[cur_min]:
                    cur_min = j

            temp = nums[i]
            nums[i] = nums[cur_min]
            nums[cur_min] = temp

        return nums
