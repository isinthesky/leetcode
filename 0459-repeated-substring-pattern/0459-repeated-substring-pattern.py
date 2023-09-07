class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        repeat = s[0]
        
        for ch in s[1:]:
            if repeat[0] == ch:
                if (len(s) % len(repeat)) != 0:
                    repeat += ch
                else:
                    merge = set()
                    repeat_length = len(repeat)
                    for i in range(0, len(s), repeat_length):
                        merge.add(s[i:i+repeat_length])
                    
                    if len(merge) == 1:
                        return True
                    else:
                        repeat += ch
            else:
                repeat += ch

        return False
        