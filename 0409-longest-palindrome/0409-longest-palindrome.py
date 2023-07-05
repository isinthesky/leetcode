class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        dic = {}

        for char in s:
            if char in dic:
                dic[char] += 1
            else :
                dic[char] = 1

        length = 0
        odd = False

        for char, num in dic.items():
            if num % 2 == 1:
                odd = True
                length += (num - 1)
            else:
                length += num
            

        return length + ( 1 if odd == True else 0 )
                