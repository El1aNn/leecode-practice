from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0

        def trap_part(height):
            n = len(height)
            ans = 0
            st = []
            for l in height:
                while st and l >= st[0]:
                    h = st.pop()
                    if not st:
                        break
                    ans += (min(st[0], l) - h)
                st.append(l)
            return ans, st
        ans, st = trap_part(height)
        ans += trap_part(st[::-1])[0]
        return ans


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
