# Create method that returned value from list based on index.
#
# If list does not contain such index, than return None value
#
# Note:
#
# Use try except to resolve this issue.

def get_value_from_list(data:list, index:int):
    """
    function returns list element by index
    :param data: list of elements
    :param index: required index
    :return: element by index
    """
    try:
        return data[index]
    except IndexError:
        return None
