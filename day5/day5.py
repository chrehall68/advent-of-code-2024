from collections import defaultdict, deque
import sys


def main():
    lines = list(map(lambda a: a.strip(), sys.stdin.readlines()))
    # befores[a] = {x, y, z} means a should be printed before x, y, and z
    befores = defaultdict(set)
    i = 0
    while lines[i] != "":
        a, b = map(int, lines[i].split("|"))
        # a must be printed before b
        befores[a].add(b)

        i += 1
    to_ints = lambda a: list(map(int, a.split(",")))
    prints = list(map(to_ints, lines[i + 1 :]))

    # part 1
    total = 0
    part2_total = 0
    for p in prints:
        seen = set()
        valid = True
        i = 0
        while i < len(p) and valid:
            item = p[i]
            seen.add(item)
            if len(befores[item].intersection(seen)) != 0:
                # something appears before the item
                # but the item should've appeared before it
                # thus invalid
                valid = False
            i += 1
        if valid:
            total += p[len(p) // 2]
        else:
            # use topsort order to get middle item
            indegrees = [0 for _ in range(len(p))]
            for item in p:
                for i in range(len(p)):
                    if p[i] in befores[item]:
                        indegrees[i] += 1
            q = deque()
            for i in range(len(p)):
                if indegrees[i] == 0:
                    q.append(p[i])
            result = []
            while len(result) < len(p):  # technically, only need till len(p)//2
                item = q.popleft()
                result.append(item)
                for i in range(len(p)):
                    if p[i] in befores[item]:
                        indegrees[i] -= 1
                        if indegrees[i] == 0:
                            q.append(p[i])
            part2_total += result[len(p) // 2]

    print(total)
    print(part2_total)


if __name__ == "__main__":
    main()
