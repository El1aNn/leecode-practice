class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n - 1, 1, -1):
            left = i
            a = 0
            b = 0
            c = 0
            while a*b*c == 0:
                if s[left] == 'a':
                    a = 1
                elif s[left] == 'b':
                    b = 1
                else:
                    c = 1
                if left > 0 and a*b*c == 0:
                    left -= 1
                else:
                    break
            if left == 0 and a*b*c == 0:
                continue
            ans += (left + 1)
        return ans


s = Solution()

print(s.numberOfSubstrings("aaacb"))
