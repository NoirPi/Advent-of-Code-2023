def part2(lines) -> int:
    import re

    digit_dict = {"one": "1", "two": "2", "three": "3",
                  "four": "4", "five": "5", "six": "6",
                  "seven": "7", "eight": "8", "nine": "9"}
    digit_regex = re.compile(r"(?=(\d|" + "|".join(digit_dict) + r"))")

    calibration_sum = 0
    for line in lines:
        digit_iter = digit_regex.finditer(line)
        first_d = next(digit_iter)
        first_digit = digit_dict.get(first_d.group(1), first_d.group(1))

        last_d = first_d
        for last_d in digit_iter:
            pass
        last_digit = digit_dict.get(last_d.group(1), last_d.group(1))

        calibration_value = int(first_digit + last_digit)
        calibration_sum += calibration_value

    return calibration_sum


with open("input.txt", "r") as f:
    file = f.readlines()
    print("Part 2:", part2(file))
