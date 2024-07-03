class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_no = str(x)
        if x < 0 :
            return False
        else :
            if (string_no==string_no[::-1]):
                return True 
            else :
                print("false")
