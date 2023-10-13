

def main():
    password = input("Введите пароль (не меньше 8 символов): ")
    if len(password) < 8:
        print("пароль должен быть не меньше 8 символов!")
        exit()

    numbers = "1234567890"
    specSymbols = "_-()*:&.,<>?!@#$%^~"

    haveSpecSymbol = False
    haveNumber = False
    haveUpperLetter = False


    if [number for number in numbers if number in password]:
        haveNumber = True
    if [symbol for symbol in specSymbols if symbol in password]:
        haveSpecSymbol = True

    for symbol in password:
        if symbol.isupper():
            haveUpperLetter = True

    reliabilityList = ["Слабый", "Средний", "Сильный"]
    passwordReliability = haveNumber + haveSpecSymbol + haveUpperLetter
    passwordReliability -= 1 if passwordReliability > 0 else passwordReliability
    passwordHave = "т.к "

    passwordHave += " Есть хотя бы 1 цифра," if haveNumber else " Пароль не содержит цифр,"
    passwordHave += " Есть одна заглавная буква," if haveUpperLetter else " Пароль не содержит заглавных букв,"
    passwordHave += " Есть хотя бы 1 специальный символ," if haveSpecSymbol else " Пароль не содержит специальных символов,"

    print(f'Пароль - {reliabilityList[passwordReliability]}, {passwordHave[:-1]} ')

if __name__ == "__main__":
    main()

