import re
from collections import defaultdict
from math import prod


def build_symbols_grid(lines):
    symbols = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c not in "1234567890.":
                symbols[(x, y)] = c
    return symbols


def build_gears_grid(lines, symbols):
    gears = defaultdict(list)
    for y, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            for (s_x, s_y), c in symbols.items():
                if (match.start() - 1 <= s_x <= match.end()) and (y - 1 <= s_y <= y + 1):
                    if c == "*":
                        num = int(match.group())
                        gears[(s_x, s_y)].append(num)
                    break
    return gears


def main():
    with open("input.txt") as f:
        lines = f.read().split("\n")

    symbols = build_symbols_grid(lines)
    gears = build_gears_grid(lines, symbols)
    calculations = sum(prod(part_nums) for part_nums in gears.values() if len(part_nums) == 2)
    print(calculations)


if __name__ == "__main__":
    main()
