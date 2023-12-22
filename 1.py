# https://adventofcode.com/2023/day/1

import fileinput

DIGITS = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def get_number(line):
    first_digit, first_idx = None, len(line)
    last_digit, last_idx = None, -1
    for digit in DIGITS.keys():
        lidx = line.find(digit)
        if lidx != -1 and lidx < first_idx:
            first_digit = DIGITS[digit]
            first_idx = lidx
        ridx = line.rfind(digit)
        if ridx != -1 and ridx > last_idx:
            last_digit = DIGITS[digit]
            last_idx = ridx
    result = first_digit * 10 + last_digit
    return result

if __name__ == "__main__":
    result = 0
    for line in fileinput.input():
        result += get_number(line)
    print(result)
