def merge_the_tools(string, k):
    # k == tamanho de cada parte da string
    # t == o pedaco da string de tamanho k
    # u == a sting t sem chars repetidos sequenciado
    t = [] # <= desnecessario, apenas para melhor entendimento
    u = [] # <= paenas para controle

    for i in range(0, len(string), k):
        t.append(string[i:k+i])
        x = list(string[i:k+i])
        for c in range(k-1, -1, -1):
            if x[c] in x[:c]:
                x[c] = ''
        u.append(''.join(x))
    for i in u:
        print(i)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)