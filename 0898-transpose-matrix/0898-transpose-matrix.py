
from collections import deque 

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        yLen = len(matrix)
        xLen = len(matrix[0])

        srcNumbers = deque() 

        for xPos in range(xLen):
            for yPos in range(yLen):
                srcNumbers.append(matrix[yPos][xPos])
             
        dstArr = []

        for yPos in range(xLen):
            arr = []
            for xPos in range(yLen):
                arr.append(srcNumbers.popleft())
            dstArr.append(arr)

        return dstArr




