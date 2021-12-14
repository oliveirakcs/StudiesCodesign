def solution(inputArray):

    product = 0
    aux = 0
    maior = -1001

    for i in range(len(inputArray)-1):
        product = product + inputArray[i] * inputArray[i + 1]
        aux = aux + 1
        if product > maior:
            maior = product
        product = 0
    return(maior)
