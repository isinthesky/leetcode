class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        resultTime = 0
        pre = timeSeries[0]

        for start in timeSeries[1:]:
            gap = start - pre

            if gap < duration:
                resultTime += gap
            else:
                resultTime += duration

            pre = start
        
        return resultTime + duration
        