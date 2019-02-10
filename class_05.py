"""
Following topics will be covered today

1) Comprehension
2) User Defined Function

# Assignment

1) Write list comprehension to create 15 random numbers
2) Write list comprehension to create Prime Numbers till user defined number
3) Write Dictionary comprehension with 5 key value pair
4) Convert all pattern assignments in User Defined Function

"""

# #############################################################################
# Comprehension
# #############################################################################

# ## List Comprehension

# _odd = list()
#
# for i in range(1, 10, 2):
#     _odd.append(i)
# print(_odd)
#
# __odd = [i for i in range(1, 10, 2)]
# print(__odd)
#
# __odd = []
# for i in range(1, 10):
#     if i % 2 == 1:
#         __odd.append(i)
#
# __odd = [i for i in range(1, 10) if i % 2 == 1]
# print(__odd)


# ## Directory Comprehension

# sq = {}
#
# numbers = [2, 4, 6, 7, 8, 9, 11]
#
# for num in numbers:
#     sq[num] = num * num
#
# print(sq)
#
# _sq = {num: num*num for num in numbers}
#
# print(_sq)

# labels = ['Name', 'Age', 'Contact No']
#
# user_1 = ['Parth', 10, 9876446654]
# user_2 = ['Srikant', 12, 986343872]
# user_3 = ['Kiran', 12, 909434455]

# op = [
#     {"Name": "Parth", "Age": 10, "Contact No": 9876446654},
#     {"Name": "Srikant", "Age": 12, "Contact No": 986343872},
#     {"Name": "Parth", "Age": 12, "Contact No": 909434455}
# ]

# op = list()
# for user in [user_1, user_2, user_3]:
#     _user = dict()
#     for index in range(0, 3):
#         _user[labels[index]] = user[index]
#     op.append(_user)
#
# print(op)
#
# output = [
#     {
#         label: user[index] for index, label in enumerate(labels)
#     } for user in [user_1, user_2, user_3]
# ]

# print(output)

# #############################################################################
# User Defined Function
# #############################################################################

'''
# simple function 
def <function_name>():
    """
    Function doc string 
    """
    <statement 1>
    <statement 2>
    .
    .
    .
    <statement n>
<statement a> 


'''


def greetings():
    """
    This is greetings function
    """
    print("Hello World")


# greetings()


def arg_greetings(name):
    """
    This is greetings function with argument
    :param name: User name
    """
    print(F"Hello {name}")


# arg_greetings(name="Parth")


def arg_return_greetings(name=""):
    """
    This is greetings function with arguments and return greeting message
    :param name:
    :return:
    """
    message = F"Hello {name}"
    return message


# _name = input("Enter name :")
# resp = arg_return_greetings(name=_name)
# print(resp)


def wild_card_args_function(*args):
    """

    :param args: List wild card argument
    :return:
    """
    print(args[0], args[1])


# wild_card_args_function(*['test', 'test2'])


def wild_card_kwargs_function(**kwargs):
    """

    :param kwargs: Dictionary wild card argument
    :return:
    """

    for key, values in kwargs.items():
        print(key, ": ", values)


user_1 = {"Name": "Parth", "Age": 10, "Contact No": 9876446654}
wild_card_kwargs_function(**user_1)
