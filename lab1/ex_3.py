

def main():
    cardNumber = input("input card number: ")

    secureCardNumber = ""

    if len(cardNumber) < 16 and len(cardNumber) > 16:
        raise Exception("invalid card number")

    secureCardNumber += cardNumber[0:4] + ("*" * 8) + cardNumber[-4:]

    print(secureCardNumber)


if __name__ == "__main__":
    main()
