class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dicAdd = {}
        
        for n in nums:
            if n in dicAdd:
                dicAdd[n] += 1
            else :
                dicAdd[n] = 1
        
        dicSort = {}
        max = 0
        
        for key, num in dicAdd.items():
            if max <= num :
                max = num
                if num in dicSort:
                    val = dicSort.get(max)
                    if val < key :
                        dicSort[max] = key
                else :
                    dicSort[max] = key
                
                

        return dicSort.get(max)
