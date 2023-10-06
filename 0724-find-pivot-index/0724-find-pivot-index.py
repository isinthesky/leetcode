class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        for pos in range(len(nums)):
            leftSum = 0
            rightSum = 0

            if pos == 0:
                rightSum = sum(nums[1:])
            elif pos == len(nums) - 1:
                leftSum = sum(nums[:-1])
            else:
                leftSum = sum(nums[:pos])
                rightSum = sum(nums[pos+1:])
            
            print("pos", pos, leftSum, rightSum)
            
            if leftSum == rightSum:
                return pos

        return -1

            

            
    