import sys


def is_roll(grid: list[str], row: int, col: int) -> bool:
    return grid[row][col] == "@"


def remove_roll(grid: list[str], row: int, col: int) -> None:
    line = grid[row]
    new_row = line[:col] + "x" + line[col + 1:]
    grid[row] = new_row


def is_roll_accessible(grid: list[str], row: int, col: int) -> bool:
    row_number = len(grid)
    col_number = len(grid[row])

    count = 0
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue

            ni, nj = row + di, col + dj
            if 0 <= ni < row_number and 0 <= nj < col_number and is_roll(grid, ni, nj):
                count += 1
                if count >= 4:
                    return False

    return True



def main():
    grid = sys.stdin.read().strip().split("\n")

    s_1 = sum(1
              for i in range(len(grid)) 
              for j in range(len(grid[i]))
              if is_roll(grid, i, j) and is_roll_accessible(grid, i, j)
    )

    s_2 = 0
    while True:
        removed = [(i, j)
        for i in range(len(grid))
        for j in range(len(grid[i]))
        if is_roll(grid, i, j) and is_roll_accessible(grid, i, j)
        ]

        if len(removed) == 0: break

        for i, j in removed: remove_roll(grid, i, j)

        s_2 += len(removed)

    print((s_1, s_2))


if __name__ == "__main__":
    main()
