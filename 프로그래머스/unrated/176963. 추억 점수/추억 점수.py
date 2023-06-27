def solution(name, yearning, photo):
    answer = []
    pointDic = {}
    
    for n in range(len(name)):
        pointDic[name[n]] = yearning[n]
        
    point = 0;
    for r in photo:
        for c in r:
            if pointDic.get(c):
                point += pointDic[c]
            
        answer.append(point)
        point = 0;
        
    return answer