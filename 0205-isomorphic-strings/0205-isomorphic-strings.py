class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_arr = ""
        t_arr = ""

        sDic = {}
        tDic = {}
        
        for char in s:
            if not char in sDic:
                sDic[char] = hex(len(sDic))
            
            s_arr += sDic.get(char)

        for char in t:
            if not char in tDic:
                tDic[char] = hex(len(tDic))
                
            t_arr += tDic.get(char)

        return True if s_arr == t_arr else False
