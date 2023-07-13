class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for n in nums:
            if n in dic:
                return True
            else:
                dic[n] = 1

        return False