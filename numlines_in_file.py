"""

This program accepts a directory name and extension as parameters and
print the list of files in the directory and sub directories with
matching extension

It also prints a summary with total number of files, total lines in the files
and average number of lines per file
"""

import os
import sys





def get_file_list(directory,extension):
    """


        :param directory: The directory given as input to start search
        :param extension : The extension which should be used to select files

        :return: list_files:Names  of matching files as a list. The list
                  would include files in sub directories

     """

    list_files = []
    for path, _subdirs, files in os.walk(directory):
        for file_name in files:
            file_name = os.path.join(path, file_name)
            file_details = os.path.splitext(file_name)
            file_extension = file_details[1]
            if file_extension == extension:
                list_files.append(file_name)
    return list_files

def get_file_num_lines(file_name):
    """
        :param file_name : Name of a file whose number of lines is to be found
        :return: ret_value : The number of lines in the file. Would be set to
                            -999 if the file is not a text file

         """
    line_count = 0
    not_txt_file = "N"
    try:
        with open(file_name, 'r', encoding="utf-8") as document:
            for  line_count, _line  in enumerate(document):
                pass
    except UnicodeDecodeError:
        not_txt_file = "Y"
    if not_txt_file == "Y":
        ret_value = -999
    else:
        ret_value = line_count + 1
    return ret_value

def print_output(file_list,directory):
    """
        :param file_list : List of files matching the seldection criterion given
        :param directory: The directory given as input to start search
        :return: ret_value : The numeric values in the print statements

            This Function is to print output.

            Output has 2 parts

            Part 1 - List of file name and number of lines for ecah file in the list

            Part 2 : Summary having total number of files, Total number of lines and
                     Average number of lines per file

         """

    total_files = 0
    total_lines = 0
    ret_list = []


    for file_name in file_list:
        num_lines = get_file_num_lines(file_name)
        if num_lines != -999:
            total_files = total_files +1
            total_lines = total_lines + num_lines
            ret_list.append(num_lines)
            file_name = format_file_name(file_name,directory)
            print(file_name, num_lines)
    if total_files == 0:
        print("\n \n Did not file any text files with given extension ")
        ret_list.append(-999)
    else:
        print("==============================================================================")
        print("Number of files found   :                ", total_files)
        print("Total number of lines   :                ", total_lines)
        print("Average lines per file  :                ", total_lines / total_files)
        ret_list.append(total_files)
        ret_list.append(total_lines)
    return ret_list

def format_file_name(file_name,directory):
    """

    :param file_name: The full path of the filw
    :param directory: The directory given as input to start search
    :return: file_name: The path starting from the directory where search started
    """
    file_prefix = "."
    back_slash = "\\"
    norm_slash = "/"
    print (file_name)
    file_name = file_prefix + file_name.replace(directory, "")
    file_name = file_name.replace(back_slash, norm_slash)
    print(file_name)
    return  file_name






ARG_NUM = len(sys.argv)
if ARG_NUM == 1:
    print ("Error : Name of directory to start search not given")
    sys.exit()
elif ARG_NUM == 2:
    EXTENSION = ".txt"
    DIRECTORY = os.path.abspath(sys.argv[1])
else:
    DIRECTORY = os.path.abspath(sys.argv[1])
    EXTENSION = sys.argv[2]

FILE_LIST =get_file_list(DIRECTORY,EXTENSION)
print_output(FILE_LIST,DIRECTORY)
