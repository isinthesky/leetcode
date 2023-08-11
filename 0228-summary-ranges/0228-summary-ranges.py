class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        res = []
        arr = []
        pos = -1
        past = -10
        
        for n in nums:
            if n != past+1:
                arr.append([])
                pos += 1
            
            arr[pos].append(n)
            past = n
            
        for item in arr:
            if len(item) < 2:
                res.append(str(item[0]))
            else:
                res.append(str(item[0]) + "->" + str(item[-1]))
                                
        return res
            
            