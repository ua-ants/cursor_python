# Task 2: For each member make his name uppercase

def names_to_uppercase(members: list) -> list:
    for d in members:
        d['name'] = d['name'].upper()
    return members

