# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
from collections import defaultdict
from typing import List


# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         lp = len(p)
#         ans = []
#         i = 0
#         j = i + lp
#         k = 0
#         q = ''
#         sorted_p = ''.join(sorted(p))
#         while i < j:
#             q += s[k]
#             k += 1
#         sorted_q = ''.join(sorted(q))
#         if sorted_q == sorted_p:
#             ans.append(i)
#
#         return ans
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lp = len(p)
        ls = len(s)
        if lp > ls:
            return []
        ans = []

        dp = defaultdict(int)
        ds = defaultdict(int)
        for char in p:
            dp[char] += 1
        for char in s[0:lp]:
            ds[char] += 1
        if ds == dp:
            ans.append(0)
        for i in range(ls - lp):
            j = i + lp
            ds[s[i]] -= 1
            if ds[s[i]] <= 0:
                del ds[s[i]]
            ds[s[j]] += 1
            if ds == dp:
                ans.append(i + 1)

        return ans


s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))
