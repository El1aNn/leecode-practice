import bisect
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        ans = []
        for spell in spells:
            min_potion = (success + spell - 1) // spell
            ans.append(len(potions) - bisect.bisect_left(potions, min_potion))
        return ans


s = Solution()
print(s.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7))
