def create_rgb(r, g, b):
    return {"r": r, "g": g, "b": b}


def power(rgb):
    return rgb["r"] * rgb["g"] * rgb["b"]


def max_rgb(rgb, other):
    rgb["r"] = max(rgb["r"], other["r"])
    rgb["g"] = max(rgb["g"], other["g"])
    rgb["b"] = max(rgb["b"], other["b"])


def parse_line(line):
    result = []
    _, rest = line.strip().split(": ")
    sets = rest.split("; ")
    for gameset in sets:
        info = create_rgb(0, 0, 0)
        colors = gameset.split(", ")
        for color in colors:
            num, name = color.split(" ")
            if name == "red":
                info["r"] = int(num)
            elif name == "green":
                info["g"] = int(num)
            elif name == "blue":
                info["b"] = int(num)
        result.append(info)
    return result


def part_2(games):
    total = 0
    for i, game in enumerate(games):
        minimum = create_rgb(0, 0, 0)
        for gameset in game:
            max_rgb(minimum, gameset)

        total += power(minimum)
    print("part 2:", total)


def main():
    games = []
    with open("input.txt", "r") as f:
        for line in f:
            games.append(parse_line(line))
    part_2(games)


if __name__ == "__main__":
    main()
