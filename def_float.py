def isfloat(num):
    try:
        b = float(num)

    except:
        return False

    else:
        if b == 0:
            return False
        return True


if __name__ == '__main__':
    T = int(input())
    for n in range(T):
        N = input()
        print(isfloat(N))
