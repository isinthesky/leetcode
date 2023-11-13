class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        left = 0 
        return_list = []
        s += '1'

        for index, letter in enumerate(s):
            if letter != s[left]:
                if index - left >= 3:
                    return_list.append([left, index - 1])
                left = index
        return return_list
               