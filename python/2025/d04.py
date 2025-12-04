import sys


def is_roll(grid: list[str], i: int, j: int) -> bool:
    return grid[i][j] == "@"


def remove_roll(grid: list[str], i: int, j: int) -> None:
    line = grid[i]
    new_line = line[:j] + "x" + line[j + 1:]
    grid[i] = new_line


def is_roll_accessible(grid: list[str], pos_i: int, pos_j: int) -> bool:
    adjacent_roll_counter = 0
    grid_i_max = len(grid)
    grid_j_max = len(grid[pos_i])
    for i in range(-1, 2):
        for j in range(-1, 2):
            curr_i = pos_i + i
            curr_j = pos_j + j

            is_not_same_pos = not (i == 0 and j == 0)
            is_pos_positive = curr_i >= 0 and curr_j >= 0
            is_pos_inside_grid = curr_i < grid_i_max and curr_j < grid_j_max
            is_valid_pos = is_not_same_pos and is_pos_positive and is_pos_inside_grid
            if is_valid_pos and is_roll(grid, curr_i, curr_j):
                adjacent_roll_counter += 1
                if adjacent_roll_counter >= 4:
                    return False
    return True


def main():
    grid = sys.stdin.read().strip().split("\n")

    s_1 = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if is_roll(grid, i, j) and is_roll_accessible(grid, i, j):
                s_1 += 1

    s_2 = 0
    s_old = -1
    while s_2 != s_old:
        s_old = s_2
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if is_roll(grid, i, j) and is_roll_accessible(grid, i, j):
                    s_2 += 1
                    remove_roll(grid, i, j)

    print((s_1, s_2))


if __name__ == "__main__":
    main()
