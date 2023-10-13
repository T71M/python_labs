import hashlib
import os


def main():
    files_dict = {}
    files = os.listdir("ex_2")

    for file in files:
        temp_file = open("./ex_2/" + file)
        hash = hashlib.md5(temp_file.read().encode("utf-8")).hexdigest()
        if hash in files_dict:
            files_dict[hash].append(file)
        else:
            files_dict[hash] = [file]
        temp_file.close()

    print(files_dict)


if __name__ == '__main__':
    main()
