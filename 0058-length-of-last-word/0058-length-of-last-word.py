class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start = 0
        end = 0
        togle = False
        
        def whiteSpace(char) -> bool:
            if char == " ":
                return True
            else:
                return False
            

        if not whiteSpace(s[0]):
            end += 1

        for n in range(1,len(s)):

            if whiteSpace(s[n-1]) and not whiteSpace(s[n]):
                start = n
                end = n

            if not whiteSpace(s[n]):
                end += 1

            
        return end - start
