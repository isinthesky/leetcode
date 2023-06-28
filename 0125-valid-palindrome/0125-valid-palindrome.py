class Solution:
    def isPalindrome(self, s: str) -> bool:
        us = s.lower()
        l = 0
        r = len(s) - 1

        def isChar(c: str) -> bool:
            print("ccc",c, l, r)
            if 'a' <= c and 'z' >= c:
                return True
            else:
                return False


        while l < r:
            print("us", l, r)

            while l < r and us[l].isalnum() == False: 
                l += 1

            while r > l and us[r].isalnum() == False: 
                r -= 1
            
            print(l, r, us[l], us[r])
            if us[l] != us[r] or l > r:
                return False
            else:    
                l += 1
                r -= 1
            
        
        return True



        #   while l < r:
        #     print("us", l, r)
        #     if not isChar(us[l]) and l < r:
        #         print("aa", l, r)
        #         l += 1
        #         continue

        #     if not isChar(us[r]) and l < r:
        #         print("ss", l, r)
        #         r -= 1
        #         continue
            
        #     print(l, r, us[l], us[r])
        #     if us[l] != us[r] or l > r:
        #         return False
        #     else:    
        #         l += 1
        #         r -= 1
