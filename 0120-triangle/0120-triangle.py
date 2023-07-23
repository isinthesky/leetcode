class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        length = len(triangle) - 1
        
        @cache
        def getmini(depth, index, leng) -> int:
            if depth < leng:
                return triangle[depth][index] + min(getmini(depth + 1, index, leng), getmini(depth + 1, index + 1, leng))
            else:
                return triangle[depth][index]

        return getmini(0, 0, length)
