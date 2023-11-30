class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        string = []

        for char in s:
            if char.isalpha() == True:
                string.append(char)

        res = ""
        for ch in s:
            if ch.isalpha() == True:
                res += string.pop()
            else:
                res += ch

        return res
        