class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split(' ') + s2.split(' ')
        wordDic = {}

        for word in words:
            if word in wordDic:
                wordDic[word] += 1
            else:
                wordDic[word] = 1

        res = []
        for key, value in wordDic.items():
            if value == 1:
                res.append(key)

        return res
