class Solution:

    def checkToeplitz(self, matrix: List[List[int]], x, y) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        posX = x
        posY = y
        
        value = matrix[posY][posX]

        print("check",x,y,value)

        while posX < col and posY < row:
            
            if value != matrix[posY][posX]:
                return False

            posX += 1
            posY += 1
        
        return True

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        size = min(row, col)

        for x in range(col-1):
            if False == self.checkToeplitz(matrix, x, 0):
                return False

        for y in range(row-1):
            if False == self.checkToeplitz(matrix, 0, y):
                return False
        
        return True
