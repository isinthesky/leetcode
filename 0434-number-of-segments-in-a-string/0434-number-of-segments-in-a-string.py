class Solution:
    def countSegments(self, s: str) -> int:
        temp = ""
        white = True
        isString = False
        count = 0

        for ch in s:
            if ch == " ":
                white = True
            
            if ch != " " and white == True:
                print("22", ch, white)
                temp += ch
                white = False
                isString = True
                count += 1

        if isString == False:
            return 0
        else:
            return count
            