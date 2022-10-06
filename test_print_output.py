"""
    This program tests the function print_output
"""

import os
from numlines_in_file import print_output
from append_path import append_path
def test_print_output():

    """
    This program does pytest for the print_output program

    A predefined directory, sub directory and file structure needs
    to be created before this program is run

    The current directory needs to be changed to TestRoot before this program is run
    """

    directory = os.getcwd()

    given_input_raw = ['File01.txt', 'Dir01\\File0101.txt',
                       'Dir01\\File0102.txt', 'Dir01\\Dir0101\\File010101.txt']
    given_input = append_path(given_input_raw)
    expected_output1 = [ 5, 5, 5, 5, 4, 20]
    real_output1 = print_output (given_input,directory)
    print (real_output1)
    assert expected_output1 == real_output1

    given_input_raw = ['File01.docx', 'Dir01\\File0101.docx',
                       'Dir01\\File0102.docx', 'Dir01\\Dir0101\\File010101.docx']
    given_input = append_path(given_input_raw)
    expected_output1 = [-999]
    real_output1 = print_output(given_input, directory)
    assert expected_output1 == real_output1

    given_input_raw = ['File01.pdf', 'Dir01\\File0101.pdf',
                       'Dir01\\File0102.pdf', 'Dir01\\Dir0101\\File010101.pdf']
    given_input = append_path(given_input_raw)
    expected_output1 = [-999]
    real_output1 = print_output(given_input, directory)
    assert expected_output1 == real_output1

    given_input_raw = []
    given_input = append_path(given_input_raw)
    expected_output1 = [-999]
    real_output1 = print_output(given_input, directory)
    assert expected_output1 == real_output1
