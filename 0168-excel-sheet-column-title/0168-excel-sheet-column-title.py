class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        charArr = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        def subNumber(num: int):
            if num == 0 :
                return ""
            num -= 1
            return subNumber(num // 26) + charArr[num % 26]

        return subNumber(columnNumber)
