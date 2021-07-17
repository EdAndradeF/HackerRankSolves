def swap_case(s):
    invert_letra = ''
    for letra in s:
        if letra == ' ':
            invert_letra = invert_letra + letra
        elif letra == letra.lower():
            invert_letra = invert_letra + letra.upper()
        elif letra == letra.upper():
            invert_letra = invert_letra + letra.lower()
    return invert_letra


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
