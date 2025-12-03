import sys


def find_max_digit_pair(string : str, ) -> int:
    max = 0
    for position_1, digit_1 in enumerate(string):
        for digit_2 in string[position_1 + 1:]:
            curr_num = int(digit_1 + digit_2)
            if max < curr_num: max = curr_num
    return max

res = sum(find_max_digit_pair(line) for line in sys.stdin.readlines())
print(res)