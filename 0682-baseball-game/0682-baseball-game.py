class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        
        for item in operations:
            if item == "C":
                arr = arr[:-1]
                continue

            if item == "D":
                double =  int(arr[len(arr) - 1]) * 2
                arr.append(double)
                continue

            if item == "+":
                plus = int(arr[len(arr) - 1]) + int(arr[len(arr) - 2])
                arr.append(plus)
                continue

            arr.append(int(item))

        return sum(arr)
        