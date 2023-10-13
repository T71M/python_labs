import random as r



def main():
    value = int(input("value: "))

    if value < 10:
        print(value)
        exit()

    thousands = 0
    hunreds = 0
    dozens = 0

    thousandBanknotes = r.randint(1, 5)
    hundredBanknotes = r.randint(1, 5)
    tenBanknotes = r.randint(1, 20)

    if value > 999:
        thousands = value // 1000
        value -= (thousands * 1000)
    if value > 99:
        hunreds = value // 100
        value -= (hunreds * 100)
    if value > 9:
        dozens = value // 10
        value -= (hunreds * 100)


    if thousands <= thousandBanknotes and hunreds <= hundredBanknotes and dozens <= tenBanknotes:
        thousandsString = str(thousands) + " * 1000 +" if thousands > 0 else ""
        hundredString = str(hunreds) + " * 100 +" if hunreds > 0 else ""
        dozensString = str(dozens) + " * 10" if dozens > 0 else ""
        print(f'{thousandsString}{hundredString}{dozensString}')
    else:
        print("операция не может быть выполнена")

if __name__ == "__main__":
    main()

