class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        if x < 4:
            return 1

        half = x

        while half * half > x :
            if half // 2 < 2:
                break
            half = half // 2
            # print(half, half * half)
        
        l = half
        h = half*half

        print(l,h,x)

        while l <= h :
            half = l + ((h - l) // 2)


            if half == x // half:
                return half

            elif half > x // half :
                h = half -1

            else:
                l = half + 1
            


            print("22",l,h,half)
        
        
        return h







