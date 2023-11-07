class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1

        # for pos in range(len(a)):
        #     if a[pos] != b[pos]:
        #         continue
        #     else:
        #         break

        return max(len(a),len(b))
