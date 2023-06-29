class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    #     position = len(digits) - 1
    #     dec = True
        
    #     while position >= 0:
    #         num = digits[position] + (1 if dec else 0)
    #         digits[position] = num % 10

    #         dec = True if num > 9 else False

    #         position -= 1
        
    #     if dec :
    #         digits.insert(0,1)
        
    #     return digits

        string = ""
        for num in digits:
            string += str(num)
        
        number = str(int(string)+1)

        arr = []

        for num in number:
            arr.append(int(num))

        return arr

