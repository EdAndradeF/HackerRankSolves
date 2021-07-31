from random import randint


def print_formatted(number):
    lbin = len(bin(number).replace('0b', ''))

    for i in range(1, number + 1):
        deci = f'{i}'
        octa = oct(i).replace('0o', '')
        hexi = hex(i).replace('0x', '')
        bina = bin(i).replace('0b', '')
        print(f'{deci:>{lbin}} {octa:>{lbin}} {hexi.upper():>{lbin}} {bina:>{lbin}}')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)



