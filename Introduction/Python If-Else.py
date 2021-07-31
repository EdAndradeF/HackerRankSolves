import math
import os
import random
import re
import sys
from random import randint

if __name__ == '__main__':
    n = int(input().strip())
    #n = randint(1, 100)  # teste aleatório
    #print(n)             # Conferindo n

    if n == 2 or n == 3 or n == 5 or n == 7:
        print('Weird')

    elif n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
        print('Weird')

    elif n % 2 == 0:
        if n > 20:
            print('Not Weird')

        elif n == 4:
            print('Not Weird')

        elif n >= 6:
            print('Weird')
