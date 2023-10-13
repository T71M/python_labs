def frange(start, end, step):
    num = start
    while num <= end:
        yield num
        num += step
        num = round(num, 1)


def main():
    for x in frange(1, 3, 0.1):
        print(x)


if __name__ == "__main__":
    main()
