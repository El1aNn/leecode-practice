from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) -> int:
            min_char = min(s)  # 找到字典序最小的字母
            return s.count(min_char) 
        ans = []
        f_word = []
        n = len(words)
        for s in words:
            f_word.append(f(s))
        f_word.sort()
        for s in queries:
            target = f(s)
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if f_word[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            ans.append(n - 1 - right)
        return ans
s = Solution()
print(s.numSmallerByFrequency(["bbb","cc"],["a","aa","aaa","aaaa"]))  # [1]