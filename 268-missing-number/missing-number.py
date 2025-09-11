class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        output = 0
        arr = []
        for i in range(len(nums)+1):
            arr.append(i)
        for i in range(len(nums)+1):
            if i not in nums:
                output = i
        return output

        