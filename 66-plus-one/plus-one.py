class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit
        # for i in range(len(digits) - 1, -1, -1):
        #     if digits[i] < 9:
        #         digits[i] += 1
        #         return digits  # Done, no carry needed
        #     digits[i] = 0  # Set to 0 and carry to next digit
        
        # # If all digits were 9, we need an extra 1 at the front
        # return [1] + [0] * len(digits)


        right = len(digits) -1
        for i in range(right, -1 , -1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i] =0

        return [1] + [0] * len(digits)
