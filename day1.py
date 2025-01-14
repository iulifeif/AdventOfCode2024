from collections import Counter


def read_from_file():
    first_list = []
    second_list = []
    with open("inputs/day1.txt", 'r') as file:
        line = file.readline()
        while line:
            x, y = line.strip().split("  ")
            first_list.append(int(x))
            second_list.append(int(y))
            line = file.readline()
    return first_list, second_list


def first_star():
    first_list, second_list = read_from_file()
    first_list.sort()
    second_list.sort()
    return sum(abs(first_list[index] - second_list[index]) for index in range(len(first_list)))


def second_star():
    first_list, second_list = read_from_file()
    appearance_numbers_first_list = Counter(first_list)

    return sum(number * appearance_numbers_first_list[number] for number in second_list)


print(first_star())
print(second_star())
