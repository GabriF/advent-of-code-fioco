import sys


def is_within(x: int, r: tuple[int, int]) -> bool:
    return r[0] <= x <= r[1]


def range_overlap(r_1: tuple[int, int], r_2: tuple[int, int]) -> bool:
    return _range_overlap_helper(r_1, r_2) or _range_overlap_helper(r_2, r_1)


def _range_overlap_helper(r_1: tuple[int, int], r_2: tuple[int, int]) -> bool:
    return is_within(r_1[0], r_2) or is_within(r_1[1], r_2)


def build_ranges(ranges_as_str: list[str]) -> list[tuple[int, int]]:
    ranges_list = []
    for record in ranges_as_str:
        tokens = record.split("-")
        r_min = int(tokens[0])
        r_max = int(tokens[1])
        r = (r_min, r_max)
        add_range(ranges_list, r)
    return ranges_list


def add_range(ranges_list: list[tuple[int, int]], new_range: tuple[int, int]) -> None:
    for curr_range_index, curr_range in enumerate(ranges_list):
        if range_overlap(new_range, curr_range):
            new_range_min = min(new_range[0], curr_range[0])
            new_range_max = max(new_range[1], curr_range[1])
            new_range = (new_range_min, new_range_max)
            ranges_list.pop(curr_range_index)
            add_range(ranges_list, new_range)
            return
    ranges_list.append(new_range)


def read_input(input_string: str) -> tuple[list[str], list[str]]:
    lines = input_string.strip().split("\n")
    ingredients_ranges = []
    ingredients_list = []
    for i, line in enumerate(lines):
        if line == "":
            ingredients_list = lines[i+1:]
            break
        ingredients_ranges.append(line)
    return (ingredients_ranges, ingredients_list)


def main():
    ingredients_ranges, ingredients_list = read_input(sys.stdin.read())
    ranges_list = build_ranges(ingredients_ranges)

    s_1 = 0
    for r in ranges_list:
        for val in ingredients_list:
            val_int = int(val)
            if is_within(val_int, r):
                s_1 += 1

    s_2 = 0
    for r in ranges_list:
        s_2 += r[1] - r[0] + 1

    print((s_1, s_2))


if __name__ == "__main__":
    main()
