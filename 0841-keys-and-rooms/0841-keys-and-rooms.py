class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        keys = {0:1}
        visit = []
        
        def enterRoom(room):
            while len(visit) > 0:
                curr = visit.pop()
            
                for v in room[curr]:
                    if not v in keys:
                        keys[v] = 1
                        visit.append(v)
            
        visit.append(0)
        enterRoom(rooms)
        
        return True if len(keys) == len(rooms) else False
            
            