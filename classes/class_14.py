"""
Exceptional Handling
1)  Basic Exception Handling
2)  Try...Except...Else...Finally clause
3)  Self-Exception class
"""


# def list_vowels(string):
#     """
#     create list of vowels from string
#     :param string:
#     :return:
#     """
#     vowels = list()
#     for word in string.split(" "):
#         # try:
#         if is_vowel(word.lower()):
#             vowels.append(word)
#         # except Exception as error:
#         #     print(error)
#
#     print(vowels)

from traceback import print_exc
from json import dumps

x = {
    'test': b'"test"'
}

try:
    dumps(x)

except TypeError:
    print_exc()
except OSError:
    print_exc()
except ValueError:
    print_exc()

else:
    print("Test from inside")

finally:
    print("Exceptional handling completed")

print("Test from outside")



# list_vowels('wqwgagfdg213 dsfa 232')