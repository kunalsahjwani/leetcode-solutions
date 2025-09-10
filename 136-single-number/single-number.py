class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0
        counts = Counter(nums)
        for key, value in counts.items():
            if value == 1:
                output = key

        return output
        