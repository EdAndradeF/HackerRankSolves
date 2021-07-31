n = int(input())
lis = []
for _ in range(n):
    cmd, *args = input().split()
    if cmd !="print":
        cmd += f'({",".join(args)})'
        eval(f'lis.{cmd}')
    else:
        print(lis)
