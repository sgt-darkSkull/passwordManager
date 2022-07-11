import random
import array


# Generates password

class LowerBound(Exception):
    pass


def generate(max_len):
    try:

        max_len = int(max_len)

        if max_len < 8 or max_len > 50:
            raise LowerBound

        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                             'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                             'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                             'z']

        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                             'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                             'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                             'Z']

        SYMBOLS = ['@', '#', '%', '=', '?', '.', '*', '(', ')']

        COMBINED_LIST = UPCASE_CHARACTERS + DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS + LOCASE_CHARACTERS

        temp_pass = random.choice(DIGITS)
        temp_pass += random.choice(UPCASE_CHARACTERS)
        temp_pass += random.choice(LOCASE_CHARACTERS)
        temp_pass += random.choice(SYMBOLS)
        temp_pass += random.choice(DIGITS)
        temp_pass += random.choice(UPCASE_CHARACTERS)
        temp_pass += random.choice(LOCASE_CHARACTERS)
        temp_pass += random.choice(SYMBOLS)

        temp_pass_list = []
        for x in range(max_len - 8):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)

        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

        password = ""
        for x in temp_pass_list:
            password = password + x

        return password
    except ValueError:
        return 'Please give Integer Value '
    except LowerBound:
        return 'Character Limit is 5-50'
