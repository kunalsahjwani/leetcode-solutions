class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums = []
        for i in range(m):
            nums.append(nums1[i])
        for i in range(n):
            nums.append(nums2[i])
        nums1[:] = nums
        nums1.sort()
        
        