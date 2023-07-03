class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        dicChar = {}
        count = 1

        for c in chars :
            dicChar[c] = count
            count += 1

        digit = 1
        number = 0
        
        for title in reversed(columnTitle):
            number += dicChar.get(title) * digit
            digit *= 26

        return number
