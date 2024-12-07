from typing import List
import sys


def main():
    lines = sys.stdin.read().strip().split("\n")

    # part 1
    def dfs1(total: int, rest: List[int], idx: int, cur: int):
        if idx >= len(rest):
            return total == cur
        if cur > total:
            return False
        # recursive case
        # try mult, try add
        res = dfs1(total, rest, idx + 1, cur + rest[idx])
        res = res or dfs1(total, rest, idx + 1, cur * rest[idx])
        return res

    # part 2
    def dfs2(total: int, rest: List[int], idx: int, cur: int):
        if idx >= len(rest):
            return total == cur
        if cur > total:
            return False
        # recursive case
        # try mult, try add, try concat
        res = dfs2(total, rest, idx + 1, cur + rest[idx])
        res = res or dfs2(total, rest, idx + 1, cur * rest[idx])
        res = res or dfs2(total, rest, idx + 1, int(str(cur) + str(rest[idx])))
        return res

    total1 = 0
    total2 = 0
    for line in lines:
        l = line.split()
        l[0] = l[0].strip(":")
        tot, *rest = map(int, l)
        if dfs1(tot, rest, 1, rest[0]):
            total1 += tot
            total2 += tot
        elif dfs2(tot, rest, 1, rest[0]):
            total2 += tot
    print(total1)
    print(total2)


if __name__ == "__main__":
    main()
