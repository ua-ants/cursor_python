# Task 2: For each member make his name uppercase

def names_to_uppercase(members: list) -> list:
    for d in members:
        d.update((k, v.upper()) for k, v in d.items() if k == 'name')
    return members


