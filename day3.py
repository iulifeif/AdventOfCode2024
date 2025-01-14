import re


def read_input():
    entire_str = ""
    with open("inputs/day3.txt", 'r') as file:
        text_line = file.readline()
        while text_line:
            entire_str += text_line
            text_line = file.readline()

    return entire_str


def first_star():
    input_text = read_input()
    matches = [(int(a), int(b)) for a, b in re.findall(r'mul\((\d+),(\d+)\)', input_text)]
    return sum(match[0] * match[1] for match in matches)


def second_star():
    input_string = read_input()
    mul_regex = re.compile(r'mul\((\d+),(\d+)\)')
    enable_regex = re.compile(r"do\(\)|don't\(\)")

    enabled = True
    total_sum = 0

    matches = re.split(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', input_string)
    for match in matches:
        match = match.strip()
        if enable_regex.fullmatch(match):
            enabled = match == "do()"
        elif mul_match := mul_regex.fullmatch(match):
            if enabled:
                x, y = map(int, mul_match.groups())
                total_sum += x * y

    return total_sum


print(first_star())
print(second_star())
