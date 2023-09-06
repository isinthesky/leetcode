class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        repeat = s[0]

        print(s[0], s[1:])

        
        for ch in s[1:]:
            if repeat[0] == ch:

                print("ok", len(s) % len(repeat))
                if (len(s) % len(repeat)) != 0:
                    print("AAA")
                    repeat += ch
                else:
                    print("repeat", repeat)
                    merge = set()
                    repeat_length = len(repeat)
                    for i in range(0, len(s), repeat_length):
                        merge.add(s[i:i+repeat_length])

                    print("merge",merge)
                    
                    if len(merge) == 1 :
                        return True
                    else:
                        repeat += ch

            else:
                print("BBB")
                repeat += ch

        return False