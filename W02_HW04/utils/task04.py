# Task 4: Left only those members who have letter 'o' in names.

def exclude_o_members(members: list) -> list:
    return list(filter(lambda d: 'O' in d['name'], members))
