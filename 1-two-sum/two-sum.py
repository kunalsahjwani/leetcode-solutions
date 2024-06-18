class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        noted = {}
        for i in range (len(nums)):
            diff = target - nums[i]
            if diff in noted :
                return [noted[diff], i]
            else :
                noted[nums[i]]=i
        