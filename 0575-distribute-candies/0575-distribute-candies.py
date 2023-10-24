class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = set(candyType)

        result = min(math.floor(len(candyType)/2) , len(types))

        print("v",types)

        print(result)

        return result
