import itertools

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        result = 0

        for n in range(len(nums)):
            comb = itertools.combinations(nums, n+1)
            print("n", n+1) 
            for tup in comb :
                print("t",tup) 
                xor = 0
                for val in tup:
                    xor ^= val
                    print("x", xor, "v", val) 
                
                result += xor

            print("r",result) 

        
        
        return result
