import sys
from tqdm import tqdm


def main():
    lines = sys.stdin.read().split("\n")
    for i in range(len(lines)):
        (*el,) = lines[i]
        lines[i] = el

    # figure out start position
    cols = len(lines[0])
    rows = len(lines)
    start_pos = None
    i = 0
    while start_pos is None:
        r, c = i // cols, i % cols
        if lines[r][c] == "^":
            start_pos = r, c
        i += 1

    def explore():
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        possible_dirs = [[set() for _ in range(cols)] for _ in range(rows)]
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        r, c = start_pos
        dir = 0
        i = 0
        while 0 <= r < rows and 0 <= c < cols and dir not in possible_dirs[r][c]:
            visited[r][c] = True
            possible_dirs[r][c] |= {dir}
            rp, cp = r + dirs[dir][0], c + dirs[dir][1]
            if 0 <= rp < rows and 0 <= cp < cols and lines[rp][cp] == "#":
                # rotate
                dir += 1
                dir %= len(dirs)
            else:
                # move forward
                r, c = rp, cp
            i += 1
        if 0 <= r < rows and 0 <= c < cols and dir in possible_dirs[r][c]:
            return -1, visited
        return sum(sum(el) for el in visited), visited

    # part 1
    p1, visited = explore()
    print(p1)

    # part 2
    total = 0
    for i in tqdm(range(rows * cols)):
        r, c = i // cols, i % cols
        if lines[r][c] != "^" and lines[r][c] != "#" and visited[r][c]:
            # try putting one here
            lines[r][c] = "#"
            total += explore()[0] == -1
            lines[r][c] = "."
    print(total)


if __name__ == "__main__":
    main()
