
from functools import cmp_to_key

def comp(a, b):
    if b[1] == a[1]:
        return a[0] - b[0]

    return b[1] - a[1]

def solution(N, stages):
    # N : 끝판 숫자
    # stage : 종료 스테이지
    # stages : 길이 유저 수

    quest = [0 for _ in range(N+1)]
    for stg in stages:
        quest[stg - 1] += 1

    user = len(stages)
    rate = []
    
    for stage in range(N):
        if quest[stage] == 0:
            rate.append((stage+1, 0))
        else:
            rate.append((stage+1, quest[stage] / user))

        user -= quest[stage]

    answer = []
    for f in sorted(rate, key=cmp_to_key(comp)):
        answer.append(f[0])
    
    return answer