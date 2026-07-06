from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    index_of_seven = -1
    for i, num in enumerate(nums):
        if num == 7:
            index_of_seven = i
            break
    return index_of_seven

def get_dist_between_sevens(nums: List[int]) -> int:
    listofIndex = []
    for i, num in enumerate(nums):
        if num == 7:
            listofIndex.append(i)
    start_index = listofIndex[0]
    # end_index = listofIndex[1] -- this would work for first and last occurance
    end_index = listofIndex[1]
    # print(start_index,end_index)
    distance = end_index - start_index
    return distance

# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
