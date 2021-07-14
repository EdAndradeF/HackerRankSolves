if __name__ == '__main__':
    scorelist = []
    namelist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        namelist.append(name)
        scorelist.append(score)


    s = scorelist.count(min(scorelist))

    while s > 0:
        g = scorelist.index(min(scorelist))
        scorelist.pop(g)
        namelist.pop(g)
        s -= 1

    lisfinal =[]
    s = scorelist.count(min(scorelist))
    while s > 0:
        g = scorelist.index(min(scorelist))
        scorelist.pop(g)
        lisfinal.append(namelist[g])
        namelist.pop(g)
        s -= 1

    lisfinal.sort()
    for _ in lisfinal:
        print(_)

