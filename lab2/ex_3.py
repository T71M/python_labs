import os


def main():
    files = os.listdir("ex_3")
    with open("./ex_3 src/ex_3.txt") as file:
        for i, line in enumerate(file):
            os.rename("ex_3/" + files[i] + ".mp3", line)


if __name__ == '__main__':
    main()
