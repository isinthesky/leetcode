class Solution:
    def findCenter(self, edg: List[List[int]]) -> int:
        
        dic = {}
        for n, m in edg:
            if n in dic:
                return n
            else: 
                dic[n] = 1

            if m in dic:
                return m
            else: 
                dic[m] = 1

            