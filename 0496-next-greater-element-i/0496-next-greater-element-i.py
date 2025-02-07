class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = []

        for num in nums1:
            if not num in nums2:
                res.append(-1)
                continue

            idx = nums2.index(num)

            if idx == len(nums2) - 1:
                res.append(-1)
                continue

            arr = nums2[idx + 1:]

            add = False

            for it in range( len(arr)):
                if num < arr[it]:
                    res.append(arr[it])
                    add = True
                    break

            if add == False:
                res.append(-1)
        
        return res
