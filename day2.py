def read_from_file() -> list[list]:
    matrix_of_numbers = []
    with open("inputs/day2.txt", 'r') as file:
        index_line = file.readline()
        while index_line:
            x = index_line.strip()
            x = [int(x) for x in x.split()]
            matrix_of_numbers.append(x)
            index_line = file.readline()
    return matrix_of_numbers


def first_star() -> int:
    matrix_of_numbers = read_from_file()
    number_of_safe_reports = 0

    for index_line in range(len(matrix_of_numbers)):
        asc_order = matrix_of_numbers[index_line][1] > matrix_of_numbers[index_line][0]
        if asc_order:
            if is_safe_asc(matrix_of_numbers[index_line]):
                number_of_safe_reports += 1
        else:
            if is_safe_desc(matrix_of_numbers[index_line]):
                number_of_safe_reports += 1

    return number_of_safe_reports


def second_star():
    matrix_of_numbers = read_from_file()
    number_of_safe_reports = 0

    for index_line in range(len(matrix_of_numbers)):
        if determine_asc_order(matrix_of_numbers[index_line]):
            if is_safe_asc(matrix_of_numbers[index_line]):
                number_of_safe_reports += 1
            elif is_safe_with_removal_asc(matrix_of_numbers[index_line]):
                number_of_safe_reports += 1
        else:
            if is_safe_desc(matrix_of_numbers[index_line]):
                number_of_safe_reports += 1
            elif is_safe_with_removal_desc(matrix_of_numbers[index_line]):
                number_of_safe_reports += 1

    return number_of_safe_reports


def determine_asc_order(numbers: list[int]) -> bool:
    asc = 0
    desc = 0
    for index, number in enumerate(numbers):
        if index == 0:
            continue
        if numbers[index - 1] < numbers[index]:
            asc += 1
        if numbers[index - 1] > numbers[index]:
            desc += 1

    if asc >= desc:
        return True
    else:
        return False


def is_safe_asc(numbers: list[int]) -> bool:
    return all(numbers[index_column] < numbers[index_column + 1]
               and 0 <= numbers[index_column + 1] - numbers[index_column] <= 3
               for index_column in range(len(numbers) - 1))


def is_safe_desc(numbers: list[int]) -> bool:
    return all(numbers[index_column + 1] < numbers[index_column]
               and 0 <= numbers[index_column] - numbers[index_column + 1] <= 3
               for index_column in range(len(numbers) - 1))


def is_safe_with_removal_asc(numbers: list[int]):
    for index in range(len(numbers)):
        list_with_removed_item = numbers[:index] + numbers[index + 1:]
        if is_safe_asc(list_with_removed_item):
            return True
    return False


def is_safe_with_removal_desc(numbers: list[int]):
    for index in range(len(numbers)):
        list_with_removed_item = numbers[:index] + numbers[index + 1:]
        if is_safe_desc(list_with_removed_item):
            return True
    return False


print(first_star())
print(second_star())
