import sys

def partition(string : str, part_len : int) -> list[str]:
    assert len(string) % part_len == 0
    string_list : list[str] = []
    for start in range(0, len(string), part_len): string_list.append(string[start:start+part_len])
    return string_list

def all_same(str_list : list[str]) -> bool:
    checked_val = str_list[0]
    for val in str_list[1:]:
        if val != checked_val: return False
    return True

def get_factors(n : int) -> list[int]:
    return [x for x in range(1, int(n / 2) + 1) if n % x == 0]

def is_invalid(n : int, parts_len : list[int]) -> bool:
    n_str : str = str(n)
    n_len = len(n_str)
    for checked_len in parts_len:
        if (n_len % checked_len != 0): continue
        parts = partition(n_str, checked_len)
        if all_same(parts): return True
    return False

def count_invalid(number_range : list[str]) -> int:
    tokens = number_range.split('-')
    n_1 = int(tokens[0])
    n_2 = int(tokens[1])
    s_1 = sum(n for n in range(n_1, n_2 + 1) if is_invalid(n, [2]))
    s_2 = sum(n for n in range(n_1, n_2 + 1) if is_invalid(n, get_factors(len(str(n)))))
    return (s_1, s_2)


line = sys.stdin.readline()
tokens = line.split(',')
s_0 = 0
s_1 = 0
for number_range in tokens:
    counters = count_invalid(number_range)
    s_0 += counters[0]
    s_1 += counters[1]
print((s_0, s_1))
