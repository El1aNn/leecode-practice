# 给你一个字符串 s，找到 s 中最长的回文子串。
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(self, s: str, left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        ans = ""
        for i in range(len(s)):
            one = expandAroundCenter(self, s, i, i)
            if len(one) > len(ans):
                ans = one
            two = expandAroundCenter(self, s, i, i + 1)
            if len(two) > len(ans):
                ans = two
        return ans

s = Solution()
print(s.longestPalindrome("d"))

