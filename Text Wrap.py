import textwrap

def wrap(string, max_width):
    lista = textwrap.wrap(string, max_width)
    txt = ''
    count = len(lista)
    for parag in lista:
        if count > 1:
            txt += f'{parag}\n'
            count -= 1
        else:
            txt += f'{parag}'
    return txt


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
