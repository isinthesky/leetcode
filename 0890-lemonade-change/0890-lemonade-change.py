class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = {5:0, 10:0, 20:0}

        for price in bills:
            if price in money:
                money[price] += 1

            print(money)

            if price == 10:
                money[5] -= 1

            if price == 20:
                if money.get(10) > 0:
                    money[10] -= 1
                    money[5] -= 1
                else:
                    money[5] -= 3

            for price, num in money.items():
                if num < 0:
                    return False
                
                
        return True
        
