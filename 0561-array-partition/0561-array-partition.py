class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        result = 0

        for pos in range(0, len(nums), 2) :
            result += min(nums[pos], nums[pos+1])
            
        return result
        