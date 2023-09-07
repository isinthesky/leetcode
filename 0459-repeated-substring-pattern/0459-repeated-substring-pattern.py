class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        repeat = s[0]
        s_length = len(s)
        
        for ch in s[1:]:

            if repeat[0] == ch:
                repeat_length = len(repeat)

                if repeat_length > s_length / 2:
                    return False

                if (len(s) % repeat_length) != 0:
                    repeat += ch
                else:
                    merge = set()
                    for i in range(0, len(s), repeat_length):
                        merge.add(s[i:i+repeat_length])
                    
                    if len(merge) == 1:
                        return True
                    else:
                        repeat += ch
            else:
                repeat += ch

        return False
