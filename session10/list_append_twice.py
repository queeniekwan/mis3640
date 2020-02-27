def append_twice(a_list, val):
    """Mutates arguments."""
    a_list.append(val)
    a_list.append(val)


# nums = [1, 2, 3]
# nums_2 = nums
# append_twice(nums, 4)
# print(nums)
# print(nums_2)


def append_twice_bad(a_list, val):
    """Useless!"""
    a_list = a_list + [val, val]


# nums = [1, 2, 3]
# append_twice_bad(nums, 4)
# print(nums)


def append_twice_good(a_list, val):
    """Returns a new list"""
    a_list = a_list + [val, val]
    return a_list


# nums = [1, 2, 3]
# new_nums = append_twice_good(nums, 4)
# print(new_nums)
