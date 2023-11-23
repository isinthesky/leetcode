class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def execBackspace(string: str):
            arr = []

            for pos, char in enumerate(string):
                if char == '#':
                    if len(arr) > 0:
                        arr.pop()
                else:
                    arr.append(char)

            return arr

        return True if execBackspace(s) == execBackspace(t) else False
