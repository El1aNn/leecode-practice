# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长
# 子串的长度。
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        ans = 1
        i = 0
        d = {s[0]: 1}
        j = 1
        while j < len(s) and s[j] not in d:
            d[s[j]] = 1
            j += 1
        ans = max(ans, j - i)
        while i < j and j < len(s):
            while j < len(s) and s[j] in d:
                del d[s[i]]
                i += 1
            while j < len(s) and s[j] not in d:
                d[s[j]] = 1
                j += 1
            ans = max(ans, j - i)
        return ans


s = Solution()
print(s.lengthOfLongestSubstring("au"))
