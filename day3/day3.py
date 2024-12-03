import sys
import re


def main():
    text = sys.stdin.read()

    # part 1
    regex = re.compile(r"mul\((\d+),(\d+)\)")
    total = 0
    item = regex.search(text)
    last_pos = 0
    while item is not None:
        a, b = map(int, item.groups())
        total += a * b
        last_pos = item.end()
        item = regex.search(text, pos=last_pos)
    print(total)

    # part 2
    regs = [
        re.compile(r"mul\((\d+),(\d+)\)"),
        re.compile(r"do\(\)"),
        re.compile(r"don't\(\)"),
    ]
    total = 0
    last_pos = 0
    enabled = True
    while True:
        first_match_idx = float("inf")
        first_match = None
        first_match_reg_idx = float("inf")
        for i, reg in enumerate(regs):
            item = reg.search(text, last_pos)
            if item is not None and item.start() < first_match_idx:
                first_match = item
                first_match_idx = item.start()
                first_match_reg_idx = i
        if first_match is None:
            break
        if first_match_reg_idx == 0:
            # was "mul"
            if enabled:
                a, b = map(int, first_match.groups())
                total += a * b
        elif first_match_reg_idx == 1:
            # "do"
            enabled = True
        else:
            # "don't"
            enabled = False

        last_pos = first_match.end()

    print(total)


if __name__ == "__main__":
    main()
