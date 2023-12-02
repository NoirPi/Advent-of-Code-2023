def part1(lines) -> int:
    calibration_sum = 0
    for line in lines:
        first_digit = next((c for c in line if c.isdigit()), "0")
        last_digit = next((c for c in reversed(line) if c.isdigit()), "0")
        calibration_value = int(first_digit + last_digit)
        calibration_sum += calibration_value

    return calibration_sum


with open("input.txt", "r") as f:
    file = f.readlines()
    print(part1(file))
