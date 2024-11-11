# 给你整数 zero ，one ，low 和 high ，我们从空字符串开始构造一个字符串，每一步执行下面操作中的一种：

# 将 '0' 在字符串末尾添加 zero  次。
# 将 '1' 在字符串末尾添加 one 次。
# 以上操作可以执行任意次。

# 如果通过以上过程得到一个 长度 在 low 和 high 之间（包含上下边界）的字符串，那么这个字符串我们称为 好 字符串。

# 请你返回满足以上要求的 不同 好字符串数目。由于答案可能很大，请将结果对 109 + 7 取余 后返回。
from functools import cache


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1

        for i in range(1, high + 1):
            if i - zero >= 0:
                dp[i] += dp[i - zero]
            if i - one >= 0:
                dp[i] += dp[i - one]
            dp[i] %= MOD

        ans = 0
        for i in range(low, high + 1):
            ans += dp[i]
            ans %= MOD

    # @cache
    # def dfs(n):
    #     if n < 0:
    #         return 0

    #     return dfs(n - zero) + dfs(n - one)
    # for i in range(low, high + 1):
    #     a#     if n == 0:
    #         return 1ns += dfs(i) % (10 ** 9 + 7)

        return ans % (10 ** 9 + 7)
