



def main():
    number = float(input("введите число:"))
    if number < 0:
        raise Exception("сумма должна быть больше 0")

    rub = int(number)
    cop = round((number - int(number)) * 100)

    print(f'{rub} руб. {cop} коп.')

if __name__ == "__main__":
    main()



