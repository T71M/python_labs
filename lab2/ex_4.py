import re


def main():
    file = open("ex_4.txt")
    pattern = '[0-9]{2}-[0-9]{2}-[0-9]{4}'

    for i, line in enumerate(file):
        match = re.search(pattern, line)
        print(
            f'строка:{i + 1}, позиция {match.span()[0]} : найдено "{match.group()}" ')
    file.close()


if __name__ == '__main__':
    main()
