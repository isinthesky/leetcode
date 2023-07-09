class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l = 0
        r = len(s)

        result = [0] * (len(s)+1)
        count = 0
        for ch in range(0, len(s)):
            if s[ch] == "I":
                result[count] = l
                l += 1
            else:
                result[count] = r
                r -= 1
            count += 1
        
        result[count] = l

        return result
