class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        leng = len(nums)
        if leng < 3:
            return True

        pos = 0
        flow = None

        while pos < leng - 1:
            if nums[pos] < nums[pos + 1] :
                if flow == None:
                    flow = True
                elif flow == False:
                    return False
            elif nums[pos] > nums[pos + 1] :
                if flow == None:
                    flow = False
                elif flow == True:
                    return False
            pos += 1
        
        return True
