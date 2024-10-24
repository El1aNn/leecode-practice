# 给你一个下标从 0 开始的字符串 s ，这个字符串只包含 0 到 9 的数字字符。

# 如果一个字符串 t 中至多有一对相邻字符是相等的，那么称这个字符串 t 是 半重复的 。例如，"0010" 、"002020" 、"0123" 、"2002" 和 "54944" 是半重复字符串，而 "00101022" （相邻的相同数字对是 00 和 22）和 "1101234883" （相邻的相同数字对是 11 和 88）不是半重复字符串。

# 请你返回 s 中最长 半重复
# 子字符串
#  的长度。
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        same = 0
        for right in range(len(s)):
            if right > 0 and s[right] == s[right - 1]:
                same += 1
            while same > 1:
                if s[left] == s[left + 1]:
                    same -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
