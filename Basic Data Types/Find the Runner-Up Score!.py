if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = tuple(arr)
    #todo resolver com Tupla ou Set



def uno(arr):
    arr2 = list()
    for i in arr:
        if i in arr2:
            continue
        else:
            arr2.append(i)
    g = max(arr2)
    arr2.remove(g)
    g = max(arr2)
    print(g)
