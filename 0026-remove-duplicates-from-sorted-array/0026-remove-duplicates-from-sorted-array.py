class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        length = 0

        for x in range(1, len(nums)):
            if nums[x - 1] == nums[x]:
                temp = 1
            else:
                length += 1
                nums[length] = nums[x]



        return length + 1


