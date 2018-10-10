# Task 3: Each member will be exclude of group after reaching the age of 200 years.
#         Add field "load" for each member, which shows percentage of progress

def add_load(members: list) -> list:
    for d in members:
        d['load'] = d['age'] / 2
    return members