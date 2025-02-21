from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st = []
        n = len(prices)
        # for i in range(n):
        #     while st and prices[st[-1]] >= prices[i]:
        #         l = st.pop()
        #         prices[l] -= prices[i]
        #     st.append(i)
        # return prices
        for i in range(n-1, -1, -1):
            while st and prices[st[-1]] > prices[i]:
                l = st.pop()
