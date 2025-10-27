

class Solution:
    def isPalindrome(self, s: str) -> bool:


        e = s.replace(" ", "").upper()
        e = s.replace("_", "").upper()

        i = 0
        j = len(e) - 1

        while i < j:
            l = e[i]
            r = e[j]

            if not l.isidentifier() and not l.isdigit():
                i += 1
            elif not r.isidentifier() and not r.isdigit():
                j -= 1
            else:
                if l != r:
                    return False
                i += 1
                j -= 1

        return True



s = Solution()
print(s.isPalindrome(s = "a.b,."))