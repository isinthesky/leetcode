class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visit = {}
        rowLength = len(grid)
        colLength = len(grid[0])
        count = 0
        
        def dfs(arr, row, col):
            if row < 0 or row >= rowLength: return
            if col < 0 or col >= colLength: return
            
            if arr[row][col] == "1":
                if not str(row)+","+str(col) in visit:
                    visit[str(row)+","+str(col)] = 1
                    
                    dfs(arr, row-1, col)
                    dfs(arr, row+1, col)
                    dfs(arr, row, col-1)
                    dfs(arr, row, col+1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if not str(row)+","+str(col) in visit:
                    if grid[row][col] == "1":
                        dfs(grid, row, col)
                        count += 1
                    
        return count
        