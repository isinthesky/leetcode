class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:

            half = (l + r) // 2

            if target == nums[half]:
                return half

            if r - l < 2:
                return -1

            if target < nums[half]:
                r = half
            else:
                l = half

        return -1
            



