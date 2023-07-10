class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        b = len(nums)-1

        nums.sort()

        while b > 1 :
            if nums[b] < nums[b-1] + nums[b-2]:
                return sum(nums[b-2:b+1])

            b -= 1
                
        return 0