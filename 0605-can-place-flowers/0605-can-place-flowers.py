class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        length = len(flowerbed)
        count = 0

        for i in range(0, length):
            if flowerbed[i] == 0 and (True if i == 0 else flowerbed[i-1] == 0) and (True if i == length - 1 else flowerbed[i+1] == 0):
                count += 1 
                flowerbed[i] = 1

        return True if count >= n else False
