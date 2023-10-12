class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = [] 
        ss = 0

        odd = True
        for pos in range(0,len(s)-1,k):
            arr.append(s[pos:pos+k])
            ss = pos + k 

        if ss < len(s):
            arr.append(s[ss:len(s)])

        print(arr)

        result = ""
        odd = True
        for item in arr:
            result += item if odd == False else item[::-1]
            odd = not odd

        return result
