"""
This is class 02 file
1) Variable
2) Data Type: Integer, Float, String, Boolean, None
3) Data Structure: List

Assignment:
1) Create 5 variables for each data types
2) Create 5 list variables with 3 elements like Name, address, contact_no

"""

# #############################################################################
# 2) Data type
# #############################################################################


# ### Integer
integer_variable = 3

# print('Integer')
# print(integer_variable, type(integer_variable), id(integer_variable))

float_variable = 3.4

# ### String
string_variable = "This is my single line string."
string_variable_2 = "This is my " \
                    "multi line string 01. "

string_variable_3 = """
This is my multi line string 02. 
I can write anything in this block.
No one have any problem with that, isn't it?
"""
# print('String')
# print(string_variable, type(string_variable), id(string_variable))

# print('String_2')
# print(string_variable_2, type(string_variable_2), id(string_variable_2))

# print('String_3')
# print(string_variable_3, type(string_variable_3), id(string_variable_3))


# ### Boolean
true_flag = True
false_flag = False

# print(true_flag, type(true_flag), id(true_flag))
# print(false_flag, type(false_flag), id(false_flag))

# ### None

none_variable = None
# print(none_variable, type(none_variable), id(none_variable))

# #############################################################################
# 2) Data Structure
# #############################################################################

# ### List

list_variable = [
    'Parth', 'Home', 98765430386, 346.533, False, 'Parth'
]

# print(list_variable)
# print(
#     type(list_variable[0]), type(list_variable[1]), type(list_variable[2]),
#     type(list_variable[3]), type(list_variable[4])
# )

# print(list_variable.index('Parth'))

# print(len(list_variable))

# print(list_variable.count('Parth'))

integer_list = [3, 5, 2, 6, 2, 6, 7, 92, 3, 22, 90]

# print(sorted(integer_list))
integer_list.sort(reverse=True)
# print(integer_list)

list_nested = [
    "Parth", ["SamarthTech", "Certview", [202000, 1039200]]
]
print(list_nested[1][2][0])

list_nested_02 = [
    ['test_1', ['test_2', 'test_3', ['test_4']], 'test_5',
     ['test_6', 'test_7'], 'test_8', ['test_9', ['test_10']]]
]

print(list_nested_02[0][4])
print(list_nested_02[0][5][1][0])
