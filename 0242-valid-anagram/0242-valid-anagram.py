class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}

        for ch in s:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1
        
        for ch in t:
            if ch in dic:
                if dic.get(ch) > 1:
                    dic[ch] -= 1
                else:
                    dic.pop(ch)
            else:
                return False

        return True if len(dic) < 1 else False
        
