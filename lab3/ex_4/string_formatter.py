import re


class StringFormatter(object):
    def __init__(self,):
        self.__str = ""

    @staticmethod
    def delete_words(str, n):
        list_str = [s for s in str.split() if len(s) >= n]
        return " ".join(list_str)

    @staticmethod
    def swap_digits(str):
        return re.sub('/d', "*", str)

    @staticmethod
    def split_for_every_symbol(str):
        return " ".join([s for s in str if s != " "])

    @staticmethod
    def sort_for_word_len(str):
        str = str.split(" ")
        return " ".join(sorted(str, key=len))

    @staticmethod
    def sort_for_lexicographic(str):
        str = str.split()
        return " ".join(sorted(str))
