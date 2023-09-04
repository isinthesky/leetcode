class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        alen = len(num1)
        blen = len(num2)

        while alen != blen:
            if alen > blen:
                num2 = "0" + num2
                blen += 1
            else:
                num1 = "0" + num1
                alen += 1

        pos = alen
        dec = False
        result = ""

        while pos > 0:
            v, s = divmod(int(num1[pos-1]) + int(num2[pos-1]), 10)

            add = s + 1 if dec == True else s
            if add >= 10:
                v = 1
                add %= 10

            result = str(add) + result
            dec = True if v > 0 else False
            pos -= 1

        return  "1" + result if dec == True else result
