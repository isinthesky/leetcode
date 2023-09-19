class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for order in moves:
            if order == "U":
                y += 1
                continue
            
            if order == "D":
                y -= 1
                continue
            
            if order == "L":
                x -= 1
                continue
            
            if order == "R":
                x += 1
                continue

        return True if x == 0 and y == 0 else False
