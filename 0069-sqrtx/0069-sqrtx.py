class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        half = x

        # while half * half > x :
        #     half = half // 2
        #     print(half, half * half)
        
        l = 1
        h = x

        # print(l,h,x)

        while l <= h :
            half = l + ((h - l) // 2)

            if half == x // half:
                return half

            elif half > x // half :
                h = half -1

            else:
                l = half + 1
            
        
        
        return h







