from typing import List

def contains_duplicate(words: List[str]) -> bool:
    my_set = set()
    # length_list = len(words)
    # for word in words:
    #     my_set.add(word)
    # length_set = len(my_set)
    # if length_list > length_set:
    #     return True
    # return False
    for word in words:
        if word in my_set:
            return True
        my_set.add(word)
    return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
