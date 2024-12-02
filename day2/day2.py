import sys


def main():
    lines = list(map(lambda a: list(map(int, a.split())), sys.stdin.readlines()))

    def ok(prev: int, cur: int, decreasing: bool):
        return (prev < cur and decreasing) or (prev > cur and not decreasing)

    def is_safe_parameterized(
        line: list, decreasing: bool, start_idx: int, fail_left: bool
    ):
        if start_idx >= len(line) - 1:
            return True

        prev = line[start_idx]
        for i in range(start_idx + 1, len(line)):
            dif = abs(line[i] - prev)
            if dif < 1 or dif > 3 or not ok(prev, line[i], decreasing):
                if not fail_left:
                    return False

                return (
                    # try removing i-1
                    (
                        (
                            i - 2 >= 0
                            and 1 <= abs(line[i - 2] - line[i]) <= 3
                            and ok(line[i - 2], line[i], decreasing)
                        )
                        or i == 1
                    )
                    and is_safe_parameterized(line, decreasing, i, False)
                    or
                    # try removing i
                    (
                        (
                            (
                                i + 1 < len(line)
                                and 1 <= abs(prev - line[i + 1]) <= 3
                                and ok(prev, line[i + 1], decreasing)
                            )
                            or i == len(line) - 1
                        )
                        and is_safe_parameterized(line, decreasing, i + 1, False)
                    )
                )
            prev = line[i]
        return True

    def is_safe(line: list):
        return is_safe_parameterized(line, True, 0, False) or is_safe_parameterized(
            line, False, 0, False
        )

    def dampen_is_safe(line: list):
        return is_safe_parameterized(line, True, 0, True) or is_safe_parameterized(
            line, False, 0, True
        )

    # part 1
    print(sum(map(is_safe, lines)))

    # part 2
    print(sum(map(dampen_is_safe, lines)))


if __name__ == "__main__":
    main()
