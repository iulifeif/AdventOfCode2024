import re


def read_from_file() -> tuple[list[tuple[int, int]], list[list[int]]]:
    rules = []
    page_numbers = []
    first_half = True
    with open("inputs/day5.txt", 'r') as file:
        line = file.readline()
        while line:
            line = line.strip()
            if not line:
                first_half = False
                line = file.readline()
                continue
            if first_half:
                x, y = re.split(r"[|,]", line)
                rules.append((int(x), int(y)))
            else:
                page_numbers.append([int(x) for x in re.split(r"[|,]", line)])
            line = file.readline()
    return rules, page_numbers


def page_order_is_valid(page: list, rules: list[tuple]) -> bool:
    for page_index in range(len(page) - 1):
        if (page[page_index + 1], page[page_index]) in rules:
            return False

    return True


def first_star() -> int:
    rules, page_numbers = read_from_file()
    count_valid_page_middle_number = 0
    for page in page_numbers:
        if page_order_is_valid(page, rules):
            count_valid_page_middle_number += page[int(len(page) / 2)]
    return count_valid_page_middle_number


def switch_pages(page: list, page_index1: int, page_index2: int) -> list:
    temporary_slot = page[page_index1]
    page[page_index1] = page[page_index2]
    page[page_index2] = temporary_slot
    return page


def order_pages(page: list, rules: list[tuple]) -> list:
    for page_index in range(len(page)-1):
        if (page[page_index], page[page_index+1]) not in rules:
            correct_order = False
            for page_index_2 in range(page_index+1, len(page)):
                if (page[page_index], page[page_index_2]) in rules:
                    correct_order = True
                    page = switch_pages(page, page_index1=page_index, page_index2=page_index_2)
                    break
            if not correct_order:
                page = switch_pages(page, page_index1=page_index, page_index2=page_index+1)
    return page


def second_star() -> int:
    rules, page_numbers = read_from_file()
    count_valid_page_middle_number = 0
    for page in page_numbers:
        if not page_order_is_valid(page, rules):
            page = order_pages(page, rules)
            while not page_order_is_valid(page, rules):
                page = order_pages(page, rules)
            count_valid_page_middle_number += page[int(len(page) / 2)]
    return count_valid_page_middle_number


print(first_star())
print(second_star())
