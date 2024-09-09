# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
from cmath import inf
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        # for c in t:
        #     dict[c] += 1
#         left, right = 0, 0

# #         lenght = inf
# #         pre_start = 0
# #         pre_end = 0

# #         def find(s, left, right):
# #             d = dict.copy()
# #             while left >= 0 and right < len(s) and d:
# #                 if s[left] in d:
# #                     d[s[left]] -= 1
# #                     if d[s[left]] == 0:
# #                         del d[s[left]]
# #                 if s[right] in d and left != right:
# #                     d[s[right]] -= 1
# #                     if d[s[right]] == 0:
# #                         del d[s[right]]
# #                 if not d:
# #                     return left, right
# #                 left -= 1
# #                 right += 1
# #             return -1, -1
# #         for i in range(len(s)):
# #             start, end = find(s, i, i)
# #             if lenght > end - start + 1 and start != -1 and end != -1:
# #                 pre_start, pre_end = start, end
# #                 lenght = end - start + 1
# #             start, end = find(s, i, i + 1)
# #             if lenght > end - start + 1 and start != -1 and end != -1:
# #                 pre_start, pre_end = start, end
# #                 lenght = end - start + 1
# #         return s[pre_start:pre_end+1] if lenght < inf else ''
        left = 0
        ans_left = -1
        ans_right = len(s)
        dict = Counter()
        d = Counter(t)
        less = len(d)
        for right, c in enumerate(s):
            dict[c] += 1
            if dict[c] == d[c]:
                less -= 1
                
            while less == 0:
                ## 存
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                
                ## 出
                x = s[left]
                if dict[x] == d[x]:
                    less += 1
                dict[x] -= 1
                left += 1
        return s[ans_left:ans_right+1] if ans_left != -1 else ''
            
#         return s[left + 1, right]
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         ans_left, ans_right = -1, len(s)
#         left = 0
#         cnt_s = Counter()  # s 子串字母的出现次数
#         cnt_t = Counter(t)  # t 中字母的出现次数
#         less = len(cnt_t)  # 有 less 种字母的出现次数 < t 中的字母出现次数
#         for right, c in enumerate(s):  # 移动子串右端点
#             cnt_s[c] += 1  # 右端点字母移入子串
#             if cnt_s[c] == cnt_t[c]:
#                 less -= 1  # c 的出现次数从 < 变成 >=
#             while less == 0:  # 涵盖：所有字母的出现次数都是 >=
#                 if right - left < ans_right - ans_left:  # 找到更短的子串
#                     ans_left, ans_right = left, right  # 记录此时的左右端点
#                 x = s[left]  # 左端点字母
#                 if cnt_s[x] == cnt_t[x]:
#                     less += 1  # x 的出现次数从 >= 变成 <（下一行代码执行后）
#                 cnt_s[x] -= 1  # 左端点字母移出子串
#                 left += 1  # 移动子串左端点
#         return "" if ans_left < 0 else s[ans_left: ans_right + 1]




s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
