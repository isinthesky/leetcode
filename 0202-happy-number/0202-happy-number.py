class Solution:
    def isHappy(self, n: int) -> bool:
        
        num = str(n)

        while True :
            sum = 0
            
            for n in num:
                sum += int(n) * int(n)
            
            if sum < 5 :
                break

            num = str(sum)

        if sum == 1 :
            return True
        else :
            return False
