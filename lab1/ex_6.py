

def main():
    string = input("string: ")
    charList = [char for char in string if string.count(char) == 1]
    print(charList)


if __name__ == "__main__":
    main()
