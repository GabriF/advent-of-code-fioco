import sys


def roll_is_accessible(grid: list[str], pos_i: int, pos_j: int) -> bool:
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
            if is_valid_pos and grid[curr_i][curr_j] == "@":
                adjacent_roll_counter += 1
                if adjacent_roll_counter >= 4:
                    return False
    return True


def main():
    grid = sys.stdin.read().strip().split("\n")

    s = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@" and roll_is_accessible(grid, i, j):
                s += 1

    print(s)


if __name__ == "__main__":
    main()
