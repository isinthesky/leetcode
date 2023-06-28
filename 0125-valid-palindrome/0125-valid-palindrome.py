class Solution:
    def isPalindrome(self, s: str) -> bool:
        us = s.lower()
        l = 0
        r = len(s) - 1

        def isChar(c: str) -> bool:
            if ('a' <= c and 'z' >= c) or ('0' <= c and '9' >= c):
                return True
            else:
                return False


        while l < r:
            while l < r and isChar(us[l]) == False: 
                l += 1

            while r > l and isChar(us[r]) == False: 
                r -= 1
            
            if us[l] != us[r] or l > r:
                return False
            else:    
                l += 1
                r -= 1
            
        return True
