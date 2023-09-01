class Solution:
    def findComplement(self, num: int) -> int:
        compNum = 1 
        bitArr = []

        while compNum < num:
            bitArr.append(0 if compNum&num>0 else 1)
            compNum <<= 1

        compNum = 1 
        result = 0
        for bit in bitArr:
            result += compNum * bit
            compNum <<= 1
        
        return result
