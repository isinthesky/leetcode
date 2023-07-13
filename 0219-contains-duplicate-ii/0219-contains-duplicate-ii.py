class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for n, v in enumerate(nums):
            if v in dic:
                print(abs(dic.get(v) - n))

                if abs(dic.get(v) - n) <= k:
                    return True 
                dic[v] = n
            else:
                dic[v] = n
        
