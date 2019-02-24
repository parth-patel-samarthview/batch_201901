"""
Following are the topics we will cover today.

1) Anonymous Lambda Function
2) Iterator
3) Generator
4) Generator vs Iterator
5) Recursive Function
"""

# #############################################################################
# 1) Anonymous Lambda Function
# #############################################################################

"""
Lambda 

lambda object : operation/expression 
map(lambda iter_item : operation/expression, iterable object) 
"""


# _add_func = lambda ele_1, ele_2, ele_3: (ele_1 + ele_2) * ele_3
#
# print(_add_func(34, 45, 1))


# _sq = list(map(lambda x: x * x, [1, 2, 3, 4, 5]))
# print(_sq)

# #############################################################################
# 2) Iterator
# #############################################################################


# class MyRange:
#     """
#     my range function
#     """
#
#     def __init__(self, i, n, s):
#         self.i = i
#         self.n = n
#         self.s = s
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         if self.i < self.n:
#             i = self.i
#             self.i += self.s
#             return i
#         else:
#             raise StopIteration()
#
#
# data = MyRange(0, 3, 1)
#
# print(data.next())
# print(data.next())
# print(data.next())
# print(data.next())


# #############################################################################
# 3) Generator
# #############################################################################

#
# def simple_generator():
#     yield 1
#     yield 2
#     yield 3
#
#
# for item in simple_generator():
#     print(item)


def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b
        # print("----", a, b)


def _fib(limit):
    numbers = []
    a = 0
    b = 1

    while True:
        if a > limit:
            break
        a, b = b, a + b
        # print('++++', a, b)
        numbers.append(a)

    return numbers


def factorial(limit):
    output = 1
    initial = 1
    while initial <= limit:
        yield initial * output
        output, initial = initial*output, initial+1


for i in factorial(5):
    print(i)

from datetime import datetime

#
# start = datetime.now()
# _fib(10000000)
# end = datetime.now()
# print('regular func: ', end - start)
#
#
# start = datetime.now()
# numbers = list()
# for i in fib(100):
#     numbers.append(i)
# end = datetime.now()
# print('generator :   ', end - start)

# start = datetime.now()
# numbers = [i for i in fib(10000000)]
# end = datetime.now()
# print('list comp:    ', end - start)




