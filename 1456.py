# 给你字符串 s 和整数 k 。
#
# 请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。
#
# 英文中的 元音字母 为（a, e, i, o, u）。

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        d = [char for char in s]
        p = ["a", "e", "i", "o", "u"]
        i = k - 1
        j = 0
        count = 0
        while i < len(s):
            if j == 0:
                for t in range(k):
                    if d[t] in p:
                        count += 1
            else:
                if d[j - 1] in p:
                    count -= 1
                if d[i] in p:
                    count += 1
            ans = max(ans, count)
            j += 1
            i += 1
        return ans


s = Solution()
print(s.maxVowels("leetcode", 3))
