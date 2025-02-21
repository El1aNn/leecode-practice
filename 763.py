from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        end = {}
        ans = []
        for i, st in enumerate(s):
            end[st] = i
        i = 0
        while i < n:
            e = end[s[i]]
            while i < e:
                i += 1
                i = end[s[i]]
                e = max(e, i)
            ans.append(e)
            i = e + 1
        return ans


s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))
