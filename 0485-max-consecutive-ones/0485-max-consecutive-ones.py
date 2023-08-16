class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        continu = 0
        mx = 0
        for n in nums:
            continu += 1
            
            if n == 0:
                continu = 0
                continue
            
            if continu > mx:
                mx = continu

        return mx
