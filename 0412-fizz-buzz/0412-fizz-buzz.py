class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        result = []

        for i in range(1, n + 1):
            item = ''
            
            if i % 3 == 0:
                item += 'Fizz'
            
            if i % 5 == 0:
                item += 'Buzz'

            if item == "":
                item = str(i)

            result.append(item)

        return result         



                