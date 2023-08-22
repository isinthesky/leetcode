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

        keys = dictChar.keys()


        result = -1
        print(dictChar, arrChar)

        for key in dictChar.keys():
            if dictChar[key] == 1:
                for p, c in arrChar:
                    print("arrchar", c, p)
                    if c == key:
                        return p


        # print(dictChar, arrChar)



        return result