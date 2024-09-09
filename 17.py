# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
from typing import List


class Solution:
    def __init__(self):
        self.ans = ''
        self.res = []
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits: str) -> List[str]:

        def backtrack(digits: str, index: int) -> None:
            if index == len(digits):
                self.res.append(self.ans)
                return
            for letter in self.letter_map[digits[index]]:
                self.ans = self.ans + letter
                backtrack(digits, index + 1)
                self.ans = self.ans[:-1]

        backtrack(digits, 0)

        return self.res
