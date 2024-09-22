# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
#
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# 要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：
#
# "AAJF" ，将消息分组为 (1 1 10 6)
# "KJF" ，将消息分组为 (11 10 6)
# 注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。
#
# 给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。
#
# 题目数据保证答案肯定是一个 32 位 的整数。
import string


class Solution:
    def numDecodings(self, s: str) -> int:
        str = [char for char in s]
        str_int = list(map(int, str))
        # d = {}
        # num = 1
        # letters = string.ascii_lowercase
        # for letter in letters:
        #     d[num] = letter
        #     num += 1
        if len(str_int) == 1:
            if str_int[0] == 0:
                return 0
            return 1
        if str_int[0] == 0:
            return 0
        else:
            dp = [0 for _ in range(len(str_int))]
            dp[0] = 1
            if str_int[1] == 0:
                if str_int[0] > 2:
                    return 0
                else:
                    dp[1] = 1
            else:
                if str_int[0] < 2 or (str_int[0] == 2 and str_int[1] < 7):
                    dp[1] = 2
                else:
                    dp[1] = 1
            for i in range(2, len(str_int)):
                if str_int[i] == 0 and (str_int[i - 1] > 2 or str_int[i - 1] == 0):
                    return 0
                else:
                    if str_int[i] == 0 and (str_int[i - 1] == 1 or str_int[i - 1] == 2):
                        dp[i] = dp[i - 2]
                    elif 0 < str_int[i - 1] < 2 or (str_int[i - 1] == 2 and str_int[i] < 7):
                        dp[i] = dp[i - 1]
                        dp[i] += dp[i - 2]
                    else:
                        dp[i] = dp[i - 1]
        return dp[-1]
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         if not s or s[0] == '0':
#             return 0
#
#         n = len(s)
#         dp = [0] * (n + 1)
#         dp[0], dp[1] = 1, 1
#
#         for i in range(2, n + 1):
#             if 1 <= int(s[i - 1]) <= 9:
#                 dp[i] += dp[i - 1]
#             if 10 <= int(s[i - 2:i]) <= 26:
#                 dp[i] += dp[i - 2]
#
#         return dp[n]

s = Solution()
print(s.numDecodings("2101"))
