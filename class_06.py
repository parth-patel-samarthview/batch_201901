"""
1) Class
2) OOPs concept
3) Abstraction
4) Encapsulation
5) Inheritance
6) Polymorphism
"""


# #############################################################################
# 1) Class
# #############################################################################


class ClassName(object):
    """
    Class level doc string
    """

    def __init__(self, name):
        self.name = name

    def my_function(self):
        """

        :return:
        """
        print(F"Hello my function {self.name}")

    def my_function_2(self):
        print(F"Hello {self.name}")


print('=========================')
_class = ClassName(name="Parth")
_class.my_function()
_class.name = "Vote for BJP"
_class.my_function_2()
_class.my_function()

print('=========================')

_class2 = ClassName(name="PPP").my_function()

print('=========================')
_class3 = ClassName(name="BJP").my_function_2()
