

def checkWord(word):
    return word.upper() if word[0].isupper() else word


def main():
    wordList = input("string: ").split(" ")
    wordList = map(checkWord, wordList)
    print(" ".join(wordList))


if __name__ == "__main__":
    main()
