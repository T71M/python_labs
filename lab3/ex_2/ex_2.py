from book import Book
from lib import Library


def main():
    lib = Library("51 Some str., NY", 1)
    lib += Book("Leo Tolstoi", "War and Peace")
    lib += Book("Charles Dickens", "David Copperfield")

    book = Book("Charles Dickens", "David Copperfield")

    for book in lib:
        print(f'[{book.id}] {book}')
        print(book.get_tag())


if __name__ == '__main__':
    main()
