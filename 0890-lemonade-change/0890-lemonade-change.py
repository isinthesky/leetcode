class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = [0,0,0]

        for price in bills:
            if price == 5:
                money[0] += 1
                continue
            elif price == 10:
                money[1] += 1
                money[0] -= 1
            else:
                money[2] += 1
                if money[1] > 0:
                    money[1] -= 1
                    money[0] -= 1
                else:
                    money[0] -= 3

            for num in money:
                if num < 0:
                    return False
                
        return True
        