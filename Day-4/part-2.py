import re


def calculate_score(winning, ours):
    return sum(num in winning for num in ours)


def build_copies(lines):
    n = len(lines)
    copies = [[] for _ in range(n)]

    for i, line in enumerate(lines):
        parts = re.split(r"\s+", line)
        idx = parts.index("|")
        winning = list(map(int, parts[2:idx]))
        ours = list(map(int, parts[idx + 1:]))

        score = sum(num in winning for num in ours)
        for j in range(i + 1, i + score + 1):
            copies[i].append(j)

    return copies


def calculate_total_score(copies):
    n = len(copies)
    score = [1 for _ in range(len(copies))]

    for i in range(n - 1, -1, -1):
        for j in copies[i]:
            score[i] += score[j]

    return sum(score)


def main():
    with open("input.txt") as file:
        lines = file.read().strip().split("\n")
    copies = build_copies(lines)
    total_score = calculate_total_score(copies)

    print(total_score)


if __name__ == "__main__":
    main()
