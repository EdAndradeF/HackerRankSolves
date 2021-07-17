def stringvalidator(string, func):
    count = len(string)
    for char in string:
        if eval(f'char.{func}'):
            return True
    return False


if __name__ == '__main__':
    s = input()
    isits = ['isalnum()', 'isalpha()', 'isdigit()', 'islower()', 'isupper()']
    for test in isits:
        print(stringvalidator(s, test))
