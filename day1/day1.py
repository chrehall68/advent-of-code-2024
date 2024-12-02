from collections import Counter, defaultdict


def main():
    left = []
    right = []

    fname = input()
    f = open(fname)
    for line in f.readlines():
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)
    left.sort()
    right.sort()

    # part 1
    total = 0
    for a, b in zip(left, right):
        total += abs(a - b)
    print(total)

    # part 2
    right = defaultdict(int, Counter(right))
    print(sum(map(lambda a: a * right[a], left)))


if __name__ == "__main__":
    main()
