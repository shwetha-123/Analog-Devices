# Analog Devices
Python line count exercise


##Aim

The program takes a directory and extension as arguments. The program would search all files with the given extension in the given directory and all its subdirectories. A list of all matching files with the number of lines within the file would be printed. It also prints a summary having number of files, number of lines across files and the average number of lines per file.

##List of programs :

1.    num_lines_in_file.py         --->  The main progran which containes all functions required 
2.    test_get_file_list.py       --->  ptest for get_file_list function
3.    test_get_file_num_lines.py  --->  pyest for get_file_num_lines function
4.    test_print_output.py        --->  pytest for print_output function
5.    test_format_file_name.py    --->  pytest fot format_file_name function
6.    TestRoot.zip                --->  zip file to be used to create the directories, sub directories and files required for unit testing


##Instructions

1)	Ensure that Pytest is installed . 
2)	Ensure that the path is set to include directory containing python and pytest executables used
3)  To run the program, the following steps should be followed
     - Go to terminal of the IDE
     - Execute the command "python num_lines_in_file.py" with appropriate paramaters
4)  To run unit test cases, the following steps should be followed
     - Create directory structure starting with TestRoot by unzippig the TestRoot.zip file
     - Change current directory to the newly created TestRoot directory
     - Go tothe terminal of the IDSE and execute the command "pytest <file_name> . Eg. pytest test_get_file_list.py
    
