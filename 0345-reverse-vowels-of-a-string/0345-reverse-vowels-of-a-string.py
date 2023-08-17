class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a","e","i","o","u","A","E","I","O","U"}        

        arr = []
        pos = []
        for p, ch in enumerate(s):
            if ch in vowels:
                pos.append(p)
                arr.append(ch)
            
        print(pos)
        print(arr)

        arrStr = list(s)

        for p in pos:
            arrStr[p] = arr.pop()


        res = ""
        for ch in arrStr:
            res += ch

        return res
            