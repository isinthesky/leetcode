
class Solution:
    def wordCheck(self, lis: List[str],word: str)-> int:
        temp = list(lis)
        for i in word:
            if i in temp:
                temp.remove(i)
                if len(temp) == 0:
                    return 1
        return 0
        
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        arr = []
        minLen = inf
        res = ""
        for char in licensePlate:
            if (char>="A" and char<="Z") or (char>='a' and char<='z'):
                arr.append(char.lower())
        for char in words:
            if(Solution.wordCheck(self, arr, char)):
                if minLen > len(char):
                    minLen  =len(char)
                    res = char
        return res
