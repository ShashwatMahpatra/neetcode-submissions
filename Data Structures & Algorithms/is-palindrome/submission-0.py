class Solution:
    def isPalindrome(self, s: str) -> bool:
        array_of_s=[i.lower() for i in s if i.isalnum()]
        if (array_of_s==array_of_s[::-1]):
            return True
        else:
            return False

        