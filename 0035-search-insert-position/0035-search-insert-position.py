class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s_pos = 0
        e_pos = len(nums)-1

        while s_pos <= e_pos:
            half_pos = (s_pos + e_pos) // 2

            if nums[half_pos] == target:
                return half_pos
            elif nums[half_pos] < target:
                s_pos = half_pos + 1
            else:
                e_pos = half_pos - 1

        return s_pos

        


                

        