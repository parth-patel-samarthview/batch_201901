"""
Following Topics will be covered today..

1)  Conditional Statement
2)  Break and Continue
3)  Looping Structure
4)  Nested loop
5)  Control looping

Assignments:
1) write a code to find maximum number from 5 values
2) write a code to find minimum number from 5 values
3) write a code to find maximum number from 10 values with only single if statement
4) write a code to find minimum number from 10 values with only single if statement


Create pattern using for or while loop
1)                  2)              3)                  4)
* * * * *           1 1 1 1 1       0 0 0 0 0           0
* * * * *           1 1 1 1 1       1 1 1 1 1           1 0
* * * * *           1 1 1 1 1       0 0 0 0 0           0 1 0
* * * * *           1 1 1 1 1       1 1 1 1 1           1 0 1 0
* * * * *           1 1 1 1 1       0 0 0 0 0           0 1 0 1 0

5)                  6)              7)                  8)
1                   1 2 3 4 5       01 02 03 04 05      1 0 1 0 1
1 0                 1 2 3 4 5       06 07 08 09 10      0 1 0 1
1 0 1               1 2 3 4 5       11 12 13 14 15      1 0 1
1 0 1 0             1 2 3 4 5       16 17 18 19 20      0 1
1 0 1 0 1           1 2 3 4 5       21 22 23 24 25      1

9)                  10)             11)                 12)
      1             * *   * *       01 02 03 04 05      2
   1    1           *  * *  *       05 04 03 02 01      2 4
  1   1   1         *   *   *       02 04 06 08 10      2 4 8
1   1   1   1       *       *       10 08 06 04 02      2 4 8 16
                    *       *       03 06 09 12 15      2 4 8 16 32
                                    15 12 09 06 03      2 4 8 16 32 64
13) *       *
    * *   * *
    *   *   *
    *       *
    *       *

1) Create a Matrix
2) Matrix Multiplication
3) Spiral Matrix rotation
4) Shift elements in Matrix


"""

# #############################################################################
# 1)  Conditional Statement
# #############################################################################

# ## if
"""
if <Condition>:
    statement     
"""
# number_01 = 6
# number_02 = 4
# number_03 = 4
#
# if number_01 < number_02:
#     print("Number 02 is greater then Number 01.")


# if else
# if number_01 > number_02:
#     print("Number 01 is greater then Number 02.")
# else:
#     print("Number 02 is greater then Number 01.")

# if elif else

# if number_01 > number_02:
#     print("Number 02 is greater then Number 01.")
#
# elif number_02 < number_03:
#     print("Number 03 is greater then Number 02.")
#
# else:
#     print("Number 02 is greater then Number 01.")

# Nested if else

# if number_01 > number_02:
#     if number_01 > number_03:
#         print("01 Number 01 is max")
#     else:
#         print("02 Number 03 is max")
#
# else:
#     if number_02 > number_03:
#         print("03 Number 02 is max")
#     else:
#         print("04 Number 03 is max")


# if number_01 < number_02 < number_03:
#     print("05 Number 03 is max")
#
# elif number_01 < number_02 and number_02 > number_03:
#     print("06 Number 02 is max")
#
# elif number_01 > number_02 and number_01 > number_03:
#     print("07 Number 01 is max")
#
# else:
#     print("08 Numbers are same")


# #############################################################################
# 2)  Break and Continue
# #############################################################################


# #############################################################################
# 3)  Looping Structure
# #############################################################################

# For
# while


"""
for i in range():
    print(i)    
"""
# For Loop
# for i in range(0, 5):
#     print(i)
#
# # While loop
# number = 0
# while number < 5:
#     print(number)
#     number += 1

# #############################################################################
# 4)  Nested loop
# #############################################################################

for i in range(0, 5):
    for j in range(0, i):
        print(j, end=" ")
    print('')


# #############################################################################
# 5)  Control looping
# #############################################################################

# Do while loop (by default enters in loop)
# number = 0
# while True:
#     if number > 5:
#         break
#     print(number)
#     number += 1

for i in range(0, 11, 2):
    if i % 2 == 0:
        print(i)
