# 给定两个字符串 s 和 t ，它们只包含小写字母。
#
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
#
# 请找出在 t 中被添加的字母。

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1 = list(s)
        t1 = list(t)
        d = {}
        for i in t1:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in s1:
            d[i] -= 1
            if d[i] == 0:
                d.pop(i)

        return list(d.keys())[0]


s = Solution()
print(s.findTheDifference("abcd", "abcde"))
