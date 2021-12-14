def solution(statues):
    nstatues = 0
    sortStatues = sorted(statues)

    for i in range(len(sortStatues) - 1):
        # print(i)
        if sortStatues[i + 1] - sortStatues[i] > 1:
            nstatues = nstatues + (sortStatues[i + 1] - sortStatues[i]) - 1

    return(nstatues)


