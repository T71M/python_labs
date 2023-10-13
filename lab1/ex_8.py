import random as r


def main():

    n = r.randint(1, 10000)
    list = [r.randint(1, 100) for _ in range(n)]

    print(len(list))

    while not len(list) & (len(list) - 1) == 0:
        list.append(0)

    print(len(list))

if __name__ == "__main__":
    main()
