import itertools

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        
        for n in range(len(nums)):
            comb = itertools.combinations(nums, n+1)

            for tup in comb :
                xor = 0

                for val in tup:
                    xor ^= val
                
                result += xor
        
        return result
