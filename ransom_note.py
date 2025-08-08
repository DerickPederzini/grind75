class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        h = {

        }

        for i in range(len(magazine)):
            if not h.get(magazine[i]):
                h[magazine[i]] = 1
            else:
                h[magazine[i]] += 1

        for i in range(len(ransomNote)):
            if ransomNote[i] not in h:
                return False

            h[ransomNote[i]] -= 1
            if h[ransomNote[i]] == 0:
                h.pop(ransomNote[i])

        return True



s = Solution()

print(s.canConstruct(ransomNote="aa", magazine="ab"))