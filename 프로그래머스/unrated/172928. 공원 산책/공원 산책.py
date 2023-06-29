def solution(park, routes):
    start = [0, 0]
    H = len(park)
    W = len(park[0])

    for row in range(len(park)):
        print("rr", row)
        for col in range(len(park[row])):
            print("cc", park[row][col])
            if park[row][col] == 'S':
                start = [row, col]
                break

    def checkload(pos, v, count) -> bool:
        if (v == "E"):
            for step in range(count):
                if (int(pos[1])+1) > W-1:
                    return False
                if park[pos[0]][pos[1]+1] == "X":
                    return False
                pos[1] += 1
        elif (v == "S"):
            for step in range(count):
                if (int(pos[0])+1) > H-1:
                    return False
                print(pos, park)
                if park[pos[0]+1][pos[1]] == "X":
                    return False
                pos[0] += 1
        elif (v == "W"):
            for step in range(count):
                if (int(pos[1])-1) < 0:
                    return False
                if park[pos[0]][pos[1]-1] == "X":
                    return False
                pos[1] -= 1
        elif (v == "N"):
            for step in range(count):
                if (int(pos[0])-1) < 0:
                    return False
                if park[pos[0]-1][pos[1]] == "X":
                    return False
                pos[0] -= 1
        return True

    for move in routes:
        rem_w = start[1]
        rem_h = start[0]

        if move[0] == "E":
            if not checkload(start, "E", int(move[2])):
                start[1] = rem_w
        elif move[0] == "S":
            if not checkload(start, "S", int(move[2])):
                start[0] = rem_h
        elif move[0] == "W":
            if not checkload(start, "W", int(move[2])):
                start[1] = rem_w
        elif move[0] == "N":
            if not checkload(start, "N", int(move[2])):
                start[0] = rem_h

    return start
