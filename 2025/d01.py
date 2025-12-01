file_name = 'd01.txt'
max_val = 100
curr = 50
res = 0
direction_mult = {'L' : -1, 'R' : 1}
with open(f'2025/input/{file_name}', 'r') as file:
    for line in file.readlines():
        line : str = line.strip()
        direction : str = line[0]
        count : int = int(line[1:])
        curr = (curr + count * direction_mult[direction])

        if curr < 0: curr = max_val + curr
        elif curr > 99: curr = curr % max_val

        if curr == 0: res += 1
print(res)
