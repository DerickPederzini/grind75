from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) -1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                end = mid - 1

            if nums[mid] < target:
                start = mid + 1

        return -1

nums = [-1, 0, 3, 5, 9, 12]
target = 9

s = Solution()
s.search(nums, target)
