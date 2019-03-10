"""
1) Program to accept the strings which contains all vowels
2) Palindrome numbers in a list
3) Number to words like 121 converts one two one or one hundred twenty one
"""


# #############################################################################
# 1) Program to accept the strings which contains all vowels
# #############################################################################

def is_vowel(word):
    """

    :param word:
    :return:
    """
    return word.startswith(('a', 'e', 'i', 'o', 'u'))


def list_vowels(string):
    """
    create list of vowels from string
    :param string:
    :return:
    """
    vowels = list()
    for word in string.split(" "):
        if is_vowel(word.lower()):
            vowels.append(word)

    print(vowels)


# input_string = str(input("Enter string"))
# list_vowels(input_string)


# #############################################################################
# 2) Palindrome numbers in a list
# #############################################################################


def is_palindrome(number):
    """
    check if given number has odd or even digit
    :param number:
    :return:
    """
    for i, j in zip(number, number[::-1]):
        if i != j:
            return False

    return True


# print(is_palindrome("1231"))

# #############################################################################
# 3) Number to words like 121 converts one two one or one hundred twenty one
# #############################################################################

NUM_TO_WORD = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine', 0: 'zero', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
    30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
    80: 'eighty', 90: 'ninety'
}


def basic_number_to_word(number):
    """

    :return:
    """
    words = list()
    for i in str(number):
        words.append(NUM_TO_WORD.get(int(i)))

    return " ".join(words)


# print(basic_number_to_word(1234))

# #############################################################################

ONE_TO_19 = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine', 0: 'zero', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}

NINETEEN_TO_90 = {
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
    70: 'seventy', 80: 'eighty', 90: 'ninety'
}

HUNDREDS = {
    100: 'hundred', 1000: 'thousand', 1000000: 'million', 1000000000: 'billion'
}


def number_to_word(number):
    """
    Number to Word
    :param number:
    :return:
    """
    if number in ONE_TO_19:
        return ONE_TO_19.get(number)

    elif number < 100:

        if num < 100:
            return nums_20_90[num / 10 - 2] + (
                '' if num % 10 == 0 else ' ' + nums_0_19[num % 10])
            # find the largest key smaller than num
        maxkey = max([key for key in nums_dict.keys() if key <= num])
        return num2words(num / maxkey) + ' ' + nums_dict[maxkey] + (
            '' if num % maxkey == 0 else ' ' + num2words(num % maxkey))