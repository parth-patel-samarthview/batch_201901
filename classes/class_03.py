"""

1) Data Structure: Dictionary, Tuple, Set


Assignment:

1) Create dictionary of user data
2) create list of user data dictionary with minimum of 10 user data
3) Create 5 dictionaries which have list values

"""

# [] = List
# {} = Dictionary
# () = Tuple


dictionary_variable = {
    'name': 'Parth',
    'address': 'home',
    'mobile_no': 9876553314
}
#
print(dictionary_variable)

print(dictionary_variable['name'])

print(dictionary_variable.get('mobile_no', "Key does not found."))
print(dictionary_variable.get('contact_no', "Key does not found."))

print(dictionary_variable.keys())
print(dictionary_variable.values())
print(dictionary_variable.items())

contact_no = dictionary_variable['mobile_no']

dictionary_variable.pop('mobile_no')
print(dictionary_variable)

dictionary_variable['contact_no'] = contact_no

print(dictionary_variable)

dict_01 = [
    {
        'test1': 'test2',
        'test3': 'test4'
    },
    {
        'test5': [
            {
                'test6': 'test7',
                'test8': 'test9'
            },
            {
                'test10': 'test11',
                'test12': 'test13'
            }
        ]
    }
]

# print(dict_01[1]['test5'][1]['test12'])

dict_02 = {
    'test1': 'test2',
    'test3': [
        {
            'test4': 'test5',
            'test6': [
                'test7',
                'test8'
            ]
        },
        [
            {'test9': 'test10'},
            'test11',
            {
                'test12': 'test13',
                'test14': 'print_me'
            }
        ],
        {'test15': 'print_me_2'}
    ]
}

# print(dict_02['test3'][1][2]['test14'])
# print(dict_02['test3'][2]['test15'])

tuple_variable = (1,)
# print(tuple_variable[0], tuple_variable[1])


x = [1, 1, 2, 3, 4, 2, 1, 3, 4, 2, 1, 3, 1, 3, 4, 1, 2, 3, 1]

print(set(x))
