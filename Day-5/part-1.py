def main():
    def parse_input(input_str):
        data = input_str.split("\n\n")
        _seeds = [int(i) for i in data[0][7:].split(" ")]
        _mappings = [[[int(i) for i in line.split(" ")] for line in mapping.splitlines()[1:]] for mapping in data[1:]]
        return _seeds, _mappings

    def apply_mappings(_seeds, _mappings):
        vals = _seeds
        for mapping in _mappings:
            new_vals = []
            for val in vals:
                new_val = val
                for dest, start, size in mapping:
                    if start <= val < start + size:
                        new_val = val - start + dest
                        break
                new_vals.append(new_val)
            vals = new_vals
        return min(vals)

    input_data = open("input.txt", "r").read()
    seeds, mappings = parse_input(input_data)

    result1 = apply_mappings(seeds, mappings)
    print(result1)


if __name__ == "__main__":
    main()
