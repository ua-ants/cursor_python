from utils.task02 import names_to_uppercase
from utils.task03 import add_load
from utils.task03 import delete_200
from utils.task04 import exclude_o_members
from utils.task05 import return_summary
from utils.task06 import sort_members


members = [
    {'age': 43, 'name': 'Denis'},
    {'age': 49, 'name': 'Roman'},
    {'age': 36, 'name': 'Godzilla'},
    {'age': 47, 'name': 'Spike'},
    {'age': 31, 'name': 'SuperMan'},
    {'age': 49, 'name': 'Batman'},
    {'age': 37, 'name': 'Claus'},
    {'age': 55, 'name': 'Frank'},
    {'age': 83, 'name': 'Homer'},
    {'age': 200, 'name': 'Test1'},
    {'age': 210, 'name': 'Test2'}
]


#2
names_to_uppercase(members)
#3
add_load(members)
print(members)
delete_200(members)
print(members)
#4
members = exclude_o_members(members)
print(members)
#5
print(return_summary(members))
#6
print(sort_members(members))
