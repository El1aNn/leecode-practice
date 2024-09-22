# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。
#
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if word == s[i - len(word):i]: dp[i] = dp[i] or dp[i - len(word)]

        # for i in range(n):
        #     for j in range(i + 1, n + 1):
        #         if s[i:j] in wordDict:
        #             dp[j] = dp[j] or dp[i]

        # for j in range(1, n + 1):
        #     for word in wordDict:
        #         if j >= len(word):
        #             dp[j] = dp[j] or dp[j - len(word)] and word == s[j - len(word):j]

        return dp[-1]


s = Solution()
print(s.wordBreak("applepenapple", ["apple", "pen"]))
