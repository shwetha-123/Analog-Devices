"""
This file has the program to carry out pytest for format_file_name function

"""
from numlines_in_file import format_file_name

def test_format_file_name():

    """
    This program carries out pytest for the format_file_name function

    """

    input_file_name = "C:\\Users\\Downloads\\Dir01\\Dir0101\\File010101.txt"
    expected_output = "./Dir01/Dir0101/File010101.txt"
    directory = "C:\\Users\\Downloads"


    real_output = format_file_name(input_file_name, directory)
    assert real_output == expected_output
