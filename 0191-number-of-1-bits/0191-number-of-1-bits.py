class Solution:
    def hammingWeight(self, n: int) -> int:
        digit = 1
        count = 0

        print(n)

        while n > 0 :
            if n & 1 :
                count += 1

            n >>= 1

        return count
