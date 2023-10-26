class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        wordDict = {}
        
        for pos, word in enumerate(list1):
            wordDict[word] = pos + 10000

        print("w", wordDict)

        for pos, word in enumerate(list2):
            if word in wordDict:
                wordDict[word] = pos + wordDict[word] - 10000

        result = []
        index = math.inf

        for key, value in wordDict.items():
            print(key, value)
            if index > int(value):
                index = value
                result.clear()
                result.append(key)
                
            elif index == value:
                result.append(key)

        return result
        