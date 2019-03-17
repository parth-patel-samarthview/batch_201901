"""
Following are the topics we will cover today.

1)  Know how – Python Absolute Path + write file
2)  File Parsing with “With”
3)  File Parsing with Generator


"""

from os import path, makedirs

# #############################################################################
# 1) Python Absolute Path
# #############################################################################


# Current absolute path

# file_path = r"c:\repos\Library"
current_file_path = path.abspath(__file__)
print(current_file_path)

# Get current directory
current_directory = path.dirname(path.abspath(__file__))

# Concat file paths

json_file_path = path.join(
    current_directory, 'test_demo', 'json_file', 'parse_json_data.json'
)
#
# if path.exists(json_file_path):
#     print("hello JSON")

xml_file_path = path.join(
    current_directory, 'test_demo', 'xml_file', 'parse_xml_data.xml'
)

# if path.exists(xml_file_path):
#     print("hello XML")

text_file_path = path.join(
    current_directory, 'test_demo', 'text_file', 'parse_text.txt'
)

csv_file_path = path.join(
    current_directory, 'test_demo', 'csv_file', 'parse_csv.csv'
)


# if not path.exists(path.dirname(text_file_path)):
#     makedirs(path.dirname(text_file_path))

file_data = """
This is my file, which have text format in addition this is created at demo.
This file has nothing to do with my session, still i want to create this file.
Since I decided to create file, no one can stop me to create this file. 
I am not alone when I created this file.
"""

# file_obj = open(text_file_path, 'w+')
# file_obj.writelines(file_data)
# file_obj.close()

# with open(text_file_path, 'w+') as text_file:
#     text_file.writelines(file_data)

# with open(text_file_path, 'r+') as text_file_read:
#     data = text_file_read.readlines()
#     print(data)

#
# with open(text_file_path, 'r+') as text_file_read:
#     for line in text_file_read:
#         print(line.replace("\n", ""))


def generator_parse_file(file_path):
    with open(file_path, 'r+') as text_file:
        for line in text_file:
            yield line.replace("\n", "")


for i in generator_parse_file(text_file_path):
    print(i)
