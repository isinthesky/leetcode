class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num.reverse()
        arrNumber = list(str(k))
        arrNumber.reverse()
        
        leng1 = len(num)
        leng2 = len(arrNumber)
        leng = max(leng1, leng2)

        while leng1 != leng2:
            if leng1 > leng2:
                arrNumber.append(0)
                leng2 = len(arrNumber)
            else:
                num.append(0)
                leng1 = len(num)

        dec = 0
        pos = 0
        resArr = []

        while leng > pos :
            sum = num[pos] + int(arrNumber[pos]) + dec

            if sum > 9:
                resArr.append(sum - 10)
                dec = 1
            else:
                resArr.append(sum)
                dec = 0

            pos += 1

        if dec == 1:
            resArr.append(1)

        resArr.reverse()

        return resArr
