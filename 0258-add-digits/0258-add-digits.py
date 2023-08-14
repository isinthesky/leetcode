class Solution:
    def addDigits(self, num: int) -> int:
        def digitFunc(number: int)-> int:
            digit = 0
            for n in str(number):
                digit += int(n)
            return digit

        while num >= 10:
            num = digitFunc(num)

        return num
