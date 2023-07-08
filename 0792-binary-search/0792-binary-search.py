class Solution:
    def search(self, nums: List[int], target: int) -> int:

        print(nums, target)
        
        def slideFunc(arr, num, pos)-> int:

            half = len(arr) // 2
            print(half, arr, pos)

            if arr[half] == target:
                return pos + len(arr) // 2

            if half < 1:
                return -1
            
            if arr[half] > target:
                return slideFunc(arr[:half], num, pos)
            else:
                return slideFunc(arr[half:], num, pos + half)

        print(slideFunc(nums, target, 0))
        return slideFunc(nums, target, 0)