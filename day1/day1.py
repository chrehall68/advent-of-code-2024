from collections import Counter, defaultdict
import sys


def main():
    left = []
    right = []

    for line in sys.stdin.readlines():
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)
    left.sort()
    right.sort()

    # part 1
    print(sum(map(lambda p: abs(p[0] - p[1]), zip(left, right))))

    # part 2
    right = defaultdict(int, Counter(right))
    print(sum(map(lambda a: a * right[a], left)))


if __name__ == "__main__":
    main()
