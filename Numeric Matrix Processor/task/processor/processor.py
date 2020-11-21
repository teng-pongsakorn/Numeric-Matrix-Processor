
import copy

MENU_MESSAGE = """1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit"""

TRANSPOSE_MENU = '''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice: > '''


def read_matrix():
    n, m = map(int, input("Enter size of first matrix: > ").split())
    data = []
    print("Enter first matrix:")
    for r in range(n):
        data.append(list(map(convert_str_to_int_or_float, input().split())))
    assert len(data) == n and all(len(row) == m for row in data)
    return data


def sum_matrix(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return None
    else:
        result = []
        for row_a, row_b in zip(A, B):
            row = []
            for a, b in zip(row_a, row_b):
                row.append(a+b)
            result.append(row)
        return result


def scalar_multiply(A, c):
    result = []
    for row in A:
        result.append([a*c for a in row])
    return result


def matrix_multiplication(A, B):
    n_a, m_a = len(A), len(A[0])
    n_b, m_b = len(B), len(B[0])
    if m_a != n_b:
        return None

    result = []
    for r in range(n_a):
        row_result = []
        for c in range(m_b):
            row_result.append(sum(A[r][i]*B[i][c] for i in range(m_a)))
        result.append(row_result)
    return result


def main_diagonal_transpose(A):
    result = []
    n, m = len(A), len(A[0])
    for r in range(m):
        new_row = [A[c][r] for c in range(n)]
        result.append(new_row)
    return result


def side_diagonal_transpose(A):
    result = []   # shape: m x n
    n, m = len(A), len(A[0])

    for r in range(m-1, -1, -1):
        new_row = [A[c][r] for c in range(n-1, -1, -1)]
        result.append(new_row)
    return result


def vertical_line_transpose(A):
    result = []
    for row in A:
        result.append(row[::-1])
    return result


def horizontal_line_transpose(A):
    return A[::-1]


def matrix_transpose(A, method):
    if method == '1':
        return main_diagonal_transpose(A)
    elif method == '2':
        return side_diagonal_transpose(A)
    elif method == '3':
        return vertical_line_transpose(A)
    elif method == '4':
        return horizontal_line_transpose(A)


def get_matrix_value(A, r, c):
    try:
        return A[r][c]
    except IndexError:
        return 0


def det_2x2(A):
    return get_matrix_value(A, 0, 0) * get_matrix_value(A, 1, 1) - get_matrix_value(A, 0, 1) * get_matrix_value(A, 1, 0)


def matrix_determinant(A):
    n = len(A)
    if n == 1:
        return A[0][0]

    if n == 2:
        return det_2x2(A)

    # use first column as M_ij * c_ij
    c = 0
    sub_matrix = [row[1:] for row in A]
    total = 0
    for r in range(n):
        c_ij = 1 if (c + r) % 2 == 0 else -1
        M_ij = [sub_matrix[i] for i in range(n) if i != r]
        total += A[r][c] * c_ij * matrix_determinant(M_ij)
    return total


def get_adjacent(A, r, c):
    B = copy.deepcopy(A)   # copy the matrix
    n = len(B)
    cofactor = 1 if (r + c) % 2 == 0 else -1
    # drop r-th row
    B.pop(r)
    # drop c-th column
    for row in B:
        row.pop(c)
    return cofactor * matrix_determinant(B)


def get_adjacent_matrix(A):
    result = []
    for r in range(len(A)):
        row = []
        for c in range(len(A)):
            row.append(get_adjacent(A, r, c))
        result.append(row)
    return result


def trunc_matrix(A):
    import math
    for r in range(len(A)):
        for c in range(len(A[0])):
            A[r][c] = math.trunc(A[r][c] * 100) / 100


def inverse_matrix(A):
    det_A = matrix_determinant(A)
    if det_A != 0:
        # find transpose of the adjacent matrix
        adj_A = get_adjacent_matrix(A)
        adj_A_transpose = matrix_transpose(adj_A, method='1')  # diag transpose
        A_inv = scalar_multiply(adj_A_transpose, 1/det_A)
        trunc_matrix(A_inv)
        return A_inv


def print_matrix(A):
    for row in A:
        print(*row, sep=' ')
    print()


def convert_str_to_int_or_float(x):
    try:
        return int(x)
    except ValueError:
        return float(x)


def read_constant():
    x = input("Enter constant: > ")
    return convert_str_to_int_or_float(x)


def run_menu_matrix_addition():
    A = read_matrix()
    B = read_matrix()
    C = sum_matrix(A, B)
    if C is not None:
        print("The result is:")
        print_matrix(C)
    else:
        print("ERROR\n")


def run_menu_scalar_multiply():
    A = read_matrix()
    c = read_constant()
    print("The result is:")
    print_matrix(scalar_multiply(A, c))


def run_menu_matrix_multiplication():
    A = read_matrix()
    B = read_matrix()
    C = matrix_multiplication(A, B)
    if C is None:
        print("The operation cannot be performed.\n")
    else:
        print("The result is:")
        print_matrix(C)


def run_transpose():
    choice = input(TRANSPOSE_MENU)
    A = read_matrix()
    AT = matrix_transpose(A, choice)
    print('The result is:')
    print_matrix(AT)


def run_determinant():
    A = read_matrix()
    det = matrix_determinant(A)
    print("The result is:\n{}\n".format(det))


def run_inverse():
    A = read_matrix()
    A_inv = inverse_matrix(A)
    if A_inv is not None:
        print("The result is:")
        print_matrix(A_inv)
    else:
        print("This matrix doesn't have an inverse.")


def main():
    while True:
        print(MENU_MESSAGE)
        user_choice = input("Your choice: > ")
        if user_choice == '0':
            break
        elif user_choice == '1':
            run_menu_matrix_addition()
        elif user_choice == '2':
            run_menu_scalar_multiply()
        elif user_choice == '3':
            run_menu_matrix_multiplication()
        elif user_choice == '4':
            run_transpose()
        elif user_choice == '5':
            run_determinant()
        elif user_choice == '6':
            run_inverse()
        else:
            print("Invalid input. Please try again.")


if __name__=='__main__':
    main()
