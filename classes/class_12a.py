"""
1) Decorator
2) Project Discussion

Assignments :
1) Create 10 decorators

2) write a decorator function and 3-4 functions to check user have that
   permission or not.

   Create list of permissions (at least 15 permissions)
   permissions = ['can_create_user', 'can_delete_user', ....]
   Create dictionary of user  (at least 4 users)
   users = {
        '<email_id/phone_no/user_id>' : {
            'roles': [role_id1],
            'permissions': ['can_read_user']
        }
   }
   Create dictionary of roles (at least 5 roles)
   roles = {
        'id': 1,
        'permissions': ['can_create_user', 'can_delete_user']
   }

   Functions
   def create_user(user_id, 'can_create_user')
   def delete_user(user_id, 'can_delete_user')
   .
   .
   .
"""


# #############################################################################
# 1) Decorator
# #############################################################################

# Closer Function
# Nested Function

def greetings():
    return my_name


def my_name(name):
    return "Hello {}".format(name)


def add_p_tag(string):
    return "<p>{}</p>".format(string)


def add_span_tag(string):
    return "<span>{}</span>".format(string)


def base_func(_name):
    def derived_1_func(func):
        return func(_name)

    return derived_1_func(add_p_tag)


# print(base_func("Parth"))
#
#
# p = greetings()
#
# print(p("Parth"))


# def decorator_function(name):
#     print("hello from decorators")
#
#     def greetings():
#         return F"hello {name} from greetings"
#
#     return greetings
#
#
# def display(name):
#     print(name)


# display = decorator_function(display)
# display()
#
#
def make_p(func):
    def wrapper(name):
        func(F"<p>{name}</p>")

    return wrapper

def make_span(func):
    def wrapper(name):
        func(F"<span>{name}</span>")

    return wrapper

@make_span
@make_p
def my_name_display(name):
    print("my name is {}".format(name))


@make_p
def your_name_display(name):
    print("your name is {}".format(name))


# pp = make_p(my_name_display)
# pp("Parth")

my_name_display("Parth")
your_name_display("parth")

def p_tag_decorator(_function):
    def wrapper(name):
        print('We are in Wrapper function')
        _format = F"<p>{name}</p>"
        _function(_format)

    return wrapper


def b_tag_decorator(_function):
    def wrapper(name):
        print('We are in b Wrapper function')
        _format = F"<b>{name}</b>"
        _function(_format)

    return wrapper
#
#

# @b_tag_decorator
# @p_tag_decorator
# def display_2(string_data):
#
#     print(string_data)


# display_2("Parth")


# # display_2("Hi Parth, what happening with your life..")
#
#
#
# def u_tag_decorator(display_function):
#
#     def wrapper_function(name):
#         print('This is wrapper function of u tag decorator')
#         updated_string = F"<u>{name}</u>"
#         display_function(updated_string)
#
#     return wrapper_function
# #
# # test = u_tag_decorator(display)
# #
# # test("parth")
#
# @u_tag_decorator
# def display(name):
#     print(name)
#
# display('This is my 1st decorator')


"""
# Project definition
based on template generate pdf (stand alone)
unit converter (stand alone)
Invoice generator from commandline (stand alone)
BMI calculator and suggestion (stand alone)
Income Tax calculator (stand alone)
Weather forecast (stand alone)
Exam delivery (web project)

"""
