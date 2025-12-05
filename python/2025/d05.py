import sys

lines = sys.stdin.read().strip().split("\n")
ranges = list()
id_start = 0
for line in lines:
    id_start += 1
    line = line.strip()
    if line == "": break
    tokens = line.split("-")
    start = int(tokens[0])
    end = int(tokens[1])
    ranges.append(range(start, end + 1))

s = 0
for line in lines[id_start:]:
    line = line.strip()
    val = int(line)
    for r in ranges:
        if val in r:
            s += 1
            break

print(s)