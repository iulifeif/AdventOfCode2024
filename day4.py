import re


def read_from_file() -> list[str]:
    matrix = []
    with open("inputs/day4.txt", 'r') as file:
        line = file.readline()
        while line:
            matrix.append(line.strip())
            line = file.readline()
    return matrix


XMAS = ['X', 'M', 'A', 'S']


def find_word_forward(matrix, index_line, index_column, letter_pos):
    if letter_pos == len(XMAS):
        return True
    if index_column == len(matrix[index_line]):
        return False
    if matrix[index_line][index_column] == XMAS[letter_pos]:
        return find_word_forward(matrix, index_line, index_column + 1, letter_pos + 1)
    return False


def find_word_backward(matrix, index_line, index_column, letter_pos):
    if letter_pos == len(XMAS):
        return True
    if index_column == -1:
        return False
    if matrix[index_line][index_column] == XMAS[letter_pos]:
        return find_word_backward(matrix, index_line, index_column - 1, letter_pos + 1)
    return False


def find_word_up(matrix, index_line, index_column, letter_pos):
    if letter_pos == len(XMAS):
        return True
    if index_line == -1:
        return False
    if matrix[index_line][index_column] == XMAS[letter_pos]:
        return find_word_up(matrix, index_line - 1, index_column, letter_pos + 1)
    return False


def find_word_down(matrix, index_line, index_column, letter_pos):
    if letter_pos == len(XMAS):
        return True
    if index_line == len(matrix):
        return False
    if matrix[index_line][index_column] == XMAS[letter_pos]:
        return find_word_down(matrix, index_line + 1, index_column, letter_pos + 1)
    return False


def find_word_diagonal_up_left(matrix, index_line, index_column, letter_pos):
    if letter_pos == len(XMAS):
        return True
    if index_line == -1 or index_column == -1:
        return False
    if matrix[index_line][index_column] == XMAS[letter_pos]:
        return find_word_diagonal_up_left(matrix, index_line - 1, index_column - 1, letter_pos + 1)
    return False


def find_word_diagonal_up_right(matrix, index_line, index_column, letter_pos):
    if letter_pos == len(XMAS):
        return True
    if index_line == -1 or index_column == len(matrix[index_line]):
        return False
    if matrix[index_line][index_column] == XMAS[letter_pos]:
        return find_word_diagonal_up_right(matrix, index_line - 1, index_column + 1, letter_pos + 1)
    return False


def find_word_diagonal_down_right(matrix, index_line, index_column, letter_pos):
    if letter_pos == len(XMAS):
        return True
    if index_line == len(matrix) or index_column == len(matrix[index_line]):
        return False
    if matrix[index_line][index_column] == XMAS[letter_pos]:
        return find_word_diagonal_down_right(matrix, index_line + 1, index_column + 1, letter_pos + 1)
    return False


def find_word_diagonal_down_left(matrix, index_line, index_column, letter_pos):
    if letter_pos == len(XMAS):
        return True
    if index_line == len(matrix) or index_column == -1:
        return False
    if matrix[index_line][index_column] == XMAS[letter_pos]:
        return find_word_diagonal_down_left(matrix, index_line + 1, index_column - 1, letter_pos + 1)
    return False


def find_word(matrix, index_line, index_column):
    return sum([find_word_forward(matrix, index_line, index_column, 0),
                find_word_backward(matrix, index_line, index_column, 0),
                find_word_up(matrix, index_line, index_column, 0),
                find_word_down(matrix, index_line, index_column, 0),
                find_word_diagonal_up_left(matrix, index_line, index_column, 0),
                find_word_diagonal_up_right(matrix, index_line, index_column, 0),
                find_word_diagonal_down_right(matrix, index_line, index_column, 0),
                find_word_diagonal_down_left(matrix, index_line, index_column, 0)])


def first_star() -> int:
    matrix = read_from_file()
    number_of_found_words = 0
    for index_line in range(len(matrix)):
        for index_column in range(len(matrix)):
            if matrix[index_line][index_column] == "X":
                number_of_found_words += find_word(matrix, index_line, index_column)

    return number_of_found_words


def check_max_pattern(matrix, index_line, index_column):
    chars = [matrix[index_line - 1][index_column - 1],
             matrix[index_line - 1][index_column + 1],
             matrix[index_line + 1][index_column + 1],
             matrix[index_line + 1][index_column - 1]]
    if chars.count('S') != 2 or chars.count('M') != 2:
        return False
    if (matrix[index_line - 1][index_column - 1] == matrix[index_line + 1][index_column + 1]
            or matrix[index_line + 1][index_column - 1] == matrix[index_line - 1][index_column + 1]):
        return False
    return True


def second_star() -> int:
    matrix = read_from_file()
    number_of_found_words = 0
    for index_line in range(1, len(matrix)-1):
        for index_column in range(1, len(matrix)-1):
            if matrix[index_line][index_column] == "A":
                number_of_found_words += int(check_max_pattern(matrix, index_line, index_column))
    return number_of_found_words


print(first_star())
print(second_star())
