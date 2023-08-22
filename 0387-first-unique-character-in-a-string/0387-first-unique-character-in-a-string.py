class Solution:
    def firstUniqChar(self, s: str) -> int:
        dictChar = {}
        arrChar = []

        for pos, ch in enumerate(s):
            if ch in dictChar:
                dictChar[ch] += 1
            else:
                dictChar[ch] = 1
                arrChar.append([pos, ch])

        result = -1

        for key in dictChar.keys():
            if dictChar[key] == 1:
                for p, c in arrChar:
                    if c == key:
                        return p

        return result
