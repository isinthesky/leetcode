class Solution:
    def checkRecord(self, s: str) -> bool:
        countA = 0
        countL = 0

        for pos, char in enumerate(s):
            if char == 'A':
                countA += 1
                if countA > 1:
                 return False

            if char == 'L':
                if countL == 0:
                    countL += 1
                elif s[pos-1] == 'L':
                    countL += 1
                    if countL > 2:
                        return False
            else:
                countL = 0

        return True
