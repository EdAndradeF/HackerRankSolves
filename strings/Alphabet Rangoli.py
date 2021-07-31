def print_rangoli(size):
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    ind = alpha[size-1::-1]
    if size == 1:
        print(alpha[0])

    for sq in range(size):
        print(('-'.join(ind[:sq])).rjust(size*2-3, '-')+'-'+('-'.join(ind[sq::-1])).ljust(size*2-1, '-'))

    for sq in range(size-2, -1, -1):
        print(('-'.join(ind[:sq])).rjust(size*2-3, '-')+'-'+('-'.join(ind[sq::-1])).ljust(size*2-1, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


