# 这里有 n 个一样的骰子，每个骰子上都有 k 个面，分别标号为 1 到 k 。
#
# 给定三个整数 n、k 和 target，请返回投掷骰子的所有可能得到的结果（共有 kn 种方式），使得骰子面朝上的数字总和等于 target。
#
# 由于答案可能很大，你需要对 109 + 7 取模。

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # 先剪枝
        if not (n <= target <= n * k):
            return 0
        mod = 10 ** 9 + 7
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                for f in range(1, k + 1):
                    if j - f >= 0:
                        dp[i][j] += dp[i - 1][j - f]
        return dp[-1][-1] % mod


s = Solution()
p = 1
a = 3
p = (p + a) % 2
print(p)
