
# 1. Create list with 10 elements using range method.  First element is 1.
#    Each next  equal previous plus 2

task_two_list = [1]
for i in range(9):
    task_two_list.append(task_two_list[i]+2)
print(task_two_list)

# 2. Append to previous list elements -  1, 5, 13, 20

add_to_list = [1, 5, 13, 20]
for i in range(add_to_list.__len__()):
    task_two_list.append(add_to_list[i])

print(task_two_list)

# 3. Create set from previous list.

task_four_set = set(task_two_list)

print(task_four_set)

# 4. Compare elements count in task_three_list and task_four_set
#    print "List is bigger" or "Set is bigger" based on which
#    element has more values

def compare_elements(a:list, b:set):
    """
    this function is created to compare provided list and set
    by nimber if elements
    :param a: list
    :param b: set
    :return: string with comparison results description
    """

    if a.__len__() > b.__len__():
        return "List is bigger"
    elif a.__len__() < b.__len__():
        return "Set is bigger"
    else:
        return "List and Set are equal"

print(compare_elements(task_two_list, task_four_set))