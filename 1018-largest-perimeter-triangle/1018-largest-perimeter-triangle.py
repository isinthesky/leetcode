class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        b = len(nums)-1
        l = b-1
        r = b-2

        largest = 0

        nums.sort()

        while b > r :
            print(l,r, "b", b)
            if nums[b] < nums[l] + nums[r]:
                return sum(nums[r:r+3])

            b -=1
            l -=1
            r -=1
                
                
        
        print(largest)
        return largest