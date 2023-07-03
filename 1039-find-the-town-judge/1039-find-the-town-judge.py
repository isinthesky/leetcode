class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        people = []
        Trusted = [0] * (n+1)

        print(Trusted)
        
        for _ in range(1, n+1):
           people.append([0,0])

        for p, tout in trust:
            people[p-1][1] += 1
            people[tout-1][0] += 1

        num = 0
        for pp in people:
            num += 1
            if pp[0] == n-1 and pp[1] == 0:
                return num

        return -1
