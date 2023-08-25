class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        front = 0
        back = len(s)
        half = len(s) // 2

        while front < half:
            temp = s[front]
            s[front] = s[back-1]
            s[back-1] = temp

            front += 1
            back -= 1