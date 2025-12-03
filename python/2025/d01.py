import math
import sys

max_val = 100
curr = 50
s_1 = 0
direction_mult = {'L': -1, 'R': 1}
for line in sys.stdin.readlines():
    line = line.strip()
    direction = line[0]
    count = int(line[1:])

    curr += (count * direction_mult[direction])
    if curr < 0: curr = max_val + curr
    curr = curr % max_val

    if curr == 0: s_1 += 1
print(s_1)
