from typing import List


class Solution:
    # My code
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)-1):
    #         for j in range(i+1, len(nums)):
    #             if nums[i]+ nums[j] == target:
    #                 return [i, j]

    # Best way
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        di = {}
        for x in range(len(nums)):
            if (target - nums[x]) in di:
                return [di[target - nums[x]], x]
            di[nums[x]] = x
        return []