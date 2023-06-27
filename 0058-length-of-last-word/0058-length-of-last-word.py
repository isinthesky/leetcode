class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start = len(s)
        end = len(s)
        lenn = False;
        
        def whiteSpace(char) -> bool:
            if char == " ":
                return True
            else:
                return False

        for n in reversed(range(len(s))):
            if lenn == False and not whiteSpace(s[n]):
                end = n
                start = n
                lenn = True
            
            if lenn == True and whiteSpace(s[n]):
                start = n+1
                break
            
            if lenn == True:
                start = n

        return (end - start) + 1
