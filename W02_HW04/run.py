from my_utils.task02 import names_to_uppercase
from my_utils.task03 import add_load
from my_utils.task04 import exclude_o_members
from my_utils.task05 import return_summary
from my_utils.task06 import sort_members


members = [
    {'age': 43, 'name': 'Denis'},
    {'age': 49, 'name': 'Roman'},
    {'age': 36, 'name': 'Godzilla'},
    {'age': 47, 'name': 'Spike'},
    {'age': 31, 'name': 'SuperMan'},
    {'age': 49, 'name': 'Batman'},
    {'age': 37, 'name': 'Claus'},
    {'age': 55, 'name': 'Frank'},
    {'age': 83, 'name': 'Homer'}
]


#2
names_to_uppercase(members)
#3
add_load(members)
print(members)
#4
members = exclude_o_members(members)
print(members)
#5
print(return_summary(members))
#6
print(sort_members(members))