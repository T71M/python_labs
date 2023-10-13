
import argparse
import os
from datetime import datetime


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', required=True)
    parser.add_argument('--days', required=True, type=int)
    parser.add_argument('--size', required=True, type=int)

    return parser


if __name__ == "__main__":
    date = datetime
    now = datetime.now()
    parser = createParser()
    namespace = parser.parse_args()
    files = os.listdir("./ex_6/")
    print(files)

    for file in files:
        if os.path.isfile("./ex_6/" + file) and not file == ".DS_Store":
            birth_time = date.fromtimestamp(
                os.stat("./ex_6/" + files[0]).st_birthtime)
            difference = birth_time - now
            if difference.days >= namespace.days:
                if os.path.exists("./ex_6/archive"):
                    os.replace("./ex_6/" + file, "./ex_6/archive/" + file)
                    continue
                else:
                    os.mkdir("./ex_6/archive")
                    os.replace("./ex_6/" + file, "./ex_6/archive/" + file)
                    continue

            if os.stat("./ex_6/" + file).st_size < namespace.size:
                if os.path.exists("./ex_6/small"):
                    os.replace("./ex_6/" + file, "./ex_6/small/" + file)
                    continue
                else:
                    os.mkdir("./ex_6/small")
                    os.replace("./ex_6/" + file, "./ex_6/small/" + file)
                    continue
