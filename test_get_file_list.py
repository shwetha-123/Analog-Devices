"""
    File containing function to do pytest on get_file_list function
"""

import os
from append_path import append_path
from numlines_in_file import get_file_list
def test_get_file_list():
    """

    This function is for carrying out pytest on
    get_file_list function

    This  is a pre-defined directory , sub directory and file
    structure starting at TestRoot to be created

    The current directory has to be made TestRoot to run pytest
    """

    working_directory = os.getcwd()
    expected_output_raw = ['File01.txt', 'Dir01\\File0101.txt', 'Dir01\\File0102.txt',
                           'Dir01\\Dir0101\\File010101.txt']
    expected_output1 = append_path(expected_output_raw)
    real_output1 = get_file_list(working_directory, ".txt")
    assert expected_output1 == real_output1

    expected_output_raw = ['File01.docx', 'File02.docx', 'Dir01\\File0101.docx',
                           'Dir01\\File0102.docx', 'Dir01\\Dir0101\\File010101.docx']

    expected_output1 = append_path(expected_output_raw)
    real_output1 = get_file_list(working_directory, ".docx")
    assert expected_output1 == real_output1


    expected_output1 = []
    real_output1 = get_file_list(working_directory+"/DoesNotExist", ".pdf")
    assert expected_output1 == real_output1
