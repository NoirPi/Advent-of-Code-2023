import re


def build_symbols_grid(lines):
    symbols = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c not in "1234567890.":
                symbols[(x, y)] = c
    return symbols


def calculate_part_numbers_sum(lines, symbols):
    part_numbers_sum = 0
    for y, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            for s_x, s_y in symbols:
                if (match.start() - 1 <= s_x <= match.end()) and (y - 1 <= s_y <= y + 1):
                    num = int(match.group())
                    part_numbers_sum += num
                    break
    return part_numbers_sum


def main():
    with open("input.txt") as f:
        lines = f.read().split("\n")

    symbols = build_symbols_grid(lines)
    part_numbers_sum = calculate_part_numbers_sum(lines, symbols)

    print(part_numbers_sum)


if __name__ == "__main__":
    main()
