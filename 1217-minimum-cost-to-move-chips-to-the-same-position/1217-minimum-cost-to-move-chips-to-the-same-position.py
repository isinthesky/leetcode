class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:

        arr = [0,0]
        
        for v in position:
            arr[v%2] += 1

        return min(arr[0], arr[1])
    