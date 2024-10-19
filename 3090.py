# 给你一个字符串 s ，请找出满足每个字符最多出现两次的最长子字符串，并返回该子字符串的 最大 长度。
from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        d = defaultdict(int)
        ans = 0
        n = len(s)
        left = 0
        for i in range(n):
            d[s[i]] += 1
            while d[s[i]] > 2:
                d[s[left]] -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans


s = Solution()
print(s.maximumLengthSubstring("abcabcbb"))
