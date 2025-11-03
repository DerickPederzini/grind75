


class Solution:
    def isValid(self, s: str) -> bool:

        hash = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }
        stack = []

        for i in range(len(s)):
            if s[i] not in hash.keys():
                stack.append(s[i])
            elif  len(stack) == 0 or stack.pop() != hash[s[i]] :
                return False

        return len(stack) == 0



s = Solution()

print(s.isValid(")"))