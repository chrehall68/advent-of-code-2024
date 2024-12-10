from collections import *
from typing import *
import sys


def main():
    lines = sys.stdin.read().splitlines()
    lines = [list(map(int, line)) for line in lines]

    # setup
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    rows = len(lines)
    cols = len(lines[0])

    # part 1
    def dfs1(i: int, r: int, c: int) -> set:
        # base case
        if lines[r][c] != i:
            return set()
        if i == 9:
            return {(r, c)}
        # recursive case
        total = set()
        for d in dirs:
            rp, cp = r + d[0], c + d[1]
            if 0 <= rp < rows and 0 <= cp < cols:
                total |= dfs1(i + 1, rp, cp)
        return total

    # part2
    def dfs2(i: int, r: int, c: int) -> set:
        # base case
        if lines[r][c] != i:
            return 0
        if i == 9:
            return 1
        # recursive case
        total = 0
        for d in dirs:
            rp, cp = r + d[0], c + d[1]
            if 0 <= rp < rows and 0 <= cp < cols:
                total += dfs2(i + 1, rp, cp)
        return total

    part1 = 0
    part2 = 0
    for r in range(rows):
        for c in range(cols):
            part1 += len(dfs1(0, r, c))
            part2 += dfs2(0, r, c)
    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
