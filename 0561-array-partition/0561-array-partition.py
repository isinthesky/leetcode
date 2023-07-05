class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        arr = []

        for pos in range(0, len(nums), 2) :
            arr.append(min(nums[pos], nums[pos+1]))
            
        print(sum(arr))

        return sum(arr)
        