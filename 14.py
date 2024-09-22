from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        Min = 1000
        p = 0
        Strs = []
        ans = 0
        for i in range(len(strs)):
            Min = min(Min, len(strs[i]))
            j = []
            Strs.append(j)
            Strs[i] = list(strs[i])
        temp = Strs[0]
        for i in range(Min):
            count = 0
            for j in range(len(strs)):
                if temp[i] == Strs[j][i]:
                    count += 1
                else:
                    break
            if count == len(strs):
                ans += 1
            else:
                break

        return strs[0][:ans]


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
