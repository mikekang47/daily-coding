from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            return float((nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2)
        else:
            return float(nums[len(nums) // 2])

s = Solution()
n = s.findMedianSortedArrays([1,2], [3,4])
print(n)
