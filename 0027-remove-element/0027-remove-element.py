class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        position = 0
        for n in range(len(nums)):
            if nums[n] != val:
                nums[position] = nums[n]
                position += 1
        

        return position