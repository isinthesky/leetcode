class Solution:
    def addBinary(self, a: str, b: str) -> str:

        length = max(len(a),len(b))
        
        for n in range(length - len(a)):
            a = "0" + a

        for n in range(length - len(b)):
            b = "0" + b

        result = ""

        bin = False
        for digit in reversed(range(length)):
            num = int(int(a[digit]) + int(b[digit]) + (1 if bin == True else 0))
            bin = True if num >= 2 else False

            result = str(num % 2) + result

        return "1"+result if bin else result
