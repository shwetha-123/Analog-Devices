"""
This file has the append path function. This is developed to ensure that
pytest can be carried out on any computer .

pytest is done from a specified directory with "." as the paramter pased

This program gets the full path
"""

import os
def append_path(file_list):
    """


    :param file_list: List of files for which full path needs to be returned
    :return ret_list: contains the list of files with full path

    """
    directory = "."
    dir_path = os.path.abspath(directory)
    ret_list = []
    for file_name in file_list:
        file_name = dir_path + "\\" + file_name
        ret_list.append (file_name)
    return ret_list