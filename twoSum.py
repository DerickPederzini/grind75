from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            temp = target - nums[i]
            if h.get(temp) is not None:
                return [h.get(temp), i]
            if h.get(nums[i]) is None:
                h[nums[i]] = i
        return []

s = Solution()
print(s.twoSum(nums=[3,3], target=6))

