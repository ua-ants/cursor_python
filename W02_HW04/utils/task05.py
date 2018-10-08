# Task 5: Write function that return three values
#         1. Summary age of members.
#         2. The youngest member
#         3. The oldest member.


def return_summary(members: list) -> list:
    return (sum([x.get('age') for x in members]), min(members, key=lambda x: x.get('age')), max(members, key=lambda x: x.get('age')))

