def add_two_numbers() -> int:
    input_data = input()
    extracted_values = input_data.split(",")

    mylist = []
    total_sum = 0
    for value in extracted_values:
        mylist.append(int(value))
        total_sum+=int(value)

    return total_sum

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
