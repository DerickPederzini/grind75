class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count_s = {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)



        for c in t:
            if count_s.get(c) is None:
                return False
            count_s[c] -= 1
            if count_s[c] == 0:
                count_s.pop(c)

        return len(count_s) == 0



s = Solution()
s.isAnagram("anagram", "nagaram")