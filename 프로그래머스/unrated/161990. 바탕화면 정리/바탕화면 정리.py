def solution(wallpaper):
    l = 99
    t = 99
    r = 0
    b = 0

    for row in range(len(wallpaper)):
        for col in range(len(wallpaper[0])):
            if wallpaper[row][col] == "#":
                if t < row and l < col:
                    break
                if t > row:
                    t = row
                if l > col:
                    l = col

    for row in range(len(wallpaper)-1, -1, -1):
        for col in range(len(wallpaper[0])-1, -1, -1):
            if wallpaper[row][col] == "#":
                if b > row and r > col:
                    break
                if b < row:
                    b = row
                if r < col:
                    r = col

    return [t, l, b+1, r+1]