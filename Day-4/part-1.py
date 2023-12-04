import re


def calculate_score(winning, ours):
    return sum(num in winning for num in ours)


def main():
    with open("input.txt") as file:
        lines = file.read().strip().split("\n")
    ans = 0

    for line in lines:
        parts = re.split(r"\s+", line)
        winning = list(map(int, parts[2:12]))
        ours = list(map(int, parts[13:]))

        score = calculate_score(winning, ours)

        if score > 0:
            ans += 2 ** (score - 1)

    print(ans)


if __name__ == "__main__":
    main()
