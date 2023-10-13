from re import X


def non_empty(func):
    def decorate_list():
        return [elem for elem in func() if elem != '' and elem != "None"]
    return decorate_list


@non_empty
def get_pages():
    return ['chapter1', '', 'contents', 'None', 'line1']


def main():
    print(get_pages())


if __name__ == "__main__":
    main()
