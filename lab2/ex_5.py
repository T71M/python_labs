import re


def main():
    str = input("введите строку:")
    pattern = '[A-Z][a-z]+[0-9]{2,4}'
    print(re.findall(pattern, str))


if __name__ == '__main__':
    main()
