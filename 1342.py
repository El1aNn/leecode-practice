# 给你一个非负整数num ，请你返回将它变成0
# 所需要的步数。 如果当前数字是偶数，你需要把它除以2 ；否则，减去1 。
class Solution:
    def numberOfSteps(self, num: int) -> int:
        # M = 10e6 + 1
        # a = {}
        # a[1] = 1
        # a[2] = 2
        # for i in range(1, num + 1):
        #     if i not in a:
        #         if i % 2 == 0:
        #             a[i] = a[i / 2] + 1
        #         else:
        #             a[i] = a[i - 1] + 1
        # return a[num]
        def f(x):
            if x == 0:
                return 0
            else:
                if x % 2 == 0:
                    return f(x / 2) + 1
                else:
                    return f(x - 1) + 1
        return f(num)