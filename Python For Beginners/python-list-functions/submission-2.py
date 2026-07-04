from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    total_sum = 0
    for num in nums:
        total_sum += num
    return total_sum

def get_min(nums: List[int]) -> int:
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num
    #return min(nums)

def get_max(nums: List[int]) -> int:
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num
    #return max(nums)

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
