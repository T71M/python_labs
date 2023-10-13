
from abc import *

class Library(object):
    book_id = 0;
    def __init__(self, adress, id):
        self.__adress = adress
        self.__id = id
        self._collection = []
        Library.book_id = 0;

    def __iadd__(self, book):
        book.id = len(self._collection) + 1
        self._collection.append(book)
        return self

    def __str__(self):
        return "" + self.__adress + " " + str(self.__id)

    def __iter__(self):
        for book in self._collection:
            yield book
