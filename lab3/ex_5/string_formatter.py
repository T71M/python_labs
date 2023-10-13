import re


class StringFormatter(object):
    def __init__(self,):
        self.__str = ""

    def delete_words(self, str, n):
        list_str = [s for s in str.split() if len(s) >= n]
        return " ".join(list_str)

    def swap_digits(self, str):
        patter = re.compile('[0-9]')
        return patter.sub("*", str)

    def split_for_every_symbol(self, str):
        return " ".join([s for s in str if s != " "])

    def sort_for_word_len(self, str):
        str = str.split(" ")
        return " ".join(sorted(str, key=len))

    def sort_for_lexicographic(self, str):
        str = str.split()
        return " ".join(sorted(str))
