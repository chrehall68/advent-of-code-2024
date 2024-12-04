import sys


def main():
    lines = sys.stdin.readlines()
    word = "XMAS"
    dirs = [
        (1, 0),  # down
        (-1, 0),  # up
        (0, 1),  # right
        (0, -1),  # left
        (1, 1),  # down right
        (1, -1),  # down left
        (-1, 1),  # up right
        (-1, -1),  # up left
    ]

    # part 1
    # match word going in any direction
    count = 0
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            for dir in dirs:
                i = 0
                ri, ci = r, c
                rp, cp = dir
                while (
                    i < len(word)
                    and 0 <= ri < len(lines)
                    and 0 <= ci < len(lines[0])
                    and lines[ri][ci] == word[i]
                ):
                    ri += rp
                    ci += cp
                    i += 1
                count += i == len(word)
    print(count)

    # part 2
    # look for an a
    count = 0
    for r in range(1, len(lines) - 1):
        for c in range(1, len(lines[0]) - 1):
            diagonal_left = [(r - 1, c - 1), (r, c), (r + 1, c + 1)]
            diagonal_right = [(r - 1, c + 1), (r, c), (r + 1, c - 1)]
            diagonal_left = set(list(map(lambda a: lines[a[0]][a[1]], diagonal_left)))
            diagonal_right = set(list(map(lambda a: lines[a[0]][a[1]], diagonal_right)))
            if (
                diagonal_left == diagonal_right == {"M", "A", "S"}
                and lines[r][c] == "A"
            ):
                count += 1
    print(count)


if __name__ == "__main__":
    main()
