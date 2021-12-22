def line_parser(file):
    f = open(file, 'r')
    lines = []
    for line in f:
        lines.append(line.rstrip())
    return lines


def parse_diagnostic_lines(input):
    list_of_dicts = []
    for i in range(len(input[0])):
        d = {'0': 0, '1': 0}
        for j in input:
            d[j[i]] += 1
        list_of_dicts.append(d)
    return list_of_dicts


def calculate_gamma(input):
    gamma_list = []
    for d in input:
        gamma_list.append(max(d, key=d.get))
    gamma_binary = ''.join(gamma_list)
    gamma_int = int(gamma_binary, 2)
    return gamma_int


def calculate_epsilon(input):
    epsilon_list = []
    for d in input:
        epsilon_list.append(min(d, key=d.get))
    epsilon_binary = ''.join(epsilon_list)
    epsilon_int = int(epsilon_binary, 2)
    return epsilon_int


def test():
    test_input = 'inputs/3-0.txt'
    test_lines = parse_diagnostic_lines(line_parser(test_input))
    assert (calculate_gamma(test_lines) == 22)
    assert (calculate_epsilon(test_lines) == 9)


if __name__ == "__main__":
    test()
    puzzle_input = 'inputs/3-1.txt'
    lines = line_parser(puzzle_input)
    d_lines = parse_diagnostic_lines(lines)
    gamma_rate = calculate_gamma(d_lines)
    epsilon_rate = calculate_epsilon(d_lines)
    print(gamma_rate * epsilon_rate)
