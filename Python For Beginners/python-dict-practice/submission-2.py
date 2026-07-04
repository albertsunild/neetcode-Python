from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    word_dic = {}
    for char in word:
        if char in word_dic:
            word_dic[char] += 1
        else:
            word_dic[char] = 1
    return word_dic

# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
