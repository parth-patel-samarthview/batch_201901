"""
Following are the topics we will cover today.

1) Recursive Function
2) Built-in Functions: min, max, count, len, split, zip, types, sum, sorted
"""


# #############################################################################
# 1) Recursive Function
# #############################################################################

def prime(limit):
    for no in range(1, limit + 1):
        flag = True
        for divider in range(2, no):
            if no % divider == 0:
                flag = False
                break
        if flag:
            print(F"{no} is Prime.")


def prime_generator(limit):
    number = 2

    while number < limit:
        flag = True
        for divider in range(2, number):
            if number % divider == 0:
                flag = False
                break

        if flag:
            yield number, flag
        number += 1


def prime_recursive(start, limit):
    if start == limit:
        return

    flag = True
    for divider in range(2, start):
        if start % divider == 0:
            flag = False
            break
    if flag:
        print(F'{start} is Prime.')

    prime_recursive(start + 1, limit)


def is_prime(number):
    """
    Check number is prime or not
    :param number: number
    :return: Boolean
    """
    #
    # _div = number - 1
    # check = 1
    # while _div > 1:
    #     if number % _div == 0:
    #         check = 0
    #         # break
    #     _div -= 1
    #
    # if check == 1:
    #     return True
    # else:
    #     return False

    # for i in range(2, number+1):
    #     for j in range(2, i):
    #         if i % j == 0:
    #             break
    #
    #     else:
    #         print(F"{i} Number is prime")

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


_list = [1, 3, 5, 24, 6, 7, 4, 2, 1, 3, 5, 7, 45]

print(min(_list))

print(max(_list))

print(_list.count(1))

print(len(_list))

print("This is what you want to split".split("to"))

fields = ['name', 'number']
values = ['Parth', '9869087667']
values2 = ['SS', '9789384773893']

for field, value, value2 in zip(fields, values, values2):
    print(field, value, value2)

__list = [1, "a", ['test'], {'test3': 'test4'}, True]

for i in __list:
    print(type(i), i)

print(sum(_list))

print(_list)
_list.sort()
print(_list)

_list = ['This is what', 'What is next', 'Nothing is limit', 'Why to stop',
         'Bas']

_list.sort()
print(_list)

mm, ss = divmod(600005, 60)
print(mm, ss)

hh, mm = divmod(mm, 60)
print(mm, ss)
dd, hh = divmod(hh, 24)
print(F"{dd}:{hh}:{mm}:{ss}")
