class Solution:
    def reverseBits(self, n: int) -> int:

        digit = 1
        number = n
        binary = ""
        test = ""
        multi = 0

        while number > 0:
            number, val = divmod(number, 2)
            binary = binary + str(val)
            
        for nn in range(32 - len(binary)):
            binary += "0"


        for bin in reversed(binary):
            test += bin
            multi += int(bin) * digit
            digit *= 2

        return multi
