class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = {}
        for n in nums:
            if n in map:
                map.pop(n)
            else:
                map[n] = 1
        
        for key in map:
            return key
