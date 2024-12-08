from collections import defaultdict
import sys


def main():
    lines = sys.stdin.read().strip().splitlines()

    # part 1 and 2
    # get locations, then figure out all combinations
    letter_locations = defaultdict(list)
    rows = len(lines)
    cols = len(lines[0])
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] != ".":
                letter_locations[lines[r][c]].append((r, c))
    antinodes1 = [[False for _ in range(cols)] for _ in range(rows)]
    antinodes2 = [[False for _ in range(cols)] for _ in range(rows)]
    for _, locations in letter_locations.items():
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                a, b = locations[i], locations[j]
                delta_r, delta_c = b[0] - a[0], b[1] - a[1]

                # part 1
                added = b[0] + delta_r, b[1] + delta_c
                subbed = a[0] - delta_r, a[1] - delta_c
                if 0 <= added[0] < rows and 0 <= added[1] < cols:
                    antinodes1[added[0]][added[1]] = True
                if 0 <= subbed[0] < rows and 0 <= subbed[1] < cols:
                    antinodes1[subbed[0]][subbed[1]] = True

                # part 2
                cur = b
                while 0 <= cur[0] < rows and 0 <= cur[1] < cols:
                    antinodes2[cur[0]][cur[1]] = True
                    cur = cur[0] + delta_r, cur[1] + delta_c
                cur = a
                while 0 <= cur[0] < rows and 0 <= cur[1] < cols:
                    antinodes2[cur[0]][cur[1]] = True
                    cur = cur[0] - delta_r, cur[1] - delta_c

    print(sum(sum(el) for el in antinodes1))
    print(sum(sum(el) for el in antinodes2))


if __name__ == "__main__":
    main()
