# 给定一个单词列表 words 和一个整数 k ，返回前 k 个出现次数最多的单词。
#
# 返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率， 按字典顺序 排序。
import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        ans = []
        count = 0
        for word in words:
            if word not in d:
                d[word] = -1
            else:
                d[word] -= 1
        tuple_list = [(value, key) for key, value in d.items()]
        heapq.heapify(tuple_list)
        while (count < k) and tuple_list:
            a = heapq.heappop(tuple_list)
            ans.append(a[1])
            count += 1

        return ans


S = Solution()
print(S.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
