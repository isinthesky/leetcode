class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        arr = [0 for _ in range(n)]
        
        for k, v in edges:
            arr[v] += 1
            
        count = []
        
        for n, v in enumerate(arr):
            if 0 == v:
                count.append(n)
                
        return count
                