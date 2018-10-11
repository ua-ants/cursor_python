# Task 1: Usage of os module. Create a tree of directories (any depth, any names).
#         Create files in some of directories (how many. and where - up to you).
#         Using recursive function and os module, pretty print the tree with directory
#         and file names.

import os
from shutil import rmtree
import pprint as pp

working_path = os.getcwd() + "/resources"

def create_dirs_files(working_path: str, dirs_number: int, files_number_in_dir: int):
    '''
    function to create fake tree with files for testing
    :param working_path: directory where to create
    :param dirs_number: number of trees to be created
    :param files_number_in_dir: number of files created in directory
    :return: None
    '''
    for i in range(dirs_number):
        current_dir = working_path + "/test" + str(i)
        os.makedirs(current_dir)
        os.chdir(current_dir)
        for f in range(files_number_in_dir):
            with open("file" + str(f) + ".txt", 'w') as file:
                file.write("This is file #" + str(f) + " in directory: " + current_dir)
        os.chdir(working_path)

def delete_dirs(working_path: str):
    '''
    function to delete recursively all directory and files starting from
    working directory provided as a parameter
    :param working_path:
    :return: None
    '''
    if 'resources' in os.listdir():
        print('deleting')
        rmtree(working_path)

def print_tree(working_path: str) -> dict:
    '''
    function to collect file tree into dictionary hierarchically
    :param working_path: top directory where to start
    :return: dictionary structured accordingly
    '''
    res_dict = {}
    if os.path.isdir(working_path):
        res_dict[os.path.basename(working_path)] = []
        for file in os.listdir(working_path):
            if os.path.isdir(working_path + "/" + file):
                res_dict[os.path.basename(working_path)].append(print_tree(working_path + "/" + file))
            else:
                res_dict[os.path.basename(working_path)].append(file)
    return res_dict


##delete files if exists before creation
delete_dirs(working_path)
##create tree
create_dirs_files(working_path, 3, 5)
##pretty print files tree dictionary
pp.pprint(print_tree(working_path))
