def extra_enumerate(x):
    cum = 0
    for i, elem in enumerate(x):
        cum += x[i]
        frac = round(cum * 0.1, 1)
        yield i, elem, cum, frac


def main():
    list = [1, 3, 4, 2]
    for i, elem, cum, frac in extra_enumerate(list):
        print(i, cum, frac)


if __name__ == "__main__":
    main()
