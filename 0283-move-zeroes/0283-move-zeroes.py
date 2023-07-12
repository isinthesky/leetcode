class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in nums[:]:
            if 0 == i:
                nums.remove(0)
                count += 1
                continue

        nums += [0 for _ in range(count)]
    