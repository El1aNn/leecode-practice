import collections
from typing import List


# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         s = [0 for _ in range(len(nums))]
#         ans = 0
#         d = {}
#         dict = {}
#         s[0] = nums[0]
#         d[s[0]] = []
#         d[s[0]].append(0)
#         if 0 not in d:
#             d[0] = [-1]
#         else:
#             d[0].append(-1)
#         for i in range(1, len(nums)):
#             s[i] = s[i - 1] + nums[i]
#             if s[i] not in d:
#                 d[s[i]] = []
#                 d[s[i]].append(i)
#             else:
#                 d[s[i]].append(i)
#
#         for i in range(len(nums)):
#             if s[i] - k in d:
#                 for j in d[s[i] - k]:
#                     if k == 0:
#                         if j == -1:
#                             if 0 in dict:
#                                 dict[0] += 1
#                             else:
#                                 dict[0] = 1
#                         else:
#                             if j < i and s[j] in dict:
#                                 dict[s[j]] += 1
#                             elif j < i and s[j] not in dict:
#                                 dict[s[j]] = 1
#                     else:
#                         if j == -1:
#                             if 0 in dict:
#                                 dict[0] += 1
#                             else:
#                                 dict[0] = 1
#                         else:
#                             if j <= i and s[j] in dict:
#                                 dict[s[j]] += 1
#                             elif j <= i and s[j] not in dict:
#                                 dict[s[j]] = 1
#
#         return sum(dict.values())
#
#
# s = Solution()
# print(s.subarraySum([0, 0, 0], 0))

# from typing import List
#
#
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         sum = [0 for _ in range(len(nums))]
#         ans = 0
#         d = {}
#         sum[0] = nums[0]
#         d[sum[0]] = []
#         d[sum[0]].append(0)
#         if 0 not in d:
#             d[0] = [-1]
#         else:
#             d[0].append(-1)
#         for i in range(1, len(nums)):
#             sum[i] = sum[i - 1] + nums[i]
#             if sum[i] not in d:
#                 d[sum[i]] = []
#                 d[sum[i]].append(i)
#             else:
#                 d[sum[i]].append(i)
#
#         for i in range(len(nums)):
#             if sum[i] - k in d:
#                 for j in d[sum[i] - k]:
#                     if k == 0:
#                         if j < i:
#                             ans += 1
#                     else:
#                         if j <= i:
#                             ans += 1
#         return ans
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        presum = collections.defaultdict(int)
        presum[0] = 1
        cur_presum = 0

        for n in nums:
            cur_presum += n
            ans += presum[cur_presum - k]
            presum[cur_presum] += 1
        return ans


s = Solution()
print(s.subarraySum([1, 2, 3, -2, 5, -3, 2], 5))
