class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rowLength = len(grid)
        colLength = len(grid[0])
        move = [(1,1),(-1,1),(1,-1),(0,1),(1,0),(-1,0),(0,-1),(-1,-1)]

        def dfs(arr, way):
            while len(way) > 0:
                item = way[0]

                for rr, cc in move:
                    if item[0] + rr < 0 or item[0] + rr >= rowLength: continue
                    if item[1] + cc < 0 or item[1] + cc >= colLength: continue
                    
                    if arr[item[0] + rr][item[1] + cc] == 0:
                        arr[item[0] + rr][item[1] + cc] = arr[item[0]][item[1]] + 1
                        way.append([item[0] + rr, item[1] + cc])

                way.remove(item)

        if grid[0][0] == 0:
            grid[0][0] = 1
            wway = [[0,0]]
            dfs(grid, wway)

            if rowLength > 1 and grid[rowLength-1][colLength-1] <= 1:
                return -1

            return grid[rowLength-1][colLength-1]
        else:
            return -1
