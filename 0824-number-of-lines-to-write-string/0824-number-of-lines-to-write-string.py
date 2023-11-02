class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        charDict = {}
        arr = [chr(x) for x in range(ord('a'), ord('z')+1)]
        
        for pos, width in enumerate(widths):
            charDict[arr[pos]] = width

        print(charDict)

        lines = 1
        strLength = 0
        for char in s:
            if strLength + charDict[char] > 100:
                lines += 1
                strLength = charDict[char]
            else:
                strLength += charDict[char]


        print("len", strLength)

        # lines = int(str(strLength)[:-2]) + 1 if strLength > 99 else 0

        return [lines, strLength]