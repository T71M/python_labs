
def main():
    file = open("ex_1.txt")

    text = file.read()
    file.close()
    ban_symbols = "()""/ \ '':;><.,!#$%^&* "
    dic = {x.lower(): 0 for _, x in enumerate(text) if x not in ban_symbols}

    for index, sym in enumerate(text):
        if sym in dic:
            dic[sym] += 1
    sorted = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))

    print(sorted)


if __name__ == '__main__':
    main()
