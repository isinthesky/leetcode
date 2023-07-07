class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = length = len(nums) - 1

        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        if i == 0: 
            nums.reverse()
            return 

        k = length

        while nums[i - 1] >=  nums [k]:
            k -= 1

        nums[i-1], nums[k] = nums[k], nums [i-1]

        l = i
        r = length

        while l < r :
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
