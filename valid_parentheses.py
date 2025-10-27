


class Solution:
    def isValid(self, s: str) -> bool:

        hash = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }
        stack = []

        for i in range(len(s)):
            if s[i] not in stack:
                stack.append(s[i])
            elif stack.pop() != hash[s[i]] or stack.count == 0:
                return False

        return True



s = Solution()

print(s.isValid("())"))