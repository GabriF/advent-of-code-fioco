def is_repeated(n : int) -> bool:
    n_str : str = str(n)
    n_len_half : int = int(len(n_str) / 2)
    return n_str[:n_len_half] == n_str[n_len_half:]

def count_invalid(number_range : list[str]) -> int:
    tokens = number_range.split('-')
    n_1 = int(tokens[0])
    n_2 = int(tokens[1])
    return sum(n for n in range(n_1, n_2 + 1) if is_repeated(n))

file_name = '2025/input/d02.txt'

with open(file_name, 'r') as file:
    line = file.readline().strip()
    tokens = line.split(',')
    s = sum(count_invalid(number_range) for number_range in tokens)
    print(s)