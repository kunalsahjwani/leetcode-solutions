class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        total = len(nums)
        if total % 2 == 1:
            x = nums[total//2]
            return x
        else:
            middle1 = nums[total // 2 - 1]
            middle2 = nums[total // 2]
            y = (float(middle1) + float(middle2))/ 2
            return y
