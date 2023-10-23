class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        result = [ "" for i in range(len(score)) ]
        ranker = {}
        
        for pos, point in enumerate(score):
            ranker[point] = pos
        
        sortedRanker = sorted(ranker.items(), reverse=True)

        for pos, value in enumerate(sortedRanker):
            result[value[1]] = str(pos + 1)

        for pos in range(3):
            if pos >= len(score):
                break
            result[sortedRanker[pos][1]] = rank[pos]

        return result
        