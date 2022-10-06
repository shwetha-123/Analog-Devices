"""

File having function to do pytest on get_file_num_lines function
"""

import os
from numlines_in_file import get_file_num_lines
def test_get_file_num_lines():

    """
    This program carries out pytest on get_file_num_lines function

     A predefined directory, sub directory and file structure starting with
     TestRoot needs to be created before this program is run

     This program has to be run after changing the current directory to
     TestRoot



    """

    working_directory = os.getcwd()
    file_name1 = working_directory + ".\\File01.txt"
    expected_output1 = 5
    real_output1 = get_file_num_lines(file_name1)
    assert expected_output1 == real_output1

    file_name1 = working_directory + ".\\File01.docx"
    expected_output1 = -999
    real_output1 = get_file_num_lines(file_name1)
    print (real_output1)
    assert expected_output1 == real_output1

    file_name1 = working_directory + ".\\File01.pdf"
    expected_output1 = -999
    real_output1 = get_file_num_lines(file_name1)
    assert expected_output1 == real_output1
