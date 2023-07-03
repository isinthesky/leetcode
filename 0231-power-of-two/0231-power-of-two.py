class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = 1

        while power <= n :
            if n == power :
                return True

            power <<= 1
        
        return False