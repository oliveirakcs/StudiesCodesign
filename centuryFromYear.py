def solution(ano):

    if (int(ano % 100)) == 0:
        seculo = int(ano / 100)
    else:
        seculo = int((ano / 100) + 1)

    return (seculo)

