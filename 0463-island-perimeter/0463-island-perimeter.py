class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        gridSet = set()
        gridArr = []

        y_len = len(grid)
        x_len = len(grid[0])

        for n1, aa in enumerate(grid) :
            for n2, bb in enumerate(aa):
                if bb == 1:
                    gridSet.add(str(n1)+","+str(n2))
                    gridArr.append([n1,n2])

        def isNear(gridparam:List[List[int]], y:int, x:int) -> int:
            return 1 if gridparam[y][x] == 1 else 0
         
        count = 0
        for y, x in gridArr:
            
            if x > 0 :
                count += isNear(grid, y, x-1)
            
            if x < x_len-1 :
                count += isNear(grid, y, x+1)
                
            if y > 0 :
                count += isNear(grid, y-1, x)
                
            if y < y_len-1:
                count += isNear(grid, y+1, x)

        return len(gridArr) * 4 - count