from collections import *
from typing import *
import sys


def main():
    lines = sys.stdin.read().splitlines()
    line = list(map(lambda c: int(c), lines[0]))
    total_spaces = sum(line)

    # setup
    spaces = [-1 for _ in range(total_spaces)]
    lengths = []
    starts = []
    cur = 0
    id = 0
    for i in range(len(line)):
        if i % 2 == 0:
            # file
            starts.append(cur)
            for _ in range(line[i]):
                spaces[cur] = id
                cur += 1
            id += 1
            lengths.append(line[i])
        else:
            # empty space
            cur += line[i]
    # part1
    # now move to front
    spaces1 = spaces.copy()
    back = total_spaces - 1
    front = 0
    while back >= 0 and spaces1[back] == -1:
        back -= 1
    while front < total_spaces and spaces1[front] != -1:
        front += 1
    while front < back:
        spaces1[front] = spaces1[back]
        spaces1[back] = -1
        front += 1
        back -= 1
        while back >= 0 and spaces1[back] == -1:
            back -= 1
        while front < total_spaces and spaces1[front] != -1:
            front += 1
    # calculate checksum
    print(sum(max(i * el, 0) for i, el in enumerate(spaces1)))
    # part2
    # probably should use a segment tree or smth else here
    # since we need to be able to quickly find minimum idx of place
    # that contains at least lengths[i] empties in a row, then be able
    # to update that when we move i back and also when we reduce # of empties
    spaces2 = spaces.copy()
    for i in range(id - 1, -1, -1):
        cur_span = 0
        start_locat = None
        for j in range(starts[i]):
            if spaces2[j] == -1:
                cur_span += 1
            else:
                cur_span = 0

            if cur_span >= lengths[i]:
                # possible, stop here
                start_locat = j - cur_span + 1
                break
        if start_locat:
            for j in range(lengths[i]):
                spaces2[starts[i] + j] = -1
                spaces2[start_locat + j] = i

    print(sum(max(i * el, 0) for i, el in enumerate(spaces2)))


if __name__ == "__main__":
    main()
