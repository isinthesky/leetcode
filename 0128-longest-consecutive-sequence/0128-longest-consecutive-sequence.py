class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        st = set(nums)
        mx = 0
       
        for n in st:
            if n - 1 not in st:
                length = 1
                while n + length in st:
                    length += 1
                mx = max(mx, length)

        return mx
        