class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        out = []
        for n in range(0, len(s) + 1):
            out.append(n)

        l = 0
        r = len(s)

        result = []
        for ch in s:
            if ch == "I":
                result.append(out[l])
                l += 1
            else:
                result.append(out[r])
                r -= 1

        result.append(out[l])

        return result
