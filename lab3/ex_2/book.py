
class ITaggable(object):
    def tag(self):
        ...


class Book(ITaggable):
    def __init__(self, author, name):
        if name == "":
            raise ValueError("поле имя должно быть заполнено!")
        self.__name = name
        self.__author = author
        self.__id = 0
        self.tag()

    def tag(self):
        self.__tag = [t for t in self.__name.split() if t[0].isupper()]

    def __str__(self):
        return "" + self.__name + ", " + self.__author

    
    def get_tag(self):
        return self.__tag

    def get_id(self):
        return self.__id
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
