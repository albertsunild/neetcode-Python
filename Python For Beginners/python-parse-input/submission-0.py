from typing import List

def read_integers() -> List[int]:
    number_string = input()
    string_list = number_string.split(",")

    mylist = []
    for string in string_list:
        mylist.append(int(string))
    return mylist


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
