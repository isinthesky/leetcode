def solution(players, callings):
    run = {}

    for p in range(len(players)):
        run[players[p]] = p


    for call in callings:
        nTh = run[call]

        temp = players[nTh]
        players[nTh] = players[nTh-1]
        players[nTh-1] = temp

        run[call] = nTh - 1
        run[players[nTh]] = nTh

    return players
