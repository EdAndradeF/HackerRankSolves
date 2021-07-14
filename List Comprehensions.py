if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    arr = []
    # x=i=0 y=j=1 z=k=2
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                arr.append([i, j, k])
    k = []
    for i in arr:
        j = sum(i)
        if j != n:
            k.append(i)
    print(k)
