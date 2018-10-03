# We have dict {"Name": "", "Age": , "Hobby": ""}.
#
# Create method that will fill it with data.

def create_dict(name:str, age:int, hobby:str):
    """
    function place passed parameters into the dictionary structure
    :param name:
    :param age:
    :param hobby:
    :return: dictionary
    """
    resuslt_dict = {}
    resuslt_dict["Name"] = name
    resuslt_dict["Age"] = age
    resuslt_dict["Hobby"] = hobby

    return resuslt_dict

print(create_dict("Andrii", 34, "Books"))