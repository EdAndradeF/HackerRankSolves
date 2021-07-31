'''

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

'''


texto = 'WELCOME'
tamanho = list(map(int, input().split()))
c = '.|.'
f = '-'

for alt in range(tamanho[0]//2):
    print((alt*c).rjust(tamanho[1]//2-1, f)+(c)+(alt*c).ljust(tamanho[1]//2-1, f))

print(texto.center(tamanho[1], f))

for alt in range(tamanho[0]//2-1, -1, -1):
    print((alt*c).rjust(tamanho[1]//2-1, f)+(c)+(alt*c).ljust(tamanho[1]//2-1, f))
