# Task 6: Sort members by length of their names. If length of names is equal than sort by age.

def sort_members(members: list) -> list:
    return sorted(members, key = lambda x: (len(x.get('name')), x.get('age')))