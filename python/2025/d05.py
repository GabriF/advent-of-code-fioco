def parse_range(s: str) -> tuple[int, int]:
    lo, hi = map(int, s.split('-'))
    return lo, hi


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not ranges:
        return []

    ranges = sorted(ranges)

    merged = [ranges[0]]
    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def read_input(input_string: str) -> tuple[list[str], list[str]]:
    lines = input_string.strip().splitlines()
    for i, line in enumerate(lines):
        if line == "":
            return (lines[:i], lines[i+1:])
    return (lines, [])


def main():
    import sys

    ranges_raw, ingredients_raw = read_input(sys.stdin.read())

    ranges = merge_ranges([parse_range(r) for r in ranges_raw])
    values = list(map(int, ingredients_raw))

    s_1 = sum(any(lo <= v <= hi for lo, hi in ranges) for v in values)

    s_2 = sum(hi - lo + 1 for lo, hi in ranges)

    print((s_1, s_2))

if __name__ == "__main__":
    main()
