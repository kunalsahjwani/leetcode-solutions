class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))  # convert to integer
        num += 1
        digits = [int(x) for x in str(num)]
        return digits
        