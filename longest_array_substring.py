import math


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        currWindow = 0

        hash = set()

        for char in range(len(s)):
            while s[char] in hash:
                hash.remove(s[currWindow])
                currWindow += 1

            hash.add(s[char])
            maxLength = max(maxLength, char - currWindow + 1)
        return maxLength






sol = Solution()

print(sol.lengthOfLongestSubstring("abcabcbb"))