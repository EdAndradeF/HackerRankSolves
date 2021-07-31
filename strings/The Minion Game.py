

def minion_game(string):
    vocais = 'AEIOU'
    # kevin {inicia com vogais}
    kevin_p = 0
    # stuart {inicia com consuantes}
    stuart_p = 0
    tamanho = len(string)
    # conta a quantidade de strings criadas a partir de cada letra
    # exp.: ABACAXI[0] = A; + AB; + ABA; + ABAC; (...) |
    #       ABACAXI[2] = A; + AC; + ACA; + ACAX; (...) |
    for c in range(tamanho):
        if string[c] in vocais:
            kevin_p += (tamanho-c)
        else:
            stuart_p += (tamanho-c)

    if kevin_p < stuart_p:
        print(f'Stuart {stuart_p}')
    elif kevin_p > stuart_p:
        print(f'Kevin {kevin_p}')
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
