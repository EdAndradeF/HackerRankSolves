
import math
import os
import random
import re
import sys



def solve(s):
    resultado = list(s)
    for words in resultado:
        resultado.replace(words, words.capitalize())

    return ' '.join(words.capitalize() for words in resultado)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
