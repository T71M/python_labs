
def main():
    wordList = input("string: ").split(" ")

    print(list(filter(lambda x: len(x) > 7, wordList)))
    print(list(filter(lambda x:  4 <= len(x) <= 7, wordList)))
    print(list(filter(lambda x:   len(x) < 4, wordList)))


if __name__ == "__main__":
    main()
