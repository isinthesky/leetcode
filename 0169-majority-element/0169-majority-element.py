class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half = len(nums) // 2
        nums.sort()


        return nums[half]
        