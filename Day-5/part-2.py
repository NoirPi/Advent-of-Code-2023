def parse_input(input_str):
    data = input_str.split("\n\n")
    _seeds = [int(i) for i in data[0][7:].split(" ")]
    _mappings = [[[int(i) for i in line.split(" ")] for line in mapping.splitlines()[1:]] for mapping in data[1:]]
    return _seeds, _mappings


def carve(span_start, span_end, map_start, map_end):
    a, b = span_start, span_end
    c, d = map_start, map_end

    overlap_start, overlap_end = max(a, c), min(b, d)

    if overlap_start > overlap_end:
        return [], [(a, b)]
    to_map = [(overlap_start, overlap_end)]
    extra = [(a, overlap_start - 1)] * (a < overlap_start) + [(overlap_end + 1, b)] * (overlap_end < b)
    return to_map, extra


def get_ranges(_seeds, _mappings):
    ranges = [(_seeds[i], _seeds[i + 1] + _seeds[i] - 1) for i in range(0, len(_seeds), 2)]
    _mappings = [[[dest - start, start, start + size - 1] for dest, start, size in mapping] for mapping in _mappings]

    for mapping in _mappings:
        new_ranges = []
        for seed_span in ranges:
            unprocessed = [seed_span]
            for offset, map_start, map_end in mapping:
                new_unprocessed = []
                for span_start, span_end in unprocessed:
                    to_map, extra = carve(span_start, span_end, map_start, map_end)
                    new_unprocessed += extra
                    new_ranges += [(a + offset, b + offset) for a, b in to_map]
                unprocessed = new_unprocessed
            new_ranges += unprocessed
        ranges = new_ranges

    return min(start for start, _ in ranges)


if __name__ == "__main__":
    input_data = open("input.txt", "r").read()
    seeds, mappings = parse_input(input_data)

    result2 = get_ranges(seeds, mappings)

    print(result2)
