
def checkIsListInc(list):
    count = 0

    for item in list[:-1]:
        if item > list[count + 1]:
            return False
        count += 1
    return True


def main():

    listDec = [7, 6, 5, 4, 3, 2, 1]
    listInc = [1, 2, 3, 4, 5, 6, 7]

    print(f'first list - {checkIsListInc(listInc)}')
    print(f'second list - {checkIsListInc(listDec)}')


if __name__ == "__main__":
    main()
