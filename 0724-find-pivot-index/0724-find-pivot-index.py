class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        length = len(nums)
        leftSum = 0
        rightSum = sum(nums[1:])

        if leftSum == rightSum:
                return 0

        for pos in range(1,length):
            leftSum += nums[pos-1]
            rightSum -= nums[pos]

            print("pos", pos, leftSum, rightSum)
            

            
            if leftSum == rightSum:
                return pos

        return -1            
    