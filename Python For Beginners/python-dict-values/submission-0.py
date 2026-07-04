from typing import Dict, List

# key things to remember in Dictionary
#create dictionary -- dict = {}


def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    values_in_dict = list(age_dict.values())

    values = []
    for key in age_dict:
        value = age_dict[key]
        values.append(value)
    return values

# do not modify below this line
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))
