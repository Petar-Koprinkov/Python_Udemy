def validate_matrix(my_matrix):
    if not my_matrix or not all(isinstance(row, list) for row in my_matrix):
        raise ValueError("Input should be a 2D list.")
    row_length = len(my_matrix[0])
    if not all(len(row) == row_length for row in my_matrix):
        raise ValueError("Matrix is not rectangular.")
    return True


def transpose_matrix(my_matrix):
    return [list(row) for row in zip(*my_matrix)]


def row_sums(my_matrix):
    return [sum(row) for row in my_matrix]


def column_products(my_matrix):
    transpose = transpose_matrix(my_matrix)
    return [prod(column) for column in transpose]


def prod(my_list):
    result = 1
    for num in my_list:
        result *= num
    return result


def spiral_traversal(my_matrix):
    result = []
    while my_matrix:
        result += my_matrix.pop(0)
        if my_matrix and my_matrix[0]:
            for row in my_matrix:
                result.append(row.pop())
        if my_matrix:
            result += my_matrix.pop()[::-1]
        if my_matrix and my_matrix[0]:
            for row in my_matrix[::-1]:
                result.append(row.pop(0))
    return result


def rotate_90(my_matrix):
    return [list(row) for row in zip(*my_matrix[::-1])]


def rotate_180(my_matrix):
    return [row[::-1] for row in my_matrix[::-1]]


"""
Example for Intput
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# matrix = [
#     [1],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


try:
    validate_matrix(matrix)
    print("Transpose:", transpose_matrix(matrix))
    print("Row Sums:", row_sums(matrix))
    print("Column Products:", column_products(matrix))
    print("Spiral Traversal:", spiral_traversal([row[:] for row in matrix]))
    print("Rotate 90°:", rotate_90(matrix))
    print("Rotate 180°:", rotate_180(matrix))
except ValueError as ve:
    print("Error:", ve)
