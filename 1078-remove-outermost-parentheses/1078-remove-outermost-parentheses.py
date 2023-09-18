class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        arr1 = []
        result = ""

        for ch in s:
            if ch == "(":
                arr1.append("(")
                if len(arr1) > 1:
                    result += ch
            else:
                arr1.pop()
                if len(arr1) > 0:
                    result += ch
                
        return result
             
                
                